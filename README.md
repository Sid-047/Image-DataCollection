# Image Scrapping

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Sid-047/Image-DataCollection.svg)](https://github.com/Sid-047/Image-DataCollection/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/Sid-047/Image-DataCollection.svg)](https://github.com/Sid-047/Image-DataCollection/issues)
[![GitHub Forks](https://img.shields.io/github/forks/Sid-047/Image-DataCollection.svg)](https://github.com/Sid-047/Image-DataCollection/network/members)

> Image Data Collection Tool for Object Detection, Segmentation & Classification achieved through Web Scrapping (Google Images) ~ Image Scrapping Peeps!

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Installation

1. Clone the Repository:
   ```sh
   git clone https://github.com/Sid-047/Image-DataCollection.git
   ```

## Usage

1. Navigate to the Project Directory:
    ```sh
    cd Image-DataCollection
    ```

2. Install Dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    Note: Mozilla FireFox Web Browser is Recommended

   Windows
   ```sh
    winget install Mozilla.Firefox
    ```
   MacOS
   ```sh
    brew install firefox
    ```
   Linux
   ```sh
    sudo snap install firefox
    ```
4. Wait, Wanna Create QueryList?
    ```sh
    python queryList.py
    ```
    Here it Comes!
    ```sh
    Come On Start Entering the Search QueryKeyWords Yo!
    Enter 'Exit' to Finish

    '
    <Search Keyword Query1>
    <Search Keyword Query2>
    .
    .
    .
    <Search Keyword QueryN>
    Exit
    '

    The Search KeyWord Query List Yo!
    ['<Search Keyword Query1>', '<Search Keyword Query2>', ..., '<Search Keyword QueryN>']
    ```
    Now copy the QueryList

5. Enlist the Search Queries:
    ```sh
    #ImgScrapping.py
    q = ['<Search Keyword Query>', '<Search Keyword Query>', '<Search Keyword Query>']
    ```
    Alter the line of Code or Paste the queryList from the Previous Stage
   
6. Run the Tool:
    ```sh
    python ImgScrapping.py
    ```

7. Boom! That is it.

8. But Wait! What if yo Program's crashed? No Worries:
   ```sh
    python URLset_convo.py
    ```
   Select the right TimeStamp, then GooD to Go!

9. Just the Last One:
   ```sh
    python ImgDown.py
    ```
   You could see the Image Files Written

## Features

- Automated Image Web Scrapping via Selenium.
- The image URLs are backed in a .txt file in Real-time.
- Image files are Dynamically written without OverWriting.
- Concept of Threading & TimeOut is used to efficiently write the Image files.
- The Image URLs are scrapped at first, next off the Image downloads are initiated.
- The QueryLiat can be generated via the built-in tool as per the User Inputs each Line.
- Should a glitch disrupt the execution, Fear Not! the URLs stored in the .txt files can be served to initiate Image downloads via ImgDown.py.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
