import matplotlib.pyplot as plt
from tensorflow import keras
from keras.preprocessing import image
import click
import os


@click.command()
@click.argument("input_path", type=click.Path(exists=True), default='data/raw/VegetableImages/train')
def visualize(input_path: str):

    image_categories = os.listdir(input_path)
    
    # Create a figure
    plt.figure(figsize=(12, 12))
    for i, cat in enumerate(image_categories):
        
        # Load images for the ith category
        image_path = input_path + '/' + cat
        images_in_folder = os.listdir(image_path)
        first_image_of_folder = images_in_folder[0]
        first_image_path = image_path + '/' + first_image_of_folder
        # img = image.load_img(first_image_path)
        # img_arr = image.img_to_array(img)/255.0
        img = keras.utils.load_img(first_image_path)
        img_arr = keras.utils.img_to_array(img)/255.0

        plt.subplot(4, 4, i+1)
        plt.imshow(img_arr)
        plt.title(cat)
        plt.axis('off')
        
    plt.show()


if __name__ == "__main__":
    visualize()
