import os
import sqlite3
from sqlite3.dbapi2 import Connection
from config import Folders

class DataUsage:
    """
    class which is dedicated to operate values with the databases
    """
    def __init__(self) -> None:
        self.folder_storage = os.path.join(Folders.folder_current, 
                            Folders.folder_storage)
        os.path.exists(self.folder_storage) or os.mkdir(self.folder_storage)
    
    def check_values(self) -> str:
        """
        Method which is dedicated to check values     
        """
        pass
        # os.path.