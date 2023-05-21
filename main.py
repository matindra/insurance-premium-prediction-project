from insurance.logger import logging
from insurance.exception import InsuranceException
import os, sys
from insurance.utils import get_collection_as_dataframe
from insurance.entity import config_entity
from insurance.components.data_ingestion import DataIngestion
from insurance.components.data_validation import DataValidation

# def test_logger_and_exception():
#     try:
#         logging.info("starting the test_logger_and_exception")
#         result = 3/0
#         print(result)
#         logging.info("Ending point of the test_logger_and_exception")
#     except Exception as e:
#         logging.debug(str(e))
#         raise InsuranceException(e, sys)
    
    
    
if __name__=="__main__":
    try:
        
        training_pipeline_config = config_entity.TrainingPipelineConfig()
       
        #data ingestion
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
       
        #data validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                         data_ingestion_artifact=data_ingestion_artifact)
        
        data_validation_artifact = data_validation.initiate_data_validation()

    except Exception as e:
        print(e)