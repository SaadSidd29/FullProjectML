from collections import namedtuple

## This file should not be in config_entity as config_entity file is responsible for input locations nad directories
## While artifact_entity file is responsible for output related locations and directories

DataIngestionArtifact = namedtuple("DataIngestionArtifact", [  
                                                                "train_file_path",
                                                                "test_file_path",
                                                                "is_ingested",
                                                                "message"
                                                            ])