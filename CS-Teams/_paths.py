import os
import sys

current_dir = os.path.dirname(__file__)
cscommon_dir = os.path.join(os.path.dirname(current_dir), 'CS-Common')

sys.path.insert(0, cscommon_dir) 
from _global_paths import __path_dict__

# Let's add local paths
__path_dict__['main'] = os.path.dirname(__file__)
__path_dict__['lib'] = os.path.join(__path_dict__['main'], 'lib')

__path_dict__['kvfiles'] = os.path.join(__path_dict__['main'], 'kvfiles')


def add_path(path): 
    if path not in sys.path: sys.path.append(path)

for path_key, path_value in __path_dict__.items():
    add_path(path_value)
    print(f'{path_value} has been added.')





