# FlashFiber/Fibercop python scraper

This is my first experiment with Selenium.
I'm waiting for FlashFiber (https://flashfiber.it) to cover my house with FTTH connectivity but I find very annoying to go on the website and check the availability of the service manually.

I than decided to build a python script that uses the Selenium library and EdgeChromium (my fav browser) to check the website.

It may be useful to customize it directly with your own data and run it on a serverless platform to send daily automatic notifications on Telegram.

--------------------------------------------------------
As result of the cooperation between Tim, Fastweb and KKR the Flashfiber website is going to be decommissioned. I added the script to check the connection availability for the new website: https://fibercop.it

## Requirements:
- Python 3.X
- Selenium library installed
- msedge.selenium_tools library installed

### Preparation
- Install python: https://www.python.org/downloads/
- Install selenium:
`pip install selenium`
- Install msedge_selenium_tools:
`pip install msedge.selenium_tools`
- Download and put in the same script folder the MsEdgeDriver executable. You can download it from here (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### Usage
python check_flashfiber.py (old)

python check_fibercop.py

### Things to be implemented
Check if input data is valid, like Street and City.
