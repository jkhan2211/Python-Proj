import os

for file in os.listdir('C:/tmp/reg'):
    if file.endswith((".c")):
        print(file)