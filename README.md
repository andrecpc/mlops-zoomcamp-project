# mlops-zoomcamp-project
==============================

This repository contains the final project for the course [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp).

The ML tasks idea and the dataset are taken from [here](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset).

## Project Organization

([Cookiecutter DS template](https://github.com/drivendata/cookiecutter-data-science))

------------

    ├── LICENSE            <- License details.
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   └── raw            <- The original, immutable data dump.
    ├── Docker             <- Docker settings for minio, mlflow, pgsql, nginx
    ├── Screenshots        <- Different Images for Readme
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── mlruns             <- Meta-data of mlflows runnings
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks (EDA)
    └── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    └── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   ├── predict_sample.py
    │   │   └── train_model.py
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   |   └── visualize.py
    |   ├── app            <- Scripts to run API
    │       └── inference.py
    ├── venv               <- Virtual environment settings
    ├── .dvc               <- DVC settings
    ├── .github            <- Github settings.
    │   ├── workflows      <- CI/CD settings
    └── .dvcignore         <- DVC ignore settings.
    └── .gitignore         <- Git ignore settings
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
    └── docker-compose.yaml <- Docker settings
    └── dvc.lock           <- DVC meta-data
    └── dvc.yaml           <- DVC pipline settings 
    └── project_design.drawio.xml    <- Pipline structure in draw.io format
    └── poetry path.txt    <- Usefull CLI commands 
    └── poetry.lock        <- Poetry meta-data 
    └── pyproject.toml     <- Poetry settings 
    └── start.py           <- Simple pythons pipline 
--------

## Project Design

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/project_design.png)|
|----|

The requirements for the final project are [here](https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/07-project). 
Let's go!

----------------------------------------------------

## Project Description

**Classifier of vegetables.**

**Problem statement**

There is a lot of research on the importance of the correct placement of goods on store shelves (for example [link 1](https://www.researchgate.net/publication/215742904_Does_In-Store_Marketing_Work_Effects_of_the_Number_and_Position_of_Shelf_Facings_on_Brand_Attention_and_Evaluation_at_the_Point_of_Purchase),  [link 2](https://www.researchgate.net/publication/41623519_Brand_placement_and_consumer_choice_An_in-store_experiment)). But sometimes it is not enough to arrange the goods correctly, often it is necessary to return these goods to their places after the buyers touch them and rearrange them.
One of the particular similar tasks may be the restoration of the layout of vegetables in the relevant departments. As a solution to this problem, you can imagine a robot laying out vegetables, one of the skills of which should be the recognition of vegetables.
Therefore, the simplest classifier of vegetables is implemented in this project.

**Data description**

The dataset from Kaggle is used as [data](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset), which contains 15 classes of vegetables; 1400 examples per class.

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/1.png)|
|----|

The data has already been worked out and divided into blocks for training, validation and final control.

**Optimization methods**

Stochastic gradient descent with adaptive moment estimation (Adam). This method performs well in most machine learning tasks and provides the best convergence.

**Quality metrics**

Accuracy — the proportion of correct answers. With an equal number of images in classes, a metric that is excellent and understandable to a person.

**Description of MLops approaches**

* Version control system: git (github)
* Codestyle control tools: Pylint
* Template engine: Cookie cutter
* Workflow manager: DVC
* Tracking experiments: MLflow

**Description of the resulting service/product**

Workflow consists of 3 blocks: demonstration of examples of images of each class, model training and saving, class prediction for the image.

An additional 4 block is used to process user post requests to the API, which receive an image at the input, and give the name of the predicted class at the output.

The classifier is implemented using a sequential connection of convolutional, pooling and fully connected layers of the Keras library.

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/2.png)|
|----|

After 10 epochs of training, the Accuracy on the test dataset reaches about 95.47%.

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/3.png)|
|----|

**Technology stack**

* Language: Python 3.10.4
* Dependency Management: pip
* Managing virtual districts: poetry
* Versia management system: git (github)
* Workflow menu, control version: DVC, Minio
* Pattern: Soockiecutter
* Linter: Pylint
* Autoformer: black
* CLI: click, argparse
* Monitoring: MLflow, postgres, minio, nginx, docker
* ML stack: Keras
* Runtime: docker
* API: FastAPI

**Problems and disadvantages of the current workflow. Possible improvements.**

**Disadvantages**

* Training the model on the CPU takes about 15 minutes
* No separation into prod and dev environments
* No tests
* The simple CI/CD part only with Pylint code analyser

**Possible improvements**

* Increasing the number of classes
* Adding Tests
* Adding a model for vegetable segmentation

----------------------------------------------------

## How to run it

**1. Copy this repo**

```git clone https://github.com/andrecpc/mlops-zoomcamp-project.git```

**2. Check EDA notebook**

To understand the idea of the project.

[Notebook](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/notebooks/vegetable_image_classification_using_cnn.ipynb)

**3. Installing dependencies**

[Install Poetry](https://python-poetry.org/docs/) in the way that is convenient for you.

Install packages from the .toml-file using the command

```poetry install```

**4. Pipeline check**

Run 
```dvc dag```
to see the pipeline visualization.

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/4.png)|
|----|

The pipeline consists of 3 blocks: demonstration of examples of images of each class, training and saving the model, class prediction for one given image.

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/5.png)|
|----|

To start DVC DAG run the command

```dvc repro```

Example of visualization

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/6.PNG)|
|----|

Example of traning

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/7.PNG)|
|----|

Example of prediction generation

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/8.PNG)|
|----|

If desired, you can run the MLflow web shell, the trained model will appear in the menu.

```mlflow ui```

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/9.PNG)|
|----|

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/10.PNG)|
|----|

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/11.png)|
|----|

**5. Run Docker**

To run all containers, run the commands

```docker-compose up -d --build```

```docker build -f Docker/mlflow_image/Dockerfile -t mlflow_server .```

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/12.png)|
|----|

The pretrained model has already been loaded into the S3 bucket of Minio

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/13.png)|
|----|

**6. Check API**

You can check the operation of the model using the API and the Postman program.

|![](https://github.com/andrecpc/mlops-zoomcamp-project/blob/main/Screenshots/14.png)|
|----|

----------------------------------------

Well, here is the final of the project. MLOps Zoomcamp is an excellent course that motivated me to get acquainted with new services and expand my skills.

**Thanks to the authors of the course!**
