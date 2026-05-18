# Importa o modulo 're' (expressoes regulares), que permite
# buscar padroes dentro de strings, usado aqui para tokenizar
import re


# Importa o modulo pymupdf
import pymupdf as fitz

# O arquivo deve estar na mesma pasta do script.
CAMINHO_PDF = "Citação de Oscar Wilde.pdf"

# Abre o arquivo PDF usando PyMuPDF.
# fitz.open() retorna um objeto 'Document' com todas as paginas.
doc = fitz.open(CAMINHO_PDF)

# Variavel que vai acumular o texto extraido de todas as paginas
texto_completo = ""

# Percorre cada pazgina do documento.
for pagina in doc:
    # get_text() extrai todo o texto visível da página como string.
    texto_completo += pagina.get_text()

# Fecha o arquivo PDF após a leitura para liberar recursos do sistema
doc.close()

# Remove as quebras de linha (\n) que o PDF insere ao final de cada linha visual
# .strip() remove espaços extras no início e no fim do texto.
texto_limpo = texto_completo.replace("\n", " ").strip()

# Exibe o resultado da leitura do PDF
print("=" * 60)
print("ETAPA 1: LEITURA DO PDF")
print("=" * 60)
print(f"\nArquivo: {CAMINHO_PDF}")                      
print(f"Caracteres extraídos: {len(texto_limpo)}")      # total de caracteres no texto
print(f"\nTexto extraído:")
print(f"  {texto_limpo}")                               # exibe o texto completo extraído


# Aqui usamos re.findall() com uma expressão regular (regex)
# re.findall() retorna uma lista com todas as ocorrências
# encontradas no texto, na ordem em que aparecem.

tokens = re.findall(r"[\w']+|[.,!?;:\u2014\u2013]", texto_limpo)

# Exibe os resultados da tokenização
print("\n" + "=" * 60)
print("ETAPA 2: TOKENIZAÇÃO")
print("=" * 60)
print(f"\nTotal de tokens gerados: {len(tokens)}")  # quantidade total de tokens

# Fatia da lista: tokens[0:20] — os 20 primeiros elementos
print(f"\nPrimeiros 20 tokens:")
print(f"  {tokens[:20]}")

# Fatia da lista: tokens[-10:] — os 10 últimos elementos
print(f"\nÚltimos 10 tokens:")
print(f"  {tokens[-10:]}")


# Importa Counter, uma subclasse de dicionário especializada
from collections import Counter
.
# t.isalpha() retorna True se o token contém apenas letras
# (ignora números, pontuação e símbolos mistos como "dar-lhe").
so_palavras = [t for t in tokens if t.isalpha()]

# List comprehension que filtra apenas tokens NÃO alfabéticos
so_pontuacao = [t for t in tokens if not t.isalpha()]

# Conta a frequência de cada palavra.
frequencia = Counter(t.lower() for t in so_palavras)

# most_common(10) retorna uma lista com os 10 pares (palavra, contagem)
mais_comuns = frequencia.most_common(10)

# Exibe o resumo da análise
print("\n" + "=" * 60)
print("ETAPA 3: ANÁLISE")
print("=" * 60)
print(f"\nTotal de palavras : {len(so_palavras)}")    # quantidade de tokens que são palavras
print(f"Total de pontuação: {len(so_pontuacao)}")     # quantidade de tokens que são pontuação

# Percorre a lista de tuplas (palavra, frequência) e exibe cada par
print(f"\nTop 10 palavras mais frequentes:")
for palavra, freq in mais_comuns:
    # f-string formata a saída: 'palavra' → Nx
    print(f"  '{palavra}' → {freq}x")

print("\n" + "=" * 60)
print("Tokenização concluída com sucesso!")
print("=" * 60)
