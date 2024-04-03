import os
import shutil
from tkinter import filedialog
from sklearn.model_selection import train_test_split
from tqdm import tqdm

def select_directories():
    list_folders = []  
    path_root = filedialog.askdirectory(title='Seleccione el directorio raíz')
    while path_root:
        list_folders.append(path_root)
        path_root = filedialog.askdirectory(title='Seleccione otro directorio o cancele para continuar')
    if not list_folders:
        raise Exception("No se seleccionó ningún directorio")
    return list_folders


# Funcion para mover los archivos
def move_files(files, source_dir, destination_dir):
    for f in files:
        shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir, f))


def split_data(base_dir, data_path, train_size=0.7, val_size=0.15, test_size=0.15):

    # Path de labels y images
    images_dir = os.path.join(base_dir, 'images')
    labels_dir = os.path.join(base_dir, 'labels')
    
    # Creando lista ocn nombres de archivos
    images = os.listdir(images_dir)
    labels = os.listdir(labels_dir)

    # Splitting data
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, train_size=train_size + val_size, test_size=test_size, random_state=42)
    train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, train_size=(train_size / (train_size + val_size)), test_size=(val_size / (train_size + val_size)), random_state=42)
    
    

    # Moving files to new directories   
    move_files(train_images, images_dir, os.path.join(data_path, 're-train', 'images'))
    move_files(val_images, images_dir, os.path.join(data_path, 're-val', 'images'))
    move_files(test_images, images_dir, os.path.join(data_path, 're-test', 'images'))
    move_files(train_labels, labels_dir, os.path.join(data_path, 're-train', 'labels'))
    move_files(val_labels, labels_dir, os.path.join(data_path, 're-val', 'labels'))
    move_files(test_labels, labels_dir, os.path.join(data_path, 're-test', 'labels'))

labelsPath = 'H:/datasets/allData/labels'

# Guarda en lista los archivos en labelsPath
labels = os.listdir(labelsPath)
labelsClean = []
for label in labels:
    labelsClean.append(label.split(".")[0])

print("Seleccione carpeta de imagenes...")

list_folders = select_directories()
for path_root in list_folders:

    for folder_path in os.listdir(path_root):
        if folder_path.endswith('PP'):
            # Recorrer todos los archivos en la carpeta
            path = os.path.join(path_root, folder_path)
            
            for filename in tqdm(os.listdir(os.path.join(path,"cvat")),desc="Contando Imágenes"):
                # Verifica si el nombre de archivo (sin la extensión) está en labelsClean
                label_name = filename.split(".")[0]
                if label_name in labelsClean:
                    # Agrega el prefijo "F_" tanto al label como al nombre de archivo
                    new_label_name = "F_" + label_name
                    new_filename = "F_" + filename
                    
                    # Construir la ruta completa al archivo original y la ruta de destino con el nuevo nombre
                    file_path = os.path.join(path, "cvat", filename)
                    destination_path = os.path.join('images', new_filename)
                    
                    # Copia el archivo con el nuevo nombre al directorio 'images'
                    shutil.copy(file_path, destination_path)
                    # Cambiar nombre a label_name
                    os.rename(os.path.join(labelsPath, label_name + ".txt"), os.path.join(labelsPath, new_label_name + ".txt"))

                    


base_dir= "H:/datasets/allData"
data_path = "H:/datasets"
# Si las carpetas re-trian, re-val y re-test no existen, las crea con las sub carpetas images y labels
if not os.path.exists(os.path.join(data_path, 're-train', 'images')):
    os.makedirs(os.path.join(data_path, 're-train', 'images'))
    os.makedirs(os.path.join(data_path, 're-train', 'labels'))
    os.makedirs(os.path.join(data_path, 're-val', 'images'))
    os.makedirs(os.path.join(data_path, 're-val', 'labels'))
    os.makedirs(os.path.join(data_path, 're-test', 'images'))
    os.makedirs(os.path.join(data_path, 're-test', 'labels'))

print("Dividiendo los datos...")
split_data(base_dir, data_path)
print("Datos divididos correctamente.")