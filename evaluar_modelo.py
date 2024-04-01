from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
from io import BytesIO
from sklearn.neural_network import MLPClassifier
import base64
import joblib

app = Flask(__name__)
model = joblib.load("modelo_entrenado.pkl")
# Nombres de las clases
clases = ['Camiseta/top', 'Pantalón', 'Jersey', 'Vestido', 'Abrigo', 'Sandalia', 'Camisa', 'Zapatilla', 'Bolso', 'Botín']

# Función para preprocesar la imagen
def procesamiento(imagen):
    from PIL import Image

    # Abrir la imagen
    imagen_original = Image.open(imagen)

    # Convertir la imagen
    imagen_bn = imagen_original.convert("L")

    # Redimensionar la imagen
    nuevo_tamano = (28, 28)  # Especifica el nuevo tamaño en píxeles
    imagen_redimensionada = imagen_bn.resize(nuevo_tamano)

    # Guardar la imagen redimensionada
    imagen_redimensionada.save("auto_nuevo.jpg")
    
    return imagen_redimensionada


@app.route('/predict', methods=['POST'])
def predict():
    imagen = request.files['imagen']
    # Procesar la imagen
    imagen_procesada = procesamiento(imagen)
    
    # Convertir la imagen a un array de numpy
    imagen_array = np.array(imagen_procesada)
    
    # Aplanar el array de la imagen
    imagen_aplanada = imagen_array.flatten()
    
    # Realizar la predicción utilizando el modelo cargado
    prediccion = model.predict([imagen_aplanada])
    
    # Devolver la predicción como una respuesta JSON
    return jsonify({'prediction': str(prediccion)})
    
  

if __name__ == '__main__':
    app.run(debug=True)
