import os
import json
from config import (
    Support, 
    Folders
)


def make_string(value_default:str) -> str:
    return value_default if value_default else ''

def make_sublists(value_list:list, n:int=Support.n) -> list:
    """
    Function which is dedicated to create the list of lists n size
    Input:  value_list = list values
            n = integer to new size
    Output: list of lists n size
    """
    def chunk(value_list:list, n:int):
        """
        Function for chunking values of the
        Input:  value_list = original list
                n = length of the sublists
        Output: len on which to chunk values
        """
        for i in range(0, len(value_list), n):
            yield value_list[i:i + n]
    return list(chunk(value_list, n))

def check_presence_file(path_file:str) -> bool:
    """
    Function which is dedicated to check files
    Input:  path_file = full path to the selected file
    Output: boolean value which shows file presence
    """
    return os.path.exists(path_file) and os.path.isfile(path_file)

def check_presence_folder(path_folder:str) -> bool:
    """
    Function which is dedicated to check folders
    Input:  path_folder = full path to the selected folder
    Output: boolean value which shows folder presence
    """
    return os.path.exists(path_folder) and os.path.isdir(path_folder)

def check_folder(path_folder:str) -> None:
    """
    Function which is dedicated to create folder if neccessary
    Input:  path_folder = full path to the folder
    Output: folder is neccessary
    """
    os.path.exists(path_folder) or os.mkdir(path_folder)

def check_folders() -> None:
    """
    Function to check folders which is used widely
    Input:  None
    Output: we created folders which is used
    """
    for f in [
        Folders.folder_storage_full,
        Folders.folder_merged_full,
        Folders.folder_update_full,
        Folders.folder_temp_full,
    ]:
        check_folder(f)

def create_json_empty(value_remove:bool=False) -> list:
    """
    Function which is dedicated to take the values from the user as a file
    Input:  value_remove = boolean value which takes to remove them
    Output: list of the given values from the user
    """
    def create_empty() -> None:
        with open(Support.file_json_full, 'w') as f:
            json.dump(
                {
                    Support.file_json_containment: [],
                }, 
                f, 
                indent=4
            )
    
    check_folders()
    if not check_presence_file(Support.file_json_full):
        create_empty()
        return []
    with open(Support.file_json_full, 'r') as f:
        ret = json.load(f)
    if value_remove:
        os.remove(Support.file_json_full)
        create_empty()
    return ret.get(
        Support.file_json_containment, 
        []
    )