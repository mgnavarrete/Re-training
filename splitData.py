import os
import shutil
from sklearn.model_selection import train_test_split

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
    val_images, train_images, val_labels, train_labels = train_test_split(train_images, train_labels, train_size=(train_size / (train_size + val_size)), test_size=(val_size / (train_size + val_size)), random_state=42)
    
    

    # Moving files to new directories   
    move_files(train_images, images_dir, os.path.join(data_path, 're-train', 'images'))
    move_files(val_images, images_dir, os.path.join(data_path, 're-val', 'images'))
    move_files(test_images, images_dir, os.path.join(data_path, 're-test', 'images'))
    move_files(train_labels, labels_dir, os.path.join(data_path, 're-train', 'labels'))
    move_files(val_labels, labels_dir, os.path.join(data_path, 're-val', 'labels'))
    move_files(test_labels, labels_dir, os.path.join(data_path, 're-test', 'labels'))



base_dir= "H:/datasets/allData"
data_path = "H:/datasets"
print("Dividiendo los datos...")
split_data(base_dir, data_path)
print("Datos divididos correctamente.")