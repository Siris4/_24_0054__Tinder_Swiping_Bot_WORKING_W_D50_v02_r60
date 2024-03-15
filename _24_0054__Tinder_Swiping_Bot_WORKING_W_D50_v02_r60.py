from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

# Constants
EMAIL = "YOUR_EMAIL"

# Function to log messages
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{timestamp} - {message}")

def init_driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    log_message("WebDriver initialized.")
    return driver

def click_element(driver, by, value, description):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        element.click()
        log_message(f"{description} clicked successfully.")
        return True
    except TimeoutException:
        log_message(f"{description} not clickable or not found.")
        return False

def login_sequence(driver):
    # Click decline button
    click_element(driver, By.XPATH, "//div[contains(text(), 'I decline')]", "Decline button")

    # Click main login button
    if click_element(driver, By.CLASS_NAME, "l17p5q9z", "Main login button"):
        # Select English language
        if click_element(driver, By.XPATH, "//span[contains(text(), 'English')]", "English language option"):
            # Click additional login button if present
            click_element(driver, By.CSS_SELECTOR, "a[href*='tinder.onelink.me'] div.l17p5q9z", "Additional login button")

            # Continue with Google login attempt
            click_element(driver, By.CSS_SELECTOR, "span.nsm7Bb-HzV7m-LgbsSe-BPrWId", "Continue with Google button")

def main():
    driver = init_driver()
    driver.get("https://tinder.com/")
    log_message("Navigated to Tinder's login page.")

    login_sequence(driver)

    # Additional steps for Google login iframe and email input would go here

    input("Press Enter to exit...\n")
    driver.quit()

if __name__ == "__main__":
    main()
