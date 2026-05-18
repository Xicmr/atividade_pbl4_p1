# atividade_pbl3_p1
# Atividades Práticas — IA: PLN e Visão Computacional

Repositório com duas atividades práticas desenvolvidas em Python, cobrindo técnicas de **Processamento de Linguagem Natural (PLN)** e **Visão Computacional**.

## Estrutura do Projeto

```
📦 praticas-ia/
├── pln_exp1.py              # Tokenização de texto extraído de PDF
├── visao_gaussiano_exp2.py           # Filtro Gaussiano para redução de ruído
├── Citação_de_Oscar_Wilde.pdf   # PDF de entrada para o script de PLN
└── README.md
```

---

## Atividade 1 — PLN: Tokenização com Leitura de PDF

**Arquivo:** `pln_exp1.py`

### Descrição

O script abre um arquivo PDF, extrai o texto de suas páginas e aplica técnicas de tokenização — dividindo o conteúdo em unidades menores chamadas **tokens** (palavras e sinais de pontuação). Ao final, realiza uma análise de frequência exibindo as palavras mais comuns no texto.

### Etapas

1. **Leitura do PDF** — usa `PyMuPDF (fitz)` para extrair texto de cada página
2. **Limpeza do texto** — remove quebras de linha desnecessárias com `.replace()` e `.strip()`
3. **Tokenização** — aplica `re.findall()` com regex para separar palavras e pontuação
4. **Análise** — usa `collections.Counter` para contar frequência e exibir o Top 10 de palavras

### Dependências

```bash
pip install pymupdf
```

### Como executar

> Coloque o arquivo `Citação_de_Oscar_Wilde.pdf` na mesma pasta do script.

```bash
python pln_exp1.py
```

### Resultado

```
============================================================
ETAPA 1: LEITURA DO PDF
============================================================

Arquivo: Citação de Oscar Wilde.pdf
Caracteres extraídos: 947

Texto extraído:
  Influenciar uma pessoa é dar-lhe a nossa própria alma. O indivíduo deixa de  pensar com os seus próprios pensamentos ou de arder com as suas próprias  paixões. As suas virtudes não lhe são naturais. Os seus pecados, se é que existe  tal coisa, são tomados de empréstimo. Torna-se o eco de uma música alheia, o  ator de um papel que não foi escrito para ele. O objectivo da vida é o  desenvolvimento próprio, a total percepção da própria natureza, é para isso que  cada um de nós vem ao mundo. Hoje em dia as pessoas têm medo de si próprias.  Esqueceram o maior de todos os deveres, o dever para consigo mesmos. É  verdade que são caridosas. Alimentam os esfomeados e vestem os pobres. Mas  as suas próprias almas morrem de fome e estão nuas. A coragem desapareceu da  nossa raça e se calhar nunca a tivemos realmente. O temor à sociedade, que é a  base da moral, e o temor a Deus, que é o segredo da religião, são as duas coisas  que nos governam.

============================================================
ETAPA 2: TOKENIZAÇÃO
============================================================

Total de tokens gerados: 201

Primeiros 20 tokens:
  ['Influenciar', 'uma', 'pessoa', 'é', 'dar', 'lhe', 'a', 'nossa', 'própria', 'alma', '.', 'O', 'indivíduo', 'deixa', 'de', 'pensar', 'com', 'os', 'seus', 'próprios']

Últimos 10 tokens:
  ['religião', ',', 'são', 'as', 'duas', 'coisas', 'que', 'nos', 'governam', '.']

============================================================
ETAPA 3: ANÁLISE
============================================================

Total de palavras : 178
Total de pontuação: 23

Top 10 palavras mais frequentes:
  'o' → 10x
  'de' → 9x
  'é' → 7x
  'que' → 7x
  'a' → 6x
  'os' → 5x
  'as' → 5x
  'da' → 5x
  'são' → 4x
  'e' → 4x

============================================================
Tokenização concluída com sucesso!
============================================================
```

---

##  Atividade 2 — Visão Computacional: Filtro Gaussiano

**Arquivo:** `visao_gaussiano_exp2.py`

### Descrição

O script gera uma **imagem sintética em tons de cinza**, adiciona **ruído gaussiano** para simular imperfeições de câmera e aplica o **Filtro Gaussiano** para suavizar e remover esse ruído. As três imagens são exibidas lado a lado e salvas em um arquivo PNG.

### Etapas

1. **Criação da imagem** — gera uma imagem 300×300 px com retângulo e círculo usando OpenCV
2. **Adição de ruído** — usa `np.random.normal()` com média 0 e desvio padrão 40
3. **Filtro Gaussiano** — aplica `cv2.GaussianBlur()` com kernel 7×7
4. **Visualização** — exibe e salva as 3 imagens comparativas em `resultado_gaussiano.png`

### Dependências

```bash
pip install opencv-python numpy matplotlib
```

### Como executar

```bash
python visao_gaussiano.py
```

### Saída gerada

- **`resultado_gaussiano.png`** — comparativo das três imagens: Original | Com Ruído | Após Filtro

```
==================================================
FILTRO GAUSSIANO — RESULTADO
==================================================

Tamanho da imagem  : (300, 300)
Kernel do filtro   : 7x7 pixels

Média de pixels:
  Original         : 77.24
  Com ruído        : 85.53
  Após filtro      : 85.53

Desvio padrão dos pixels (quanto maior = mais ruído):
  Original         : 90.71
  Com ruído        : 88.10
  Após filtro      : 81.31

Imagem salva em: resultado_gaussiano.png
==================================================
```
<img width="1440" height="480" alt="image" src="https://github.com/user-attachments/assets/c4dcf778-d988-480f-9c2a-431405ff47fd" />

---

##  Requisitos Gerais

- Python 3.8+
- Instale todas as dependências de uma vez:

```bash
pip install pymupdf opencv-python numpy matplotlib
```

---

## Conceitos Abordados

| Conceito | Script | Biblioteca |
|---|---|---|
| Tokenização | `pln_exp1.py` | `re`, `PyMuPDF` |
| Análise de frequência | `pln_exp1.py` | `collections.Counter` |
| Geração de imagem sintética | `visao_gaussiano_exp2.py` | `NumPy`, `OpenCV` |
| Ruído gaussiano | `visao_gaussiano_exp2.py` | `NumPy` |
| Filtro Gaussiano (blur) | `visao_gaussiano_exp2.py` | `OpenCV` |
| Visualização comparativa | `visao_gaussiano_exp2.py` | `Matplotlib` |

---
##  Autor

Desenvolvido como atividade prática acadêmica.

---

## 📄 Licença

Este projeto é de uso educacional.
