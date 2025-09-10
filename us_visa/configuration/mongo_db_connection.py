import sys

from us_visa.exception import HandleException
from us_visa.logger import logging

import os
from us_visa.constants import DB_NAME, CONNECTION_URL
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DB_NAME) -> None:
        try:
            MongoDBClient.client = pymongo.MongoClient(CONNECTION_URL, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
            
        except Exception as e:
            raise HandleException(e,sys)