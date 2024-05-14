import os
import shutil
from random import shuffle

def split_dataset(dataset_path, output_path, train_ratio=0.8):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    animal_folders = [f for f in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, f))]

    for products_folder in animal_folders:
        products_path = os.path.join(dataset_path, products_folder)

        photos = [f for f in os.listdir(products_path) if f.endswith(('.jpg', '.jpeg', '.png'))]


        shuffle(photos)

        num_train = int(len(photos) * train_ratio)
        train_photos = photos[:num_train]
        test_photos = photos[num_train:]

        train_path = os.path.join(output_path, 'train', products_folder)
        test_path = os.path.join(output_path, 'test', products_folder)

        os.makedirs(train_path, exist_ok=True)
        os.makedirs(test_path, exist_ok=True)

        for photo in train_photos:
            shutil.copy(os.path.join(products_path, photo), os.path.join(train_path, photo))

        for photo in test_photos:
            shutil.copy(os.path.join(products_path, photo), os.path.join(test_path, photo))

if __name__ == "__main__":
    dataset_path = "C:/Users/yeras/OneDrive/Рабочий стол/Diplom2/Dataset"
    output_path = "C:/Users/yeras/OneDrive/Рабочий стол/Diplom2/output"

    split_dataset(dataset_path, output_path)
