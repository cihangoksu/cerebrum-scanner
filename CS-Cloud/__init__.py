import os
import sys

from _global_paths import __path_dict__

def add_path(path): 
    if path not in sys.path: sys.path.append(path)

for path_key, path_value in __path_dict__.items():
    add_path(path_value)
    print(f'{path_value} has been added.')



