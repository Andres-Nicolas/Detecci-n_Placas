import cv2

# URL de la transmisión de la cámara IP
url = 'http://172.18.60.86:8080//video'

# Iniciar el objeto de captura de video
cap = cv2.VideoCapture(url)

cv2.namedWindow('Camara en vivo', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Camara en vivo', 640, 480)

# Verificar si la captura se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la camara")
    exit()
camaraTexto=""

# Bucle principal para leer y mostrar la transmisión de la cámara
while True:
    # Leer el cuadro de la transmisión de la cámara
    ret, frame = cap.read()

    # Verificar si se pudo leer correctamente
    if not ret:
        print("No se pudo recibir cuadro. Saliendo...")
        break

    # Mostrar el cuadro
    cv2.imshow('Camara en vivo', frame)

    # Salir del bucle al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Liberar el objeto de captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()