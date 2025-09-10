import os
from datetime import date

DB_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

CONNECTION_URL = "mongodb+srv://mohsin416m_db:qYRARS22ofYoppWO@cluster0us.xuqdwh2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0US"

PIPELINE_NAME : str = "usvisa"
ARTIFACT_DIR : str = "artifact"

MODEL_FILE_NAME = "model.pkl"


TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocesssing.pkl"

FILE_NAME : str = "usvisa.csv"
TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2