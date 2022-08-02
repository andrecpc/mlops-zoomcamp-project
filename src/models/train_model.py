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
import mlflow
import mlflow.keras
# from mlflow.models.signature import infer_signature
from dotenv import load_dotenv
warnings.filterwarnings('ignore')

load_dotenv()
remote_server_uri = os.getenv("MLFLOW_TRACKING_URI")
mlflow.set_tracking_uri(remote_server_uri)
mlflow.set_experiment("main-train")

mlflow.keras.autolog()

@click.command()
@click.argument("train_path", type=click.Path())
@click.argument("validation_path", type=click.Path())
@click.argument("test_path", type=click.Path())
@click.argument("save_model_path", type=click.Path())
def train(train_path: str, validation_path: str, test_path: str, save_model_path: str):

    with mlflow.start_run():

        mlflow.get_artifact_uri()

        image_categories = os.listdir(train_path)

        # Creating Image Data Generator for train, validation and test set

        # 1. Train Set
        train_gen = ImageDataGenerator(rescale = 1.0/255.0) # Normalize the data
        train_image_generator = train_gen.flow_from_directory(
                                                    train_path,
                                                    target_size=(150, 150),
                                                    batch_size=32, # 32
                                                    class_mode='categorical')

        # 2. Validation Set
        val_gen = ImageDataGenerator(rescale = 1.0/255.0) # Normalize the data
        val_image_generator = train_gen.flow_from_directory(
                                                    validation_path,
                                                    target_size=(150, 150),
                                                    batch_size=32,
                                                    class_mode='categorical')

        # 3. Test Set
        test_gen = ImageDataGenerator(rescale = 1.0/255.0) # Normalize the data
        test_image_generator = train_gen.flow_from_directory(
                                                    test_path,
                                                    target_size=(150, 150),
                                                    batch_size=32,
                                                    class_mode='categorical')

        class_map = dict([(v, k) for k, v in train_image_generator.class_indices.items()])
        print(class_map)

        # Build a custom sequential CNN model

        model = Sequential() # model object

        # Add Layers
        model.add(Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu', input_shape=[150, 150, 3]))
        model.add(MaxPooling2D(2, ))
        model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding='same', activation='relu'))
        model.add(MaxPooling2D(2))

        # Flatten the feature map
        model.add(Flatten())

        # Add the fully connected layers
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.25))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(15, activation='softmax'))

        # print the model summary
        model.summary()

        params = {
            'epochs' : 10,
            'verbose' : 1,
            'steps_per_epoch' : 15000//32, # 15000//32
            'validation_steps' : 3000//32
        }

        mlflow.log_params(params)

        # Compile and fit the model
        early_stopping = keras.callbacks.EarlyStopping(patience=5) # Set up callbacks
        model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics='accuracy')
        hist = model.fit(train_image_generator, 
                        epochs=params['epochs'], 
                        verbose=params['verbose'], 
                        validation_data=val_image_generator, 
                        steps_per_epoch = params['steps_per_epoch'], 
                        validation_steps = params['validation_steps'], 
                        callbacks=early_stopping)
                        
        # Predict the accuracy for the test set
        result_metrics = model.evaluate(test_image_generator)
        print(result_metrics)

        mlflow.log_metrics({'loss': result_metrics[0], 'accuracy': result_metrics[1]})
        # signature = infer_signature(test_image_generator., model.predict(test_image_generator))
        # mlflow.log_artifact(save_model_path)
        mlflow.keras.log_model(model, "models")  # https://mlflow.org/docs/latest/models.html

        # model.save(save_model_path)


if __name__ == "__main__":
    train()
