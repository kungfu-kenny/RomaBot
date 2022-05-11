import requests
from pprint import pprint
from bs4 import BeautifulSoup
from parsers.parse_main import ParseMain
from config import Folders, Citaty


class ParseCitaty(ParseMain):
    """
    class which is dedicated to get the bars from the citaty values
    """
    def __init__(self) -> None:
        super(ParseMain, self).__init__()

    def develop_parse_link(self) -> list:
        """
        Method which is dedicated to develop main link parsing
        """
        #TODO add here the test version
        # print(Citaty.link)
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        html = requests.get(Citaty.link).text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        value_citate = [f.text for f in soup.find_all("p", attrs={"class":"blockquote-text"})]
        # pprint(value_citate)
        # print('..............................................')
        value_author = [f.text for f in soup.find_all("p", {"class": "blockquote-origin"})]
        # pprint(value_author)
        # print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

    def develop_parse_main(self) -> None:
        """
        
        """
        self.develop_parse_link()