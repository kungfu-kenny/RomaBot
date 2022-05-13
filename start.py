from parsers.parse_manually import ParseManually
from parsers.parse_citaty import ParseCitaty
from parsers.parse_anekdoty import ParseAnekdoty
from config import value_noncheck


try:
    for cls in [
        ParseManually,
        ParseCitaty,
        ParseAnekdoty
    ]:
        cls().develop_parse_main(value_noncheck)

except Exception as e:
    print(e)
    print('..............................................')