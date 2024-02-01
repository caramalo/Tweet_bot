from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Twitter credentials
USERNAME = "Your_Twitter_Username"
PASSWORD = "*Your_Twitter_Password"
TWEET_TEXT = "Your tweet text goes here"
HASHTAGS = ["#example", "#automation"]

# Path to chromedriver executable (download from https://chromedriver.chromium.org/)
CHROMEDRIVER_PATH = 'C:\\Windows\\chromedriver.exe'
# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# URL for Twitter login and compose tweet
LOGIN_URL = "https://twitter.com/login"
COMPOSE_TWEET_URL = "https://twitter.com/compose/tweet"

# Open Twitter login page
driver.get(LOGIN_URL)
time.sleep(2)

# Fill in login credentials and submit
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username" and @name="text"]'))
)
username_input.send_keys(USERNAME)

# Find and click the "Next" button
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Next")]'))
)
next_button.click()

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password" and @name="password"]'))
)
password_input.send_keys(PASSWORD)

password_input.send_keys(Keys.RETURN)
time.sleep(2)

# Navigate to tweet compose page
driver.get(COMPOSE_TWEET_URL)
time.sleep(2)

# Fill in tweet text
tweet_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Post text"]'))
)
tweet_input.send_keys(TWEET_TEXT)

# Add hashtags
for hashtag in HASHTAGS:
    tweet_input.send_keys(" " + hashtag)

time.sleep(1)
# Simulate left click of the mouse at the current cursor position
action = ActionChains(driver)
action.click()
action.perform()


# Click tweet button
tweet_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetButton"]'))
)
tweet_button.click()

time.sleep(2)

# Close the browser
driver.quit()