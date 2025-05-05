import os
import logging
import shutil

log_file = '/var/log/python'
logging.basicConfig(filename=f'{log_file}/{os.path.basename(__file__).split(".")[0]}_python.log',format="%(levelname)s %(asctime)s :: %(message)s",level=logging.DEBUG)

folder = os.getcwd()
ext = []
file_list = []

def scan_path():
    logging.debug(f'Scanning path {folder}')
    for file in os.listdir(folder):
        file_ext = file.split(".")
        nf=len(file_ext)
        if nf == 2 and file_ext[1] not in ["git","ipynb"]:
            file_list.append(file)
            if file_ext[1] not in ext:
                ext.append(file_ext[1])
    return file_list, ext

def make_dir(names):
    for name in names:
        try:
            os.makedirs(f'{name.upper()}_files')
        except:
            logging.debug(f'Dir for {name} already exits')
            continue
    
def move_files(names):
    for name in names:
        foldername = f'{name.split(".")[1].upper()}_files'
        shutil.move(name,foldername)
        logging.debug(f"{name} moved to {foldername}")

file_list, extension = scan_path()
make_dir(extension)
move_files(file_list)