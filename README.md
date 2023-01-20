![GitHub license](https://img.shields.io/github/license/torresflo/Spriters-Resource-Downloader.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/Spriters-Resource-Downloader.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/Spriters-Resource-Downloader.svg)

<p align="center">
  <h1 align="center">Spriters Resource Downloader</h3>

  <p align="center">
    A downloader for the website <a href="https://www.spriters-resource.com">Spriters Resource</a>
    <br />
    <a href="https://github.com/torresflo/Spriters-Resource-Downloader/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Introduction](#introduction)
* [Getting Started](#getting-started)
  * [Prerequisites and dependencies](#prerequisites-and-dependencies)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Introduction
Spriters-Resource-Downloader
This repository contains a command line application to simply download all sprites and spritesheets of a given game from the website <a href="https://www.spriters-resource.com">Spriters Resource</a> (`https://www.spriters-resource.com"`).

## Getting Started

### Prerequisites and dependencies

This repository is tested on Python 3.7+.

You should install Spriters Resource Downloader in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
First, create a virtual environment with the version of Python you're going to use and activate it.

You can install directly all required packages by using the file `requirements.txt` and doing:
```bash
pip install -r requirements.txt
```

### Installation

Follow the instructions above then clone the repo (`git clone https:://github.com/torresflo/Spriters-Resource-Downloader.git`).\
You can now launch the app by running `spriters-resource-downloader.py`.

## Usage

Just launch the application with:

```
python spriters-resource-downloader.py [-h] [-v] url
```

Here are the possible arguments:

```
positional arguments:
  url            URL to a game on the website spriters-resource.com

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  use it to print progress during download
```

It is recommended to activate the verbose mode (optional, not activated by default) to keep track of the progress.

### Example

The next command line will download all the sprites referenced on this <a href="https://www.spriters-resource.com/game_boy_gbc/pokemongoldsilver/">page</a> and put them in the folder `downloaded/game_boy_gbc/pokemongoldsilver/` while printing progress during download:

```
python spriters-resource-downloader.py -v https://www.spriters-resource.com/game_boy_gbc/pokemongoldsilver/
```


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
