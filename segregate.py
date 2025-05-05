import os
import logging

log_file = '/var/log/python'
logging.basicConfig(filename=f'{log_file}/{os.path.basename(__file__).split(".")[0]}_python.log',format="%(levelname)s %(asctime)s :: %(message)s",level=logging.DEBUG)

folder = os.getcwd()
ext = []

def scan_path():
    logging.debug(f'Scanning path {folder}')
    for file in os.listdir(folder):
        file_ext = file.split(".")
        nf=len(file_ext)
        if nf == 2 and file_ext[1] not in ["git","ipynb"] and file_ext[1] not in ext:
            ext.append(file_ext[1])
    return ext

def make_dir(names):
    for name in names:
        try:
            os.makedirs(f'{name.upper()}_files')
        except:
            logging.debug(f'Dir for {name} already exits')
            continue





make_dir(scan_path())