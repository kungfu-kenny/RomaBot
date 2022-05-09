import requests
import pandas as pd
from pprint import pprint
from utilities.work_files import check_folders


class ParseMain:
    """
    class which is dedicated to use after in the finding text
    """
    def __init__(self) -> None:
        check_folders()

    @staticmethod
    def get_html_values(url:str) -> str:
        """
        Static method which is dedicated to get html for the parsing
        Input:  url = url value to the selected
        Output: text value which would be used as html
        """
        return requests.get(url).text

    @staticmethod
    def develop_csv(df:pd.DataFrame, df_path:str) -> None:
        """
        Static method which is dedicated to store dataframe 
        Input:  df = dataframe which was previously created
                df_path = string value for the full path
        Output: we created new dataframe
        """
        df.to_csv(df_path)

    @staticmethod
    def develop_csv_name() -> str:
        """
        Static method which is dedicated to create csv name in that cases
        Input:  
        Output: string which was previously developed in that cases
        """
        pass

    def develop_parse_main(self) -> None:
        """
        Method which is dedicated to produce main work on the parsing
        Input:  None
        Output: we developed the csv value for the parsing
        """
        pass
