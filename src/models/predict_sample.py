# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import os, shutil
import click
import warnings
warnings.filterwarnings('ignore')


@click.command()
@click.argument("test_image_path", type=click.Path())
@click.argument("model_path", type=click.Path())
def generate_predictions(test_image_path: str, model_path: str):

    model = keras.models.load_model(model_path)
    class_map = {0: 'Bean', 1: 'Bitter_Gourd', 2: 'Bottle_Gourd', 3: 'Brinjal', 4: 'Broccoli',
                5: 'Cabbage', 6: 'Capsicum', 7: 'Carrot', 8: 'Cauliflower', 9: 'Cucumber', 10: 'Papaya',
                11: 'Potato', 12: 'Pumpkin', 13: 'Radish', 14: 'Tomato'}
    
    # 1. Load and preprocess the image
    # test_img = image.load_img(test_image_path, target_size=(150, 150))
    # test_img_arr = image.img_to_array(test_img)/255.0
    test_img = keras.utils.load_img(test_image_path, target_size=(150, 150))
    test_img_arr = keras.utils.img_to_array(test_img)/255.0
    test_img_input = test_img_arr.reshape((1, test_img_arr.shape[0], test_img_arr.shape[1], test_img_arr.shape[2]))

    # 2. Make Predictions
    predicted_label = np.argmax(model.predict(test_img_input))
    predicted_vegetable = class_map[predicted_label]
    plt.figure(figsize=(4, 4))
    plt.imshow(test_img_arr)
    plt.title("Predicted Label: {}".format(predicted_vegetable))
    plt.grid()
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    generate_predictions()
