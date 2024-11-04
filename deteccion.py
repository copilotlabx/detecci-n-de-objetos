import cv2
import time
import os
import json
from datetime import datetime

# Carpeta base para almacenar las capturas
BASE_CAPTURES_FOLDER = 'htdocs/captures'
DATA_JSON_PATH = 'htdocs/data.json'

# Crear carpeta base de capturas si no existe
if not os.path.exists(BASE_CAPTURES_FOLDER):
    os.makedirs(BASE_CAPTURES_FOLDER)

def process_frames():
    # Crear una subcarpeta única para esta sesión de capturas
    session_folder = os.path.join(BASE_CAPTURES_FOLDER, datetime.now().strftime("session_%Y%m%d_%H%M%S"))
    os.makedirs(session_folder, exist_ok=True)

    # Inicializa la cámara
    cap = cv2.VideoCapture(0)
    
    # Verifica si la cámara se abre correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    frames_captured = 0
    start_time = time.time()

    # Lista para almacenar información sobre cada captura
    capture_data = []

    # Mantener la cámara encendida durante 10 segundos y capturar una imagen cada segundo
    while frames_captured < 10 and (time.time() - start_time) < 10:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo capturar el cuadro del video.")
            break

        # Guardar la imagen en la subcarpeta de la sesión actual con un nombre único
        image_path = os.path.join(session_folder, f'captured_frame_{frames_captured}.jpg')
        cv2.imwrite(image_path, frame)

        # Almacenar datos de la captura
        capture_info = {
            "image_path": image_path,
            "timestamp": time.time()
        }
        capture_data.append(capture_info)
        print(f"Imagen guardada en {image_path}")

        # Espera un segundo antes de capturar la siguiente imagen
        frames_captured += 1
        time.sleep(1)

    # Libera la cámara después de 10 segundos
    cap.release()
    print("Capturas completadas y cámara liberada.")

    # Guardar los datos de las capturas en un archivo JSON
    # Cada sesión actualizará el archivo `data.json` con los datos de la nueva sesión
    all_sessions_data = []
    if os.path.exists(DATA_JSON_PATH):
        with open(DATA_JSON_PATH, 'r') as json_file:
            all_sessions_data = json.load(json_file)

    all_sessions_data.append({
        "session_folder": session_folder,
        "captures": capture_data
    })

    with open(DATA_JSON_PATH, 'w') as json_file:
        json.dump(all_sessions_data, json_file, indent=4)
    print(f"Datos de las capturas guardados en {DATA_JSON_PATH}")

if __name__ == '__main__':
    process_frames()
