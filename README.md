# BigDataNights

Repository to store case studies for **Big Data Nights** presentations.

## Content
- [Big Data Night #1: Synthetic Data in Action](night_1/README.md)
- [Big Data Night #2: To be announced](#)

## Big Data Nights description

#### [Big Data Night #1: Synthetic Data in Action](night_1/README.md)
Imagine solving real-world business problems with data you create yourself! In this hands-on proof of concept, you'll learn how to generate synthetic data using Python, simulating real-life scenarios to meet specific business needs. From there, you’ll dive into dbt models, transforming that raw data into meaningful insights to answer key business questions. Finally, with pgAdmin 4, you’ll get to explore and analyze the transformed data, seeing firsthand how it can drive decision-making.
This session is designed to give you practical experience from start to finish — creating, transforming, and analyzing data in a fully local environment. Whether you're new to synthetic data or looking to refine your skills, you'll leave with the tools to build scalable pipelines and apply them to real-world situations.

## Prepare work environment
If you want to follow on your own the presentation and implement the project on your local machine follow these intructions.

**Note:** All commands used in this repository are for Windows.\
In repository main directory `BigDataNights` create a virtual environment that will be used for this project.
```
python -m venv venv
.\venv\Scripts\activate
```

After activating the virtual environment, you have a clean environment that don't have libraries installed. You can check this using command below.
```
pip list
```
![Image 1.1](./media/image_1.1.PNG)

As the environment is clean, here are two main options to get all necessary dependecies. Install necessary libraries one by one and store them in `requirement.txt` file.
```
python.exe -m pip install --upgrade pip
pip install psycopg2
pip install faker
pip freeze > requirements.txt
```
Also, it can be installed from a existing `requirements.txt` file using command below.
```
pip install -r requirements.txt
```
The result of this operation is presented in the image below.
![Image 1.2](./media/image_1.2.PNG)
