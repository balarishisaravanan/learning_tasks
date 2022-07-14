from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


email = "EMAIL_ADDRESS"
email_password = "GMAIL_PASSWORD" 
new_password = "NEW_PASSWORD"


def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()


def test_request_password():
    driver.get("https://www.logitechg.com/en-in/my-account.html")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "a[data-analytics-title=Login]").click()
    driver.find_element(By.CLASS_NAME, "forgot_link").click()
    driver.find_element(By.ID, "Email address").send_keys(email)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "button_text").click()
    time.sleep(30)  # long time delay because of captcha, solve it manually

    # If user has completed captcha, they see this element on screen
    success = driver.find_elements(By.CLASS_NAME, "status_area.success")
    assert len(success) == 1


def test_open_gmail():
    driver.get("https://mail.google.com")
    driver.find_element(By.ID,"identifierId").send_keys(email)
    driver.find_element(By.ID, "identifierNext").click()
    time.sleep(5)

    password_element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "password")))
    password_element.send_keys(email_password)
    driver.find_element(By.ID, "passwordNext").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//span[@email='noreply@accounts.logi.com']/ancestor::tr[@role='row']").click()
    time.sleep(3)
    collection = driver.find_elements(By.TAG_NAME,"a")
    for i in collection:
        if i.get_attribute('href') is not None:
            if "id.logi.com" in i.get_attribute('href'):
                driver.get(i.get_attribute('href'))
                time.sleep(7)
                driver.find_element(By.ID,"New Password").send_keys(new_password)
                time.sleep(5)
                driver.find_element(By.CLASS_NAME,"button").click()
                time.sleep(5)
                driver.find_element(By.CLASS_NAME, "button").click()
                time.sleep(3)
                driver.find_element(By.ID, "Email address").send_keys(email)
                driver.find_element(By.ID,"Password").send_keys(new_password)
                driver.find_element(By.CLASS_NAME,"button").click()
                time.sleep(30)
                break
            
        
    


    time.sleep(3)

def test_destruction():
    driver.close()
    driver.quit()
    print("Process complete")
