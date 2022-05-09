import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

@dataclass
class Folders:
    folder_current = os.getcwd()
    folder_storage = 'storage'
    folder_update = 'update'
    folder_merged = 'merged'
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

@dataclass
class Support:
    file_json_empty = 'json_update.json'
    file_json_containment = 'containment'
    file_json_full = os.path.join(
        Folders.folder_update_full,
        file_json_empty
    )

@dataclass
class Citaty:
    link = 'https://ru.citaty.net/tsitaty-o-volkakh/'