##################################################
#       dummy_consumer   Settings File
##################################################
import os

## Set the global logging level to debug
# LOGGING_DEBUG = True

## Consumer configuration
### Each consumer has different parameters and can be found in the documentation
CONSUMER_CONFIG = {
    "PARAMS": {
        "bootstrap.servers": os.environ["CONSUMER_SERVER"],
        "group.id": os.environ["CONSUMER_GROUP_ID"],
        "security.protocol": "SASL_PLAINTEXT",
        "sasl.mechanism": "SCRAM-SHA-256",
        "sasl.username": os.environ["USERNAME"],
        "sasl.password": os.environ["PASSWORD"],
        "auto.offset.reset": "earliest",
    },
    "TOPICS": os.environ["CONSUMER_TOPICS"].strip().split(","),
}
## Step Configuration
STEP_CONFIG = {
    # "N_PROCESS": 4,            # Number of process for multiprocess script
    # "COMMIT": False,           #Disables commit, useful to debug a KafkaConsumer
}
