mlops-repo
==============================

Final project by MLOps course (ODS, Yandex.Q)

ML task and a part of code are taken from here https://www.kaggle.com/code/chitwanmanchanda/vegetable-image-classification-using-cnn/notebook

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   └── raw            <- The original, immutable data dump.
    ├── Docker             <- Docker settings for minio, mlflow, pgsql, nginx
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── mlruns             <- Meta-data of mlflows runnings
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks (EDA)
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   ├── predict_sample.py
    │   │   └── train_model.py
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   |   └── visualize.py
    |   ├── app       <- Scripts to run API
    │       └── inference.py
    ├── venv               <- Virtual environment settings
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
    └── docker-compose.yaml <- Docker settings
    └── dvc.lock           <- DVC meta-data
    └── dvc.yaml           <- DVC pipline settings 
    └── mlops-ods.drawio.xml    <- Pipline structure in draw.io format
    └── poetry path.txt    <- Usefull CLI commands 
    └── poetry.lock        <- Poetry meta-data 
    └── pyproject.toml     <- Poetry settings 
    └── start.py           <- Simple pythons pipline 
--------

https://docs.google.com/document/d/18Qu_3Mzwz_aZmB7iZhsP0kTlRKrKj56j/edit
https://docs.google.com/presentation/d/1yjxuByyYBfDwjU-Y_zRAQU0FaAsfGZHT6S0oQ_Ka9eE/edit#slide=id.p



# data-engineering-zoomcamp-project

This repository contains the final project for the course [data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp).

**Project Design**
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/data-engineering-zoomcamp-project.drawio.png)|
|----|

The requirements for the final project are [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_7_project). 
Let's go!

----------------------------------------------------

### Step 0. Environment Settings

To work with the project, I used the Google cloud virtual machine, which was configured to do homework on the course. This [video](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&ab_channel=DataTalksClub%E2%AC%9B ) contains instructions how to set it up.

### Step 1. Choosing a dataset

To select a dataset, I could use [these materials](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_7_project/datasets.md)
As a result, the **Road Safety Data** dataset was selected from the site [data.gov.uk](https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data).
This data is excellent for applying the skills acquired during the course. There are a lot of files here, they are large. These files are difficult to understand individually, but by collecting them all into a single database, it will be possible to build understandable dashboards for analysis. For work, we will use data about accidents from 2017 to 2020 (Road Safety Data - Accidents).
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/1.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/2.png)|
|----|

> _There is a [data sample](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/1_Data/dft-road-casualty-statistics-accident-small.csv) in the current repository._


### Step 2. Selecting and preparing a data lake

Google Cloud Platform is used to store raw data, Terraform is used to configure the infrastructure.  
The deployment process is described [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp).  

Creating bucket and dataset.  
To do this, you need to run [these commands](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp/terraform)
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/3.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/4.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/5.png)|
|----|

Everything was done successfully, we created a package and a dataset.

> _Terraform settings are available in the [repository](https://github.com/andrecpc/data-engineering-zoomcamp-project/tree/main/2_Terraform)._

### Step 3. Data ingestion

Airflow is used to transfer data from the government website to the data lake.  
Launch the docker container with airflow, open the web interface, launch the dag.  
Instructions for deploying the airflow container [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_data_ingestion/airflow).
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/6.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/7.png)|
|----|

The data is successfully downloaded and uploaded to the data lake from 2017 to 2020. Data for 2021 and 2022 are not available, so there are warnings in the last steps.

Checking the data lake.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/8.png)|
|----|

Whoosh! The data was moved to the data lake.

> _The files for launching the airflow container are available in this [repository](https://github.com/andrecpc/data-engineering-zoomcamp-project/tree/main/3_Airflow)._

### Step 4. Data Transformation and creation of database

To transform the data, we will use the Data Fusion tool, which is a part of Google Cloud. To study, we will use [this guide](https://medium.com/google-cloud/from-zero-to-hero-end-to-end-automated-analytics-workload-using-cloud-functions-data-fusion-28670e5e7c74)  
In addition to the fact that this tool is included in the cloud, it is also convenient that it has a graphical interface.

#### 4.1 First, create an instance following the instructions above
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/9.png)|
|----|

In this instance, a pipeline will be created to transform data from the lake and send it to BigQuery. But first you need to make a table template.

#### 4.2 Creating a table template with a data schema.
This step does not require automation, so we'll just do it with our hands and load the headers into an empty table.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/10.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/11.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/12.png)|
|----|

So far we are not using partitioning, this step will be taken further.

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/13.png)|
|----|

We got an empty table. All formats of values are now string, this will be corrected further automatically.

#### 4.3 Creating a pipeline

Adding the GCS data source.

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/14.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/15.png)|
|----|

