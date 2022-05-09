import imp
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
        
        """
        #TODO
        pass

    def develop_parse_main(self) -> None:
        return super().develop_parse_main()