import os
import re

from PIL import Image

class ImageSaver:
    DefaultDownloadDataFolderPath = "/downloaded"

    def createFolder(folderName):
        if not os.path.isdir(folderName):
            os.makedirs(folderName, exist_ok=True)

    def saveImage(image : Image, saveDirectory, fileName):
        ImageSaver.createFolder(f"./{saveDirectory}")
        image.save(f"./{saveDirectory}/{fileName}.png")

class StringHelper:
    def cleanString(string: str):
        pattern = re.compile("[\W]+")
        return pattern.sub("_", string)