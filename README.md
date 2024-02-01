### Automated Tweet Poster Using Selenium WebDriver

This Python script automates the process of posting tweets on Twitter using Selenium WebDriver. It logs in to a Twitter account, composes a tweet with predefined text and hashtags, and posts it.

#### Features:
- Automates tweeting process on Twitter.
- Supports logging in with Twitter credentials.
- Posts tweets with predefined text and hashtags.

#### Prerequisites:
- Python installed on your system.
- Selenium WebDriver library installed (`pip install selenium`).
- Chrome WebDriver executable downloaded and located in the system path or specify the path manually (`CHROMEDRIVER_PATH`).

#### Usage:
1. Modify the script with your Twitter credentials (`USERNAME` and `PASSWORD`).
2. Specify the tweet text (`TWEET_TEXT`) and hashtags (`HASHTAGS`) you want to include in the tweet.
3. Download Chrome WebDriver executable from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/](https://googlechromelabs.github.io/chrome-for-testing/). Just find the right url for your platform, then paste it in the search bar. The zip file should download automatically, then unzip and save it in to your chosen directory. Make sure chrome is updated on your computer to the latest, you can do this by clicking the three vertical dots in the upper right corner of the chrome page then help > about google chrome. It should show the current version of chrome you are running and an option to update. After all this, make sure you specify the path to where you saved your chromedriver in the script (`CHROMEDRIVER_PATH`). I have saved mine in 'C:\\Windows\\chromedriver.exe'
4. Run the script.

#### Note:
- Ensure you have a stable internet connection while running the script.
- Adjust the sleep times according to your internet speed and system performance.

#### Disclaimer:
This script is intended for educational purposes and should be used responsibly and in compliance with Twitter's terms of service.
