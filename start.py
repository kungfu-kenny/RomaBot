from parsers.parse_citaty import ParseCitaty


try:
    for cls in [
        ParseCitaty
    ]:
        cls().develop_parse_main()

except Exception as e:
    print(e)
    print('..............................................')