In the settings, I specify the source of the data lake and the format of the output data.  
I add a Wrangler data transformation tool and connect it to the output of the previous block.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/16.png)|
|----|

In the block settings, select sending errors and enter the editing mode.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/17.png)|
|----|

We select any file from the data uploaded to the lake as a standard file.  
And now we are doing different transformations with columns to change formats and data. A good overview of the transformation is in the medium's article, which I attached at the beginning of the guide.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/18.png)|
|----|

Here are all the transformations.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/19.png)|
|----|

Now you can see the data schema at the wrangler output.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/20.png)|
|----|

From the Sink section, we add two blocks to the pipeline for writing data to the storage and bigquery.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/21.png)|
|----|

Also, between the wrangler and storage blocks, we insert the error handler from the error section.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/22.png)|
|----|

Settings of the bigquery block. Specify the names of the dataset and the tables that were created earlier.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/23.png)|
|----|

Setting up schema updates and inserting new data.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/24.png)|
|----|

We add partitioning settings and specify by which column to do it.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/25.png)|
|----|

We check what data we get at the output, change the types in the output data schema to the necessary types.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/26.png)|
|----|

Error Collector Settings.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/27.png)|
|----|

Settings of the recording block in the storage. Just specify in which bucket to record and in what format.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/28.png)|
|----|

The result is such a pipeline (all blocks must be connected, as in the screenshot).
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/29.png)|
|----|

Now you can turn on the preview mod and start the pipeline, and then look at what data we get in any of the blocks.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/30.png)|
|----|

Exit the preview mod and launch the deployment.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/31.png)|
|----|

If you start the pipeline right away, you will most likely get errors. This is due to the fact that the free Google cloud tariff limits the available resources, and the resource values in the data fusion pipeline will be very high, so we need to change some settings (I spent a lot of time on these findings).  
Go to Configure -> Customize and change the following values:  
Master Disk Size (GB) 1000 -> 31, Worker Memory (GB) 8 -> 7
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/32.png)|
|----|

Now you can start the pipeline.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/33.png)|
|----|

Everything works!  
Let's check now that the data has been transferred to the bigquery.

First, the data schema has changed.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/34.png)|
|----|

There really is data in the table.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/35.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/36.png)|
|----|

Happiness, everything works!

I'm exporting a pipeline to send to github.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/37.png)|
|----|

If desired, you can configure the pipeline execution schedule.  
But this is not necessary in the current project.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/38.png)|
|----|

> _The file of pipeline settings is available in [the folder](https://github.com/andrecpc/data-engineering-zoomcamp-project/tree/main/4_Data_Fusion) of this repository._

### Step 5. Create a dashboard in the Data Studio

Connecting the BigQuery table.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/39.png)|
|----|

|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/40.png)|
|----|

Creating the first sheet with diagrams based on this table.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/41.png)|
|----|

Here I do not describe the process in detail, since the data studio has a clear, simple interface. And also this tool was studied in the course, for example [here](https://www.youtube.com/watch?v=39nLTs74A3E&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=43&ab_channel=DataTalksClub%E2%AC%9B).

On the second sheet I create an interactive map.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/42.png)|
|----|

To do this, I created a new parameter of geographical coordinates based on Latitude and Longitude.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/43.png)|
|----|

And assigned the coordinates data type to this parameter.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/44.png)|
|----|

Some values in the uploaded data are encoded using indexes, for example local_authority_district.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/45.png)|
|----|

Replace these indexes with normal values.  
On the same page where we downloaded the data, there is a document with index values called Road Safety Open Dataset Data Guide ([download link](https://data.dft.gov.uk/road-accidents-safety-data/Road-Safety-Open-Dataset-Data-Guide.xlsx)).

Based on this document, I created [a reference book](https://docs.google.com/spreadsheets/d/1r0lZ8-1uY4W3mmRTIATjBvracqiaAQf5HLilUtrQ6jA/edit?usp=sharing) and added it as a data source in the data studio.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/46.png)|
|----|

Now I can combine the data from both sources by the local_authority_district field and build a table on the third sheet with the decrypted indexes.
|![](https://github.com/andrecpc/data-engineering-zoomcamp-project/blob/main/Screenshots/47.png)|
|----|

That's it!

**There is a dashboard of the data studio available at [the link](https://datastudio.google.com/reporting/0a6bd8f6-6f66-4945-a78e-437923ae2ffe)**

It is interesting to see how the number of incidents decreases when the coronavirus pandemic begins in the world in the spring of 2020.

> _Also, the downloaded report from the data studio is available in [the folder](https://github.com/andrecpc/data-engineering-zoomcamp-project/tree/main/5_Data_Studio) of this repository._
> 
----------------------------------------

Well, here is the final of the project. Data Engineering Zoomcamp is an excellent course that motivated me to get acquainted with new services and expand my skills.

**Thanks to the authors of the course!**








