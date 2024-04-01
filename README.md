# Guía para el Reentrenamiento de Modelos YOLO

Esta guía paso a paso te ayudará a reentrenar modelos YOLOv5 y YOLOv8 utilizando tus propios datos. Asegúrate de seguir cada paso cuidadosamente para asegurar un reentrenamiento exitoso.

## Preparación de Datos

1. **Organización de Imágenes y Etiquetas:**
   - Coloca todas las imágenes que deseas utilizar para el reentrenamiento en la carpeta `H:\datasets\allData\images`.
   - Coloca todas las etiquetas correspondientes en la carpeta `H:\datasets\allData\labels`.

2. **División de Datos:**
   - Ejecuta el script `splitData.py` para dividir tus datos en conjuntos de entrenamiento, validación y prueba. Este script distribuirá automáticamente las imágenes y sus etiquetas correspondientes en subcarpetas adecuadas.

### Pasos para Ejecutar `splitData.py`

a. Abre una terminal o CMD en la ubicación donde hayas guardado el script `splitData.py`.

b. Ejecuta el script con Python:

  ```
  python splitData.py
  ```

c. El script dividirá los datos en los conjuntos de entrenamiento, validación y prueba, y los moverá a las carpetas adecuadas dentro de `H:\datasets`.

## Reentrenamiento de Modelos YOLO

### YOLOv5

1. **Preparación:**
- Asegúrate de tener el repositorio de YOLOv5 clonado en tu sistema. Si aún no lo has hecho, puedes clonarlo desde el [repositorio oficial de YOLOv5](https://github.com/ultralytics/yolov5).
- Actualiza el script `yolo5Retrain.py` con las rutas correctas según tu configuración:
  - `yolov5_repo_path`: Ruta al clon del repositorio YOLOv5.
  - `data_yaml_path`: Ruta al archivo `.yaml` que especifica las rutas de tus conjuntos de datos. Asegúrate de que este archivo esté correctamente configurado con las rutas a las carpetas de imágenes y etiquetas divididas.

2. **Reentrenamiento:**
- Desde una terminal, navega hasta la ubicación de tu script `yolo5Retrain.py`.
- Ejecuta el script con Python:
  ```
  python yolo5Retrain.py
  ```
- El script realizará el reentrenamiento del modelo YOLOv5 con tus datos.

### YOLOv8

1. **Preparación:**
- Igual que para YOLOv5, asegúrate de que el archivo `dataReTrain.yaml` esté correctamente configurado con las rutas a tus conjuntos de datos.
- Actualiza el script `yolo8Retrain.py` si es necesario, especialmente la variable `pathModel` para apuntar al modelo que deseas reentrenar.

2. **Reentrenamiento:**
- Navega hasta la ubicación de tu script `yolo8Retrain.py` en una terminal.
- Ejecuta el script con Python:
  ```
  python yolo8Retrain.py
  ```
- El script comenzará el proceso de reentrenamiento para YOLOv8 con tus datos.

## Notas Finales

- Asegúrate de tener instaladas todas las dependencias requeridas para YOLOv5 y YOLOv8, incluidas las versiones específicas de PyTorch.
- Monitorea la salida en la terminal para detectar cualquier error y ajusta tu configuración según sea necesario.
