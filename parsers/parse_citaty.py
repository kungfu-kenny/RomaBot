import os
from bs4 import BeautifulSoup
from parsers.parse_main import ParseMain
from config import Folders, Citaty
from utilities.work_files import check_presence_file


class ParseCitaty(ParseMain):
    """
    class which is dedicated to get the bars from the citaty values
    """
    def __init__(self) -> None:
        super(ParseCitaty, self).__init__()
        self.df_path = os.path.join(
            Folders.folder_temp_full,
            self.develop_csv_name(False, Citaty.name)
        )

    def develop_parse_link(self) -> list:
        """
        Method which is dedicated to develop main link parsing 
        Input:  None
        Output: list of the citate and the authors
        """
        html = self.get_html_values(Citaty.link)
        soup = BeautifulSoup(html, 'html.parser')
        return [
            f"{c}\n{a}".replace('\xa0', ' ').replace('  ', ' ') for c, a in zip(
                [f.text for f in soup.find_all("p", attrs={"class":"blockquote-text"})],
                [f.text for f in soup.find_all("p", {"class": "blockquote-origin"})]
            ) if c
        ]

    def develop_parse_main(self) -> None:
        """
        Method which is dedicated to create parsed dataframe
        Input:  None
        Output: we developed the main parsed from the csv
        """
        df = self.develop_df( 
            Citaty.name,
            Citaty.link,
            self.develop_parse_link()
        )
        if check_presence_file(self.df_path):
            df = self.develop_df_merged(
                self.df_path,
                df
            )
        self.develop_csv(df, self.df_path)