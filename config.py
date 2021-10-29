import os
from dataclasses import dataclass

@dataclass
class Folders:
    folder_current = os.getcwd()
    folder_storage = 'storage'