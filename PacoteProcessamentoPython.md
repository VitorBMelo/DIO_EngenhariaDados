Vamos construir um pacote Python simples para realizar algumas operações básicas de processamento de imagens. Utilizaremos a biblioteca Pillow (PIL Fork) para as manipulações e o OpenCV para algumas operações mais avançadas.

![Website_cover_-_2023-03-03T213814 692](https://github.com/user-attachments/assets/6c1c720b-ecc5-4112-b17b-61f63a34f7e2)

Estrutura do Pacote
-------------------

```
meu_pacote_imagens/
├── __init__.py
├── processing.py
├── filters.py
├── __main__.py

```

-   **`__init__.py`:** Indica que este diretório é um pacote Python.
-   **`processing.py`:** Contém funções para operações básicas, como redimensionamento, rotação, etc.
-   **`filters.py`:** Contém funções para aplicar filtros, como blur, detecção de bordas, etc.
-   **`__main__.py`:** Um script de exemplo para testar as funcionalidades do pacote.

Código do Pacote
----------------

**`processing.py`**

Python

```
from PIL import Image

def resize_image(image_path, new_width, new_height):
    """Redimensiona uma imagem.

    Args:
        image_path: Caminho para a imagem.
        new_width: Nova largura da imagem.
        new_height: Nova altura da imagem.

    Returns:
        PIL.Image: Imagem redimensionada.
    """

    img = Image.open(image_path)
    img = img.resize((new_width, new_height))
    return img

def rotate_image(image_path, angle):
    """Rotaciona uma imagem.

    Args:
        image_path: Caminho para a imagem.
        angle: Ângulo de rotação em graus.

    Returns:
        PIL.Image: Imagem rotacionada.
    """

    img = Image.open(image_path)
    img = img.rotate(angle)
    return img

```
