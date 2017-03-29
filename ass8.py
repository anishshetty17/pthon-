import os
for file in os.listdir("/home/sois/Desktop/anish"):
    if file.endswith(".pdf"):
        print(os.path.join("/home/sois/Desktop/anish", file))