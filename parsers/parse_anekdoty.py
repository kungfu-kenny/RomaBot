import os
from pprint import pprint
from bs4 import BeautifulSoup
from parsers.parse_main import ParseMain
from utilities.work_files import check_presence_file
from config import (
    Folders, 
    AnekdotyGay,
    AnekdotyJews, 
    AnekdotyStupid,
    AnekdotyVeryStupid,
)


class ParseAnekdoty(ParseMain):
    """
    class which is dedicated to parse anekdoty website on different values
    """
    def __init__(self) -> None:
        super(ParseAnekdoty, self).__init__()

    @staticmethod
    def get_link_values(cls:object, value_int:int=0) -> str:
        """
        Static method which is dedicated to develop the 
        Input:  cls = selected class for the link
                value_int = selected value of the increment
        Output: we created link of the selected values
        """
        if value_int < 2:
            return cls.link
        return f"{cls.link}{cls.increment}/{value_int}"

    def develop_parse_link(self, cls:object, value_int:int=1, value_result:list=[]) -> list:
        """
        Method which is dedicated to develop main link parsing 
        Input:  cls = selected class for the search
                value_int = integer value of the selected 
        Output: list of the citate and the authors
        """
        link = self.get_link_values(cls, value_int)
        value_bool, value_html = self.get_html_values_boolean(link)
        if not value_bool:
            return value_result
        soup = BeautifulSoup(value_html, 'html.parser')
        value_result.extend(
            [
                [link, f.text.strip()] for f in soup.find_all('div', {"class": 'holder-body'})
            ]
        )
        return self.develop_parse_link(
            cls, 
            value_int + 1, 
            value_result
        )
        
    def develop_parse_main(self, previous_check:bool=False) -> None:
        """
        Method which is dedicated to produce values of the anekdots
        Input:  previous_check = boolean value which signify the new value for it
        Output: we created all
        """
        for cls in [
            AnekdotyGay,
            AnekdotyVeryStupid,
            AnekdotyStupid,
            AnekdotyJews,
        ]:
            df_path = os.path.join(
                Folders.folder_temp_full,
                self.develop_csv_name(False, cls.name)
            )
            if previous_check and check_presence_file(df_path):
                continue
            
            df_list = self.develop_parse_link(cls)
            if df_list:
                link, parsed = [*zip(*df_list)]
            else:
                link, parsed = [], []
            df = self.develop_df(
                cls.name,
                link,
                parsed
            )
            if check_presence_file(df_path):
                df = self.develop_df_merged(
                    df_path,
                    df
                )
            self.develop_csv(df, df_path)