from progress.bar import ShadyBar

class Logger:
    def __init__(self) -> None:
        self.m_enable = False

    def setEnabled(self, enable=bool):
        self.m_enable = enable

    def printSummary(self, consoleName=str, gameName=str):
        if self.m_enable:
            print(f"Starting download of spritesheets for video game {gameName} (console: {consoleName})")

    def printDownload(self, link=str):
        if self.m_enable:
            print(f"Retrieving and parsing link: {link}")

    def printDownloadDone(self):
        if self.m_enable:
            print("Download finished")

    def startProgessBar(self, max=int):
        if self.m_enable:
            self.m_progressBar = ShadyBar("Retrieving Spritesheets...", max = max)

    def incrementProgessBar(self):
        if self.m_enable and self.m_progressBar:
            self.m_progressBar.next()
            if self.m_progressBar.remaining == 0:
                print("\n")