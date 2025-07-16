import os
from pathlib import Path
import logging

logging.basicConfig(
     filename='log_file_name.log',
     level=logging.INFO, 
     format= '[%(asctime)s]: %(message)s',
     datefmt='%H:%M:%S'
 )

list_of_files=[
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'setup.py',
    'research/trials.py,'
    'app.py',
    'store_index.py',
    'static',
    'templates/chat.html'
]