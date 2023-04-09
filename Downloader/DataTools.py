import os
import re

from PIL import Image
from zipfile import ZipFile

class ResourceSaver:
    DefaultDownloadDataFolderPath = "/downloaded"

    def createFolder(folderName):
        if not os.path.isdir(folderName):
            os.makedirs(folderName, exist_ok=True)

    def saveImage(image : Image, saveDirectory, fileName):
        ResourceSaver.createFolder(f"./{saveDirectory}")
        image.save(f"./{saveDirectory}/{fileName}.png")

    def saveZip(file: ZipFile, directory: str, fileName: str):
        ResourceSaver.createFolder(f'./{directory}')
        file.extractall(f'./{directory}/{fileName}')

class StringHelper:
    def cleanString(string: str):
        pattern = re.compile("[\W]+")
        return pattern.sub("_", string)