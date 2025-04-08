import logging
import os
from datetime import datetime

# Generate log file name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory (without the file name)
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True) # Ensure the directory exists

# Define the full log file path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,

)

#Example logging statement
# if __name__=="__main__":
#     logging.info("Logging has started")