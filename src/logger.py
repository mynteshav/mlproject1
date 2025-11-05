import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # create a log file. 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # get the log path
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #get the log file path.
''' whenever we really want to create the log we really need to set see 
if you override the functionality of the logging we have to probabily set this
have into the basic config. '''

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s- %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=='__main__':
    logging.info("Logging has started")