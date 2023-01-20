import argparse

from Downloader import SpritersResourceTools

parser = argparse.ArgumentParser(
    description = "Download all available spritessheet for a given spriters-resource.com game URL.",
)

parser.add_argument("url", help="URL to a game on the website spriters-resource.com")
parser.add_argument("-v", "--verbose", action="store_true", help="use it to print progress during download")

args = parser.parse_args()

downloader = SpritersResourceTools.SpritersResourceDownloader(args.url)
if args.verbose:
    downloader.setVerboseEnabled(True)

downloader.startDownload()