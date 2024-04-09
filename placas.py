import cv2

# URL de la transmisión de la cámara IP
url = 'http://192.168.1.2:8080/video'

# Iniciar el objeto de captura de video
cap = cv2.VideoCapture(url)

# Verificar si la captura se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la transmisión de la cámara.")
    exit()

# Bucle principal para leer y mostrar la transmisión de la cámara
while True:
    # Leer el cuadro de la transmisión de la cámara
    ret, frame = cap.read()

    # Verificar si se pudo leer correctamente
    if not ret:
        print("No se pudo recibir cuadro. Saliendo...")
        break

    # Mostrar el cuadro
    cv2.imshow('Camara IP', frame)

    # Salir del bucle al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()