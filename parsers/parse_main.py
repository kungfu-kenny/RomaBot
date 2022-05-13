import os
import requests
import pandas as pd
from utilities.work_files import (
    check_folders,
    check_presence_file
)
from config import Folders


class ParseMain:
    """
    class which is dedicated to use after in the finding text
    """
    def __init__(self) -> None:
        check_folders()

    @staticmethod
    def get_link_values() -> str:
        """
        Static method which is dedicated to develop the link values
        Input:  None
        Output: string value of requested link
        """
        pass

    @staticmethod
    def get_html_values(url:str) -> str:
        """
        Static method which is dedicated to get html for the parsing
        Input:  url = url value to the selected
        Output: text value which would be used as html
        """
        return requests.get(url).text

    @staticmethod
    def get_html_values_boolean(url:str) -> set:
        """
        Static method which is dedicated to get the boolean values plus the html
        Input:  url = url of the selected values
        Output: boolean value of the okay data
        """
        value_used = requests.get(url)
        value_bool = True if 199 < value_used.status_code < 300 else False
        return value_bool, value_used.text if value_bool else ''

    @staticmethod
    def develop_csv(df:pd.DataFrame, df_path:str) -> None:
        """
        Static method which is dedicated to store dataframe 
        Input:  df = dataframe which was previously created
                df_path = string value for the full path
        Output: we created new dataframe
        """
        df.to_csv(df_path, index=False)

    @staticmethod
    def develop_csv_name(merged:bool, name:str) -> str:
        """
        Static method which is dedicated to create csv name in that cases
        Input:  merged = boolean value which signify the check of the merged value
                name = string value of the name
        Output: string which was previously developed in that cases
        """
        return f"merged.csv" if merged else f"{name}.csv"

    @staticmethod
    def develop_df(name:str='', link:str='', value_list:list=[]) -> pd.DataFrame:
        """
        Static method which is dedicated to develop basic dataframe for all of it
        Input:  name = name of the selected string
                link = string link value
                value_list = list of parsed strings
        Output: pandas dataframe of the 
        """
        return pd.DataFrame(
            {
                "Source": [name for _ in value_list],
                "String": value_list,
                "Link": [link for _ in value_list] if isinstance(link, str) else link,
            }
        )

    @staticmethod
    def develop_df_merged(df_path:str, df_new:pd.DataFrame) -> pd.DataFrame:
        """
        Static method which is dedicated to develop merged
        Input:  df_path = path to the previous dataframe
                df_new = previously calculated dataframe values
        Output: required pandas dataframe
        """
        df_new = pd.concat(
            [
                pd.read_csv(df_path),
                df_new
            ]
        )
        df_new.drop_duplicates(inplace=True)
        return df_new

    def develop_df_all(self) -> pd.DataFrame:
        """
        Method which is dedicated to created all possible
        Input:  None
        Output: merged dataframe to all of it
        """
        df = pd.concat(
            [
                pd.read_csv(
                    os.path.join(Folders.folder_temp_full, f)
                )
                for f in os.listdir(Folders.folder_temp_full)
                if os.path.splitext(f)[1].lower() == '.csv'
            ]
        )
        df.drop_duplicates(
            subset=['String'], 
            inplace=True
        )
        df_path = os.path.join(
            Folders.folder_merged_full, 
            self.develop_csv_name(1, '')
        )
        if check_presence_file(df_path):
            df = self.develop_df_merged(
                df_path, 
                df
            )
        self.develop_csv(df, df_path)

    def develop_parse_main(self, previous_check:bool=False) -> None:
        """
        Method which is dedicated to produce main work on the parsing
        Input:  previous_check = boolean value which signify the new value for it
        Output: we developed the csv value for the parsing
        """
        pass
