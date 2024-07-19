# Weather ETL Project

## Overview

The Weather ETL (Extract, Transform, Load) project collects weather data for Cairo, Egypt from OpenWeather API,
performs basic transformations, and loads the data into a PostgreSQL database.
The ETL process is automated using Apache Airflow. This project demonstrates a complete ETL pipeline from data extraction through transformation to loading, along with automation and management using Airflow.

![etl](https://github.com/user-attachments/assets/761ff3d8-fe9e-4a23-880f-7b914ffb21cb)




## Features

- **Data Extraction:** Fetches 3-day weather forecast data for Cairo from OpenWeather API.
- **Data Transformation:** Converts temperature from Kelvin to Celsius, extracts date and hour from timestamp.
- **Data Loading:** Loads the transformed data into a PostgreSQL database.
- **Automation:** Uses Apache Airflow to schedule and manage the ETL process.

## Installation

### Prerequisites

1. **Python 3.7+** - Ensure Python is installed.
2. **PostgreSQL** - Install PostgreSQL and set up a database.
3. **AirFlow** - Install AirFlow and Initialize it with the default configurations.



### Setup

1. **Install Dependencies**

   ```bash
   git clone https://github.com/1abdelhalim/Weather-ETL.git
   cd Weather-ETL

2. **Clone the Repository**

   ```bash
   pip install -r requirements.txt

3. **Initialize Airflow**

   ```bash
    airflow db init
    airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

4. **Start Airflow**

   ```bash
   airflow webserver --port 8080
   airflow scheduler


### Usage 
1. **Run ETL Manually**

   ```bash
    python main.py

2. **Automated ETL via Airflow**

   ```bash
   python main.py
The ETL process is scheduled to run daily. You can check the status and manage the DAG through the Airflow web UI at **http://localhost:8080**.


