# Guía para el Reentrenamiento de Modelos

Esta guía paso a paso te ayudará a re-entrenar modelos YOLOv5 y YOLOv8 utilizando tus propios datos. Asegúrate de seguir cada paso cuidadosamente para asegurar un reentrenamiento exitoso.

## **PASO 1:** Preparación Inicial

### Activación del Entorno Virtual

Antes de empezar con la preparación de datos y el re-entrenamiento, es importante activar tu entorno virtual donde están todas las dependencias necesarias instaladas.

Para activar el entorno virtual, utiliza el siguiente comando dependiendo de tu sistema operativo:

- **Windows:**  `.\venv\Scripts\activate`

Este comando deber ejecutarse en la cmd parado en la carpeta `Re-training`. Una vez activado el entorno virtual, puedes proceder con los siguientes pasos.

## **PASO 2:** Preparación de Datos

1. **Preparar carpetas de entrenamiento:** 
  - Elimina las carpetas `re-val`, `re-train` y `re-test` o asegurate de que estas tengan sus subcarpetas `images` y `labels` vacias, para así evitar overfiting al momento de re-entrenar.

2. **Organización de etiquetas:**
 - Coloca todas las labels de la planta que deseas usar para el re-entreno en la carpeta `H:\datasets\allData\labels`.
 - Solo copia las labels, en el siguiente paso el programa copiara las imágenes correspondientes a estas labels.


2. **Copia de imágenes y división de datos:**
 - Ejecuta el script `splitData.py`, este programa copiará las imágenes correspondientes a las labels y separará los datos en train, val y test. Este script distribuirá automáticamente las imágenes y sus etiquetas correspondientes en subcarpetas adecuadas con una distibución de:

 ```
 train: 0.7
 val: 0.15
 test: 0.15
 ```
- Si quieres cambiar los porcentajes lo puedes hacer en la línea 24, preocupate que la suma de estos sea igual a 1
- La línea que habría que cambiar es la siguiente:

```python
def split_data(base_dir, data_path, train_size=0.7, val_size=0.15, test_size=0.15):
```
- 
### Pasos para Ejecutar `splitData.py`

a. Abre una terminal o CMD en la ubicación donde está guardado el script `splitData.py` (carpeta `Re-training`).

b. Asegurate de activar el entorno virtual, ve primer paso 1.

c. Ejecuta el script con Python:

```
python splitData.py
```
d. Selecciona la carpeta raíz en donde estan todas los datos de la planta. Por ejemplo si guarde labels de Campos del Sol, seleccionar carpeta `CDS` donde esta debería tener las carpetas que ya se procesaron, así se deberia ver la carpeta:

```
CDS
  |
  --C12
  |
  --C12PP
  |
  ...
  |
  --C23
  |
  --C23PP
```

**`CDS` debe ser selecionada.**

e. El script copiará las imágenes correspondientes a los labels copiados en `H:\datasets\allData\labels`, esos datos de dividiran en los conjuntos de entrenamiento, validación y prueba, dentro de las carpetas `H:\datasets\re-val`, `H:\datasets\re-train` y `H:\datasets\re-test`, respectivamente.

## **PASO 3:** Reentrenamiento de Modelos YOLO

### YOLOv5

1. **Preparación:**

- Actualiza el script `yolo5Retrain.py` con las rutas correctas según tu configuración:

  - `pathModel`: En esta variable deberás actualizar con el path absoluto del modelo que se quiere re-entrenar
  - También puedes modificar el número de épocas en la línea 17.

2. **Reentrenamiento:**
- Abre una terminal o CMD en la ubicación donde está guardado el script `yolo5Retrain.py` (carpeta `Re-training`)

- Asegurate de activar el entorno virtual, ve primer paso 1.

- Ejecuta el script con Python:

  ```
  python yolo5Retrain.py
  ```
- El script realizará el re-entrenamiento del modelo YOLOv5 con tus datos.



### YOLOv8

1. **Preparación:**

- Actualiza el script `yolo8Retrain.py` con las rutas correctas según tu configuración:

  - `pathModel`: En esta variable deberas actualizar con el path de modelo que se quiere reentrnar

2. **Reentrenamiento:**
- Navega hasta la ubicación de tu script `yolo8Retrain.py` en una terminal.
- Ejecuta el script con Python:
  ```
  python yolo8Retrain.py
  ```
- El script comenzará el proceso de reentrenamiento para YOLOv8 con tus datos.

## Notas Finales
- Asegurate siempre de estar en el entorno virtual para correr los programas ya que acá estan las dependencias instaladas.
- Monitorea la salida en la terminal para detectar cualquier error y ajusta tu configuración según sea necesario.



