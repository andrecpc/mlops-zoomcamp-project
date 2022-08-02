# https://www.tensorflow.org/install/pip#virtual-environment-install

from src.visualization.visualize import visualize
from src.models.train_model import train
from src.models.predict_sample import generate_predictions

TRAIN_PATH = "data/raw/VegetableImages/train"
VALIDATION_PATH = "data/raw/VegetableImages/validation"
TEST_PATH = "data/raw/VegetableImages/test"
SAVE_MODEL_PATH = "models/model"
SAMPLE_IMAGE_PATH = "data/external/3.jpg"

if __name__ == "__main__":
    visualize(TRAIN_PATH)
    train(TRAIN_PATH, VALIDATION_PATH, TEST_PATH, SAVE_MODEL_PATH)
    generate_predictions(SAMPLE_IMAGE_PATH, SAVE_MODEL_PATH)
