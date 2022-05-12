import os
import json
from config import Folders, Support
from parsers.parse_main import ParseMain
from utilities.work_files import (
    create_json_empty, 
    check_presence_file
)


class ParseManually(ParseMain):
    """
    class which is dedicated to check parsing manually after the user
    """
    def __init__(self) -> None:
        super(ParseManually, self).__init__()
        self.df_path = os.path.join(
            Folders.folder_temp_full,
            self.develop_csv_name(False, Support.name)
        )
    
    def develop_parse_main(self) -> None:
        """
        Method which is dedicated to create parsed dataframe
        Input:  None
        Output: we developed the main parsed from the csv
        """
        df = self.develop_df( 
            Support.name,
            Support.link,
            create_json_empty(True)
        )
        if check_presence_file(self.df_path):
            df = self.develop_df_merged(
                self.df_path,
                df
            )
        self.develop_csv(df, self.df_path)