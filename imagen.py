from PIL import Image

# Abrir la imagen
imagen_original = Image.open("auto.jpg")

# Convertir la imagen
imagen_bn = imagen_original.convert("L")

# Redimensionar la imagen
nuevo_tamano = (300, 300)  # Especifica el nuevo tamaño en píxeles
imagen_redimensionada = imagen_bn.resize(nuevo_tamano)

# Guardar la imagen redimensionada
imagen_redimensionada.save("auto_nuevo.jpg")

# Mostrar la imagen redimensionada
imagen_redimensionada.show()
