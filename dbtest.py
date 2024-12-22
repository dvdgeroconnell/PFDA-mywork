import platform
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
import datetime as dt

import sqlite3
import sqlalchemy
from sqlalchemy import create_engine

print("Key Package Versions")
print("--------------------")
print("Python:\t\t", platform.python_version(), "\tA programming language for system integration and data manipulation")
print("NumPy:\t\t", np.__version__, "\tAn open source project for numerical computing with Python")
print("Matplotlib:\t", mpl.__version__, "\t\tA library for static, animated and interactive visualizations in Python")
print("Pandas:\t\t", pd.__version__, "\t\tA library for data manipulation and analysis with Python")
print("Seaborn:\t", sns.__version__, "\tA Python data visualization library based on matplotlib")
#print("SQLite3:\t", sqlite3.__version__, "\tA Python data visualization library based on matplotlib")
print("SqlAlchemy:\t", sqlalchemy.__version__, "\tA Python data visualization library based on matplotlib")



import pandas as pd
from sqlalchemy import create_engine, Column, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database and table
DATABASE_NAME = "wind.sqlite3"
Base = declarative_base()

def create_database():
    class Weather(Base):
        __tablename__ = 'weather'
        id = Column(Integer, primary_key=True, autoincrement=True)
        date = Column(DateTime, nullable=False)
        windspeed1 = Column(Float, nullable=True)
        windspeed2 = Column(Float, nullable=True)
        windspeed3 = Column(Float, nullable=True)
        windspeed4 = Column(Float, nullable=True)
        windspeed5 = Column(Float, nullable=True)
        windspeed6 = Column(Float, nullable=True)
        windspeed7 = Column(Float, nullable=True)
        windspeed8 = Column(Float, nullable=True)

    return Weather

# Create the SQLite database and engine
engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Populate the table with a DataFrame
def populate_table(df):
    Weather = create_database()
    # Convert the DataFrame into dictionary format for bulk insert
    data_to_insert = df.to_dict(orient='records')
    session.bulk_insert_mappings(Weather, data_to_insert)
    session.commit()

# Create a sample DataFrame for demonstration
# Replace this with your own data (up to 6,000 rows)
data = {
    "date": pd.date_range(start='2024-01-01', periods=6000, freq='H'),
    "windspeed1": [1.0] * 6000,
    "windspeed2": [2.0] * 6000,
    "windspeed3": [3.0] * 6000,
    "windspeed4": [4.0] * 6000,
    "windspeed5": [5.0] * 6000,
    "windspeed6": [6.0] * 6000,
    "windspeed7": [7.0] * 6000,
    "windspeed8": [8.0] * 6000,
}
wind = pd.DataFrame(data)

# Populate the database
populate_table(wind)

print(f"Database '{DATABASE_NAME}' created and populated successfully.")




# Alternative version just using sqlimport

import pandas as pd
import sqlalchemy

# Define the database and table
DATABASE_NAME = "wind.sqlite3"
Base = sqlalchemy.orm.declarative_base()

# Define the Weather table
class Weather(Base):
    __tablename__ = 'weather'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    windspeed1 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed2 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed3 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed4 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed5 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed6 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed7 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    windspeed8 = sqlalchemy.Column(sqlalchemy.Float, nullable=True)

# Create the SQLite database and engine
engine = sqlalchemy.create_engine(f'sqlite:///{DATABASE_NAME}')
Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# Populate the table with a DataFrame
def populate_table(df):
    # Convert the DataFrame into dictionary format for bulk insert
    data_to_insert = df.to_dict(orient='records')
    session.bulk_insert_mappings(Weather, data_to_insert)
    session.commit()

# Create a sample DataFrame for demonstration
# Replace this with your own data (up to 6,000 rows)
data = {
    "date": pd.date_range(start='2024-01-01', periods=6000, freq='H'),
    "windspeed1": [1.0] * 6000,
    "windspeed2": [2.0] * 6000,
    "windspeed3": [3.0] * 6000,
    "windspeed4": [4.0] * 6000,
    "windspeed5": [5.0] * 6000,
    "windspeed6": [6.0] * 6000,
    "windspeed7": [7.0] * 6000,
    "windspeed8": [8.0] * 6000,
}
wind = pd.DataFrame(data)

# Populate the database
populate_table(wind)

print(f"Database '{DATABASE_NAME}' created and populated successfully.")

# Read the data back into a DataFrame
retrieved_data = read_table_to_dataframe()
print(retrieved_data.head())

print(f"Database '{DATABASE_NAME}' created, populated, and read successfully.")



'''
Explanation:
Database and Table Definition:

The Weather class defines the weather table schema with id (primary key) and other fields.
Base is used to map Python classes to database tables.
SQLite Database:

The database is created using SQLAlchemy with SQLite as the backend.
Data Population:

A DataFrame wind is created with 6,000 rows and columns matching the weather table.
Data is inserted using bulk_insert_mappings for performance.
Flexibility:

Replace the sample DataFrame creation code with your own data-loading mechanism.


Explanation 2 (inport sqlalchemy):
Database and Table Definition:

The Weather class defines the weather table schema with id (primary key) and other fields.
Base is used to map Python classes to database tables.
SQLite Database:

The database is created using SQLAlchemy with SQLite as the backend.
Data Population:

A DataFrame wind is created with 6,000 rows and columns matching the weather table.
Data is inserted using bulk_insert_mappings for performance.
Flexibility:

Replace the sample DataFrame creation code with your own data-loading mechanism.
'''
