from ultralytics import YOLO


pathModel = 'best.pt' # Cambiar con path del modelo a reentrenar

# Inicializar modelo
model = YOLO(pathModel)
model.info()

model.info()


if __name__ == '__main__':
    
    results = model.train(data='H:\datasets\dataReTrain.yaml', epochs=50, imgsz=640)
    results = model.val()