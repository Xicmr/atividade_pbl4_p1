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

### Exemplo de saída

```
============================================================
ETAPA 1: LEITURA DO PDF
============================================================
Arquivo: Citação_de_Oscar_Wilde.pdf
Caracteres extraídos: 312

ETAPA 2: TOKENIZAÇÃO
============================================================
Total de tokens gerados: 72
Primeiros 20 tokens: ['Ser', 'você', 'mesmo', ...]

ETAPA 3: ANÁLISE
============================================================
Total de palavras : 61
Total de pontuação: 11

Top 10 palavras mais frequentes:
 'a' → 5x
 'de' → 3x
 ...
Tokenização concluída com sucesso!
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
Tamanho da imagem : (300, 300)
Kernel do filtro  : 7x7 pixels

Média de pixels:
  Original    : 75.42
  Com ruído   : 75.38
  Após filtro : 75.42

Desvio padrão dos pixels (quanto maior = mais ruído):
  Original    : 87.51
  Com ruído   : 100.12
  Após filtro : 88.34

Imagem salva em: resultado_gaussiano.png
==================================================
```

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
