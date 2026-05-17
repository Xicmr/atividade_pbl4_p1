
# OpenCV: biblioteca principal de Visão Computacional.
import cv2

# NumPy: biblioteca para operações com arrays e matrizes numéricas.
import numpy as np

# Matplotlib: biblioteca de visualização de gráficos e imagens.
import matplotlib.pyplot as plt

# Define a semente do gerador aleatório do NumPy.
np.random.seed(42)

# dtype=np.uint8 significa que cada pixel vai de 0 (preto) a 255 (branco).
imagem_original = np.zeros((300, 300), dtype=np.uint8)

# Desenha um retângulo branco (valor 200) preenchido (-1) na imagem.
# Parâmetros: imagem, canto superior esquerdo, canto inferior direito, cor, espessura
# espessura -1 significa preenchido
cv2.rectangle(imagem_original, (50, 50), (250, 250), 200, -1)

# Desenha um círculo cinza escuro (valor 100) preenchido no centro da imagem.
# Parâmetros: imagem, centro (x,y), raio, cor, espessura
cv2.circle(imagem_original, (150, 150), 60, 100, -1)

# np.random.normal(média, desvio_padrão, tamanho) gera valores
# aleatórios com distribuição normal (curva de sino).
ruido = np.random.normal(0, 40, imagem_original.shape).astype(np.int16)

# Soma a imagem original com o ruído.
imagem_com_ruido = np.clip(
    imagem_original.astype(np.int16) + ruido,  # soma pixel a pixel
    0,    # valor mínimo permitido (preto)
    255   # valor máximo permitido (branco)
).astype(np.uint8)  # converte de volta para o tipo de imagem padrão

# cv2.GaussianBlur() aplica o filtro gaussiano.
imagem_filtrada = cv2.GaussianBlur(imagem_com_ruido, (7, 7), 0)

# Cria uma figura com 3 subplots lado a lado (1 linha, 3 colunas).
fig, eixos = plt.subplots(1, 3, figsize=(12, 4))

# Subplot 1: imagem original sem ruído
eixos[0].imshow(imagem_original, cmap='gray')  # cmap='gray' exibe em tons de cinza
eixos[0].set_title('Original')                  # título do painel
eixos[0].axis('off')                            # oculta os eixos x e y

# Subplot 2: imagem com ruído gaussiano adicionado
eixos[1].imshow(imagem_com_ruido, cmap='gray')
eixos[1].set_title('Com Ruído Gaussiano')
eixos[1].axis('off')

# Subplot 3: imagem após aplicação do filtro gaussiano
eixos[2].imshow(imagem_filtrada, cmap='gray')
eixos[2].set_title('Após Filtro Gaussiano')
eixos[2].axis('off')

# Ajusta automaticamente o espaçamento entre os subplots
plt.tight_layout()

# Salva a figura como arquivo PNG na pasta atual.
# dpi=120 define a resolução (pontos por polegada).
plt.savefig('resultado_gaussiano.png', dpi=120)

# Exibe as estatísticas finais no terminal para evidência da execução
print("=" * 50)
print("FILTRO GAUSSIANO — RESULTADO")
print("=" * 50)
print(f"\nTamanho da imagem  : {imagem_original.shape}")
print(f"Kernel do filtro   : 7x7 pixels")
print(f"\nMédia de pixels:")
print(f"  Original         : {imagem_original.mean():.2f}")
print(f"  Com ruído        : {imagem_com_ruido.mean():.2f}")
print(f"  Após filtro      : {imagem_filtrada.mean():.2f}")
print(f"\nDesvio padrão dos pixels (quanto maior = mais ruído):")
print(f"  Original         : {imagem_original.std():.2f}")
print(f"  Com ruído        : {imagem_com_ruido.std():.2f}")
print(f"  Após filtro      : {imagem_filtrada.std():.2f}")
print(f"\nImagem salva em: resultado_gaussiano.png")
print("=" * 50)
