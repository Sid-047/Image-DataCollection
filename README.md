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

3. Enlist the Search Queries:
    ```sh
    #ImgScrapping.py
    q = ['<Search Keyword Query>', '<Search Keyword Query>', '<Search Keyword Query>']
    ```
    Alter the line of Code
   
4. Run the Tool:
    ```sh
    python ImgScrapping.py
    ```

5. Boom! That is it.

6. But Wait! What if yo Program's crashed? No Worries:
   ```sh
    python URLset_convo.py
    ```
   Select the right TimeStamp, then GooD to Go!

7. Just the Last One:
   ```sh
    python ImgDown.py
    ```
   You could see the Image Files Written

## Features

- Automated Image Web Scrapping via Selenium.
- The image URLs are backed in a .txt file in Real-time.
- Concept of Threading & TimeOut is used to efficiently write the Image files.
- The Image URLs are scrapped at first, next off the Image downloads are initiated.
- Should a glitch disrupt the execution, Fear Not! the URLs stored in the .txt files can be served to initiate Image downloads via ImgDown.py.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
