# OpenCV: biblioteca principal de Visão Computacional.
# Usada para desenhar formas, aplicar o filtro bilateral
# e salvar a imagem resultado.
import cv2

# NumPy: biblioteca para operações com arrays e matrizes numéricas.
# Usada para criar a imagem e gerar o ruído aleatório.
import numpy as np

# Matplotlib: biblioteca de visualização de gráficos e imagens.
# Usada para exibir as três imagens lado a lado.
import matplotlib.pyplot as plt

# Define a semente do gerador aleatório do NumPy.
# Com a mesma semente, o ruído gerado será sempre igual,
# garantindo que o resultado seja reproduzível em qualquer máquina.
np.random.seed(42)

# Cria uma imagem em tons de cinza (2D) de 300x300 pixels,
# preenchida com zeros (cor preta).
# dtype=np.uint8 significa que cada pixel vai de 0 (preto) a 255 (branco).
imagem_original = np.zeros((300, 300), dtype=np.uint8)

# Desenha um retângulo claro (valor 200) preenchido (-1) na imagem.
# Parâmetros: imagem, canto superior esquerdo, canto inferior direito,
#             cor, espessura (-1 = preenchido)
cv2.rectangle(imagem_original, (50, 50), (250, 250), 200, -1)

# Desenha um círculo cinza escuro (valor 100) preenchido no centro.
# Parâmetros: imagem, centro (x, y), raio, cor, espessura (-1 = preenchido)
cv2.circle(imagem_original, (150, 150), 60, 100, -1)

# np.random.normal(média, desvio_padrão, tamanho):
ruido = np.random.normal(0, 40, imagem_original.shape).astype(np.int16)

# Soma a imagem original com o ruído pixel a pixel.
imagem_com_ruido = np.clip(
    imagem_original.astype(np.int16) + ruido,  # soma pixel a pixel
    0,    # valor mínimo (preto)
    255   # valor máximo (branco)
).astype(np.uint8)


# cv2.bilateralFilter() aplica o filtro bilateral.
imagem_filtrada = cv2.bilateralFilter(
    imagem_com_ruido,
    d=9,
    sigmaColor=75,
    sigmaSpace=75
)


# Cria uma figura com 3 subplots lado a lado (1 linha, 3 colunas).
# figsize=(12, 4) define o tamanho da figura em polegadas.
fig, eixos = plt.subplots(1, 3, figsize=(12, 4))

# Subplot 1: imagem original sem ruído
eixos[0].imshow(imagem_original, cmap='gray')  # cmap='gray' exibe em tons de cinza
eixos[0].set_title('Original')                  # título do painel
eixos[0].axis('off')                            # oculta os eixos x e y

# Subplot 2: imagem com ruído gaussiano adicionado
eixos[1].imshow(imagem_com_ruido, cmap='gray')
eixos[1].set_title('Com Ruído Gaussiano')
eixos[1].axis('off')

# Subplot 3: imagem após aplicação do filtro bilateral
eixos[2].imshow(imagem_filtrada, cmap='gray')
eixos[2].set_title('Após Filtro Bilateral')
eixos[2].axis('off')

# Ajusta automaticamente o espaçamento entre os subplots
plt.tight_layout()

# Salva a figura como arquivo PNG na pasta atual.
# dpi=120 define a resolução (pontos por polegada).
plt.savefig('resultado_bilateral.png', dpi=120)

# Exibe estatísticas no terminal como evidência da execução
print("=" * 50)
print("FILTRO BILATERAL — RESULTADO")
print("=" * 50)
print(f"\nTamanho da imagem   : {imagem_original.shape}")
print(f"Parâmetros do filtro: d=9, sigmaColor=75, sigmaSpace=75")
print(f"\nDesvio padrão dos pixels (quanto maior = mais ruído):")
print(f"  Original          : {imagem_original.std():.2f}")
print(f"  Com ruído         : {imagem_com_ruido.std():.2f}")
print(f"  Após filtro       : {imagem_filtrada.std():.2f}")
print(f"\nImagem salva em: resultado_bilateral.png")
print("=" * 50)
