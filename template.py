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
    'research/trials.ipynb',
    'app.py',
    'store_index.py',
    'static/.gitkeep',
    'templates/chat.html'
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)

    if filedir !='' :
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory; {filedir} for the file {filename}')
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath, 'w') as f:
            pass 
            logging.info(f'creating empty file: {filepath}')

    else:
        logging.info(f'{filename} is already created')
