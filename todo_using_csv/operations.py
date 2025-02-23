import os
import logging
import time
import pandas as pd
from datetime import datetime


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


#* --------------------- Class to Load and Save Data Only -------------------- *#


class TaskStorage:
    def __init__(self, filename="todotask.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            logger.info("Creating New Task Storage File")
            return pd.DataFrame(
                columns=["Title", "Date", "Time", "Description", "Status"]).to_csv(
                    self.filename, index=False)
    
    def load_task(self ):
        logger.info("Loading Task From Storage File")
        return pd.read_csv(self.filename)
    
    def save_task(self, df):
        logger.info("Saving Task To Storage File")
        df.to_csv(self.filename, index=False)
    
#* --------------------- Class to Perform CRUD Operations -------------------- *#
class Todo:
    def __init__(self, storage):
        self.storage = storage
    
    def add_task(self, title, description):
        df = self.storage.load_task()
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H-%M-%S")
        new_task = {"Title": title, "Date":date, "Time":time,"Description": description, "Status": "Pending" }
        data = pd.DataFrame([new_task])
        df = pd.concat([df, data], ignore_index=True )
        self.storage.save_task(df)
        logger.info("Task Added Successfully")
    
    def read_task(self):
        df = self.storage.load_task()
        logger.info("Task Loaded Successfully")
        print(df)
    
    def update_task(self, title, status):
        df = self.storage.load_task()
        df.loc[df["Title"] == title, "Status"] = status
        self.storage.save_task(df)
        logger.info("Task Updated Successfully")
        
        print(df)
 
    
    def delete_task(self, title):
        df = self.storage.load_task()
        df = df.drop(df[df["Title"] == title].index)   
        self.storage.save_task(df)
        logger.info("Task Deleted Successfully")
        print(df)