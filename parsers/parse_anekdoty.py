import os
from bs4 import BeautifulSoup
from parsers.parse_main import ParseMain
from utilities.work_files import check_presence_file
from config import (
    Folders, 
    AnekdotyJews, 
    AnekdotyStupid
)


class ParseAnekdoty(ParseMain):
    """
    class which is dedicated to parse anekdoty website on different values
    """
    def __init__(self) -> None:
        super(ParseAnekdoty, self).__init__()
        #TODO work from here

    def develop_parse_main(self) -> None:
        """
        
        """
        pass