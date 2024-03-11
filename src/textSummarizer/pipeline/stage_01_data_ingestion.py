from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.data_ingestion import DataIngestion 
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass


    def main(self):

        try:
            
            config = ConfigurationManager() # Intialized ConfigurationManager object config
            data_ingestion_config = config.get_data_ingestion_config() # Called get_data_ingestion_config func and returned the data ingestion config class with respective values
            data_ingestion = DataIngestion(config=data_ingestion_config) # Intialized DataIngestion object 
            data_ingestion.download_file() # Invoking the methods
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e