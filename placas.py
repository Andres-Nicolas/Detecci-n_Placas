<<<<<<< HEAD
import numpy as np
import cv2
import pytesseract 
from PIL import Image

#url de la camara puede variar la ip cambiarla por la que aparece en la app
url = 'http://172.18.60.86:8080//video'

transmision = cv2.VideoCapture(url)
cv2.namedWindow('Camara en vivo', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Camara en vivo', 640, 480)
=======

import cv2
import numpy as np
import pytesseract
from PIL import Image

# URL de la transmisión de la cámara IP
url = 'http://192.168.1.2:8080//video'

# Iniciar el objeto de captura de video
cap = cv2.VideoCapture(url)

>>>>>>> 89231dab5e94e7902beb7cf2c1e79c16dc7732a0

if not transmision.isOpened():
        print("No se pudo abrir la camara")
        exit()

camaraTexto=""
while True:
    ret, frame = transmision.read()

    if not ret:
        print("No se pudo recibir cuadro. Saliendo...")
        break
    
<<<<<<< HEAD
    cv2.rectangle(frame,(870,750), (1070,850),(0, 0, 0),cv2.FILLED)
    cv2.putText(frame,camaraTexto[0:7],(900,810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    alto,ancho, cam =frame.shape
    x1=int(ancho/3)
    x2=int(x1*2)
    y1=int(alto/3)
    y2=int(y1*2)

    cv2.rectangle(frame, (x1 +160, y1 +500), (1120, 940),(0,0,0), cv2.FILLED)
    cv2.putText(frame, 'leyendo', (x1+180, y1+550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,5,0),2)
    recorte=frame[y1:y2, x1:x2]

    mB= np.matrix(recorte[:,:,0])
    mG= np.matrix(recorte[:,:,1])
    mR= np.matrix(recorte[:,:,2])

    Color=cv2.absdiff(mG, mB)
    _,umbral =cv2.threshold(Color, 40 ,255, cv2.THRESH_BINARY)
    contornos ,_ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contornos= sorted(contornos, key=lambda x:cv2.contourArea(x), reverse=True)

    for contorno in contornos:
        area= cv2.contourArea(contorno)
        if area>500 and area>5000:
            x,y,an,al =cv2.boundingRect(contorno)
            xpi= x+x1
            ypi= y+y1
            xpf= x+an+x1
            ypf= y+al+y1

            cv2.rectangle(frame, (xpi,ypi),(xpf,ypf),(255,255,0),2)
            placa= frame[ypi:ypf,xpi:xpf]
            altoplaca,anchoplaca, colorplaca=placa.shape

            Mva= np.zeros((altoplaca, anchoplaca))

            mBp= np.matrix(placa[:,:,0])
            mGp= np.matrix(placa[:,:,1])
            mRp= np.matrix(placa[:,:,2])

            for col in range(0,altoplaca):
                for fil in range(0,anchoplaca):
                    Max= max(mRp[col,fil],mGp[col,fil], mBp[col,fil])
                    Mva[col,fil]=255-Max

            _,bin= cv2.threshold(Mva,150,255, cv2.THRESH_BINARY)
            bin= bin.reshape(altoplaca, anchoplaca)  
            bin= Image.fromarray(bin)
            bin= bin.convert("L")

            if altoplaca>=36 and anchoplaca>=82:
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                config= "--psm 1"
                texto= pytesseract.image_to_string(bin, config=config)

                if len(texto)>=7:
                    camaraTexto= texto
            
            break

    
    
    cv2.imshow('Camara en vivo', frame)

    tecla= cv2.waitKey(1)

    if  tecla & 0xFF == ord('q') or tecla & 0xFF == ord('Q') :
        break


transmision.release()
cv2.destroyAllWindows()
=======

    cv2.rectangle(frame,(400,400),(800,600),(0,0,0), cv2.FILLED)
    cv2.putText(frame,camaraTexto[0:7],(100,150),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    alto,ancho, cam =frame.shape
    x1=int(ancho/3)
    x2=int(x1*2)
    y1=int(alto/3)
    y2=int(y1*2)

    cv2.rectangle(frame, (x1 +160, y1 +500), (1120, 940),(0,0,0), cv2.FILLED)
    cv2.putText(frame, 'leyendo', (x1+180, y1+550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,5,0),2)
    recorte=frame[y1:y2, x1:x2]

    mB= np.matrix(recorte[:,:,0])
    mG= np.matrix(recorte[:,:,1])
    mR= np.matrix(recorte[:,:,2])

    Color=cv2.absdiff(mG, mB)
    _,umbral =cv2.threshold(Color, 40 ,255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contornos= sorted(contornos, key=lambda x:cv2.contourArea(x), reverse=True)

    for contorno in contornos:
        area= cv2.contourArea(contorno)
        if area>500 and area>5000:
            x,y,an,al =cv2.boundingRect(contorno)
            xpi= x+x1
            ypi= y+y1
            xpf= x+an+x1
            ypf= y+al+y1

            cv2.rectangle(frame, (xpi,ypi),(xpf,ypf),(255,255,0),2)
            placa= frame[ypi:ypf,xpi:xpf]
            altoplaca,anchoplaca, colorplaca=placa.shape

            Mva= np.zeros((altoplaca, anchoplaca))

            mBp= np.matrix(placa[:,:,0])
            mGp= np.matrix(placa[:,:,1])
            mRp= np.matrix(placa[:,:,2])

            for col in range(0,altoplaca):
                for fil in range(0,anchoplaca):
                    Max= max(mRp[col,fil],mGp[col,fil], mBp[col,fil])
                    Mva[col,fil]=255-Max
            
            _,bin= cv2.threshold(Mva,150,255, cv2.THRESH_BINARY)
            bin= bin.reshape(altoplaca, anchoplaca)  
            bin= Image.fromarray(bin)
            bin= bin.convert("L")

            if altoplaca>=36 and anchoplaca>=82:
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

                config= "--psm 1"
                texto= pytesseract.image_to_string(bin, config=config)

                if len(texto)>=7:
                    camaraTexto= texto
            
            break

    cv2.imshow("vehiculo",frame)  

    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
        break       

    



# Liberar el objeto de captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()




"""   # Salir del bucle al presionar 'q' o 'Q'
   cv2.namedWindow('Camara en vivo', cv2.WINDOW_NORMAL)    
"""
>>>>>>> 89231dab5e94e7902beb7cf2c1e79c16dc7732a0
