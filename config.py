import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

value_noncheck = os.getenv("NONCHECK", False)

@dataclass
class Folders:
    folder_current = os.getcwd()
    folder_storage = 'storage'
    folder_update = 'update'
    folder_merged = 'merged'
    folder_temp = 'temporary'
    folder_storage_full = os.path.join(
        folder_current,
        folder_storage
    )
    folder_update_full = os.path.join(
        folder_storage_full,
        folder_update
    )
    folder_merged_full = os.path.join(
        folder_storage_full,
        folder_merged
    )
    folder_temp_full = os.path.join(
        folder_storage_full,
        folder_temp
    )

@dataclass
class DbCredentials:
    host = os.getenv('DB_HOST', '')
    name = os.getenv('DB_NAME', '')
    database = os.getenv('DB_DATABASE', '')
    password = os.getenv('DB_PASSWORD', '')
    db_path = os.path.join(
        Folders.folder_storage_full, 
        'local.db'
    )

@dataclass
class Support:
    name = 'support'
    link = 'manually'
    file_json_empty = 'json_update.json'
    file_json_containment = 'containment'
    file_json_full = os.path.join(
        Folders.folder_update_full,
        file_json_empty
    )

@dataclass
class Citaty:
    name = 'citaty'
    link = 'https://ru.citaty.net/tsitaty-o-volkakh/'

@dataclass
class AnekdotyStupid:
    increment = 'page'
    name = 'anekdoty_stupid'
    link = 'https://anekdoty.ru/tupo-no-smeshno/'
    
@dataclass
class AnekdotyVeryStupid:
    increment = 'page'
    name = 'anekdoty_very_stupid'
    link = 'https://anekdoty.ru/pro-glupost/'

@dataclass
class AnekdotyGay:
    increment = 'page'
    name = 'anekdoty_gay'
    link = 'https://anekdoty.ru/pro-geev/'

@dataclass
class AnekdotyJews:
    increment = 'page'
    name = 'anekdoty_jews'
    link = 'https://anekdoty.ru/pro-evreev/'
