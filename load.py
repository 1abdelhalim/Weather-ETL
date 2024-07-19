import os
import pandas as pd
from sqlalchemy import create_engine

# Fetch database connection details from environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

def load_to_postgresql(df, table_name):
    # Create an engine instance
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    try:
        # Load data into PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print("Data loaded successfully into PostgreSQL")
    except Exception as e:
        print(f"Error loading data into PostgreSQL: {e}")
    finally:
        # Dispose of the engine
        engine.dispose()