import re
import requests
from zipfile import ZipFile
from io import BytesIO, StringIO

from bs4 import BeautifulSoup
from PIL import Image

from .VerboseTools import Logger
from .DataTools import ResourceSaver, StringHelper

class SpritersResourceDownloader:
    UrlSpritersResource = "https://www.spriters-resource.com"
    UrlRegexValidator = "^https?:\/\/www\.spriters-resource\.com\/([a-zA-Z0-9_]+)\/([a-zA-Z0-9_]+)"

    SpritesheetDivClass = "icondisplay"
    IconHeaderTextDivClass = "iconheader"
    SpritesheetImageIdClass = "assetdisplay"
    ZipDownloadId = "download"

    def __init__(self, link=str) -> None:
        self.m_link = link
        self.m_logger = Logger()

        if not self.validateLink():
            raise Exception("Invalid link. Please provid a link to a game on the website spriters-resource.com")

        self.m_saveDirectory = f"{ResourceSaver.DefaultDownloadDataFolderPath}/{self.m_consoleName}/{self.m_gameName}"

    def validateLink(self) -> bool:
        pattern = re.compile(SpritersResourceDownloader.UrlRegexValidator)
        pattern.match(self.m_link)
        match = pattern.match(self.m_link)
        if len(match.groups()) == 2:
            self.m_consoleName = match.group(1)
            self.m_gameName = match.group(2)
            return True
        return False

    def setVerboseEnabled(self, enable=bool):
        self.m_logger.setEnabled(enable)

    def startDownload(self):
        links = self.computeSpritesheetLinks()
        self.downloadSpritesheets(links)

    def computeSpritesheetLinks(self):
        self.m_logger.printSummary(self.m_consoleName, self.m_gameName)
        self.m_logger.printDownload(self.m_link)
        page = requests.get(self.m_link).content

        soup = BeautifulSoup(page, "html.parser")
        spritesheetDivList = soup.find_all("div", {"class" : f"{SpritersResourceDownloader.SpritesheetDivClass}"})
        
        links = []

        for spritesheetDiv in spritesheetDivList:
            spriteSheetLinks = spritesheetDiv.find_all("a")
            for spriteSheetLink in spriteSheetLinks:
                link = spriteSheetLink.get("href")
                name = spriteSheetLink.find("div", {"class" : f"{SpritersResourceDownloader.IconHeaderTextDivClass}"}).text
                name = StringHelper.cleanString(name)
                links.append({
                    "link": link,
                    "name": name
                })
        return links

    def downloadSpritesheets(self, links):
        self.m_logger.startProgessBar(len(links))

        for linkData in links:

            self.m_logger.incrementProgessBar()
            page = requests.get(f"{SpritersResourceDownloader.UrlSpritersResource}{linkData['link']}").content
            soup = BeautifulSoup(page, "html.parser")
            spritesheetDiv = soup.find("div", {"id": f"{SpritersResourceDownloader.SpritesheetImageIdClass}"})
            spritesheet = spritesheetDiv.find("img", recursive=False) if spritesheetDiv is not None else None

            if spritesheet is not None:
                spriteLink = spritesheet.get("src")
                self.downloadAndSaveSprite(spriteLink, linkData["name"])

            else:
                zipLink = soup.find("a", {"id": f"{SpritersResourceDownloader.ZipDownloadId}"})
                
                if zipLink is not None:
                    self.downloadZIP(zipLink.attrs['href'], linkData['name'])

        self.m_logger.printDownloadDone()

    def downloadZIP(self, url: str, name: str):
        url = f'{SpritersResourceDownloader.UrlSpritersResource}{url}'
        response = requests.get(url, stream = True)

        if response.ok:
            ResourceSaver.saveZip(ZipFile(BytesIO(response.content)), self.m_saveDirectory, name)

    def downloadAndSaveSprite(self, link=str, name=str):
        imageContent = requests.get(f"{SpritersResourceDownloader.UrlSpritersResource}{link}").content
        image = Image.open(BytesIO(imageContent)).convert('RGBA')
        ResourceSaver.saveImage(image, self.m_saveDirectory, name)

