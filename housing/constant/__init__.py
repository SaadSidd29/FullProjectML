import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME="config.yaml"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = get_current_time_stamp()


TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIRECTORY_KEY = 'artifact_dir'


DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'          ## This is the folder name given and not related to yaml file. This is for artifacts
DATA_INGESTION_DOWNLAOD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
DATA_INGESTION_DIR_NAME_KEY = 'ingested_dir'
DATA_INGESTION_TRAIN_DIR_KEY = 'ingested_train_dir'
DATA_INGESTION_TEST_DIR_KEY = 'ingested_test_dir'


DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_TRANSFORMATION_CONFIG_KEY = 'data_transformation_config'
DATA_EVALUATION_CONFIG_KEY = 'data_evaluation_config'
MODEL_TRAINER_CONFIG_KEY = 'model_trainer_config'
MODEL_PUSHER_CONFIG_KEY = 'model_pusher_config'