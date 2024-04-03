from ultralytics import YOLO


nameModel = 'best.pt' # Cambiar con path del modelo a reentrenar
epochs = 50


# Inicializar modelo

model = YOLO("H:/Re-training/oldModels/yolo8/0"+ nameModel)
model.info()

model.info()


if __name__ == '__main__':
    
    results = model.train(data='H:\datasets\dataReTrain.yaml', epochs=epochs, imgsz=640)
    results = model.val()