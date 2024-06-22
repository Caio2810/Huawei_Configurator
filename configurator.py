from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from welcome import title


def initialize_driver():
    driver_path = r'chromedriver-win64\chromedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


def click_element(driver, xpath, delay=1):
    element = driver.find_element('xpath', xpath)
    element.click()
    time.sleep(delay)

def clean_and_type(driver, xpath, text, delay=1):
    element = driver.find_element('xpath', xpath)
    element.send_keys(Keys.CONTROL, 'a')  # Select all text
    element.send_keys(Keys.BACKSPACE)  # Clear input
    element.send_keys(text)
    time.sleep(delay)

def main():
    print("-- Welcome to the Huawei Router Python Configuration -- \n")

    # Constants
    NETWORK_SSID = input("Type your Wi-fi SSID: \n")

    while True:
        PASSWORD = input("Type your password (should have at least 8 characters): \n")
        if len(PASSWORD) < 8:
            print("!! Password should have at least 8 characters !! \n")
        else:
            break

    URL = input("Router URL:  \n")

    print("\nNetwork SSID:", NETWORK_SSID)
    print("Network Password:", PASSWORD)


    driver = initialize_driver()
    driver.get(URL)

    # Beginning
    click_element(driver, '//*[@id="guide_user_agree_ctrl_checkbox_ctrl"]')
    click_element(driver, '//*[@id="guidebtnbegin"]')
    click_element(driver, '//*[@id="guide"]/div[2]/div/div[2]/div[2]/span')
    click_element(driver, '//*[@id="scenarionext"]/span')
    click_element(driver, '//*[@id="networkcablenext"]/span')
    click_element(driver, '//*[@id="uncableIgnor"]/span')
    click_element(driver, '//*[@id="IP_Routed_radio"]/span')
    click_element(driver, '//*[@id="wanconfignextbtn"]/span', delay=2)

    # SSID and Password
    clean_and_type(driver, '//*[@id="guide_wifi24_ssid_ctrl"]', NETWORK_SSID)
    driver.find_element('xpath', '//*[@id="guide_wifi_password_ctrl"]').send_keys(PASSWORD)
    driver.find_element('xpath', '//*[@id="guide_user_pwd_ctrl"]').send_keys("YOUR ROUTER PASSWORD") # Here you define your router password
    click_element(driver, '//*[@id="guide_wifi_next_btn"]/span')
    click_element(driver, '//*[@id="wlannext"]/span', delay=30)
    click_element(driver, '//*[@id="finishbtn"]/span')

    # Part 2
    driver.find_element('xpath', '//*[@id="userpassword_ctrl"]').send_keys("YOUR ROUTER PASSWORD") # Here you type your router password to login
    click_element(driver, '//*[@id="loginbtn"]')
    click_element(driver, '//*[@id="wifi"]/div')
    click_element(driver, '//*[@id="dbhoOn_btnId"]', delay=3)
    click_element(driver, '//*[@id="more"]/div')
    click_element(driver, '//*[@id="safesettingsparent_menuId"]')

    try:
        click_element(driver, '//*[@id="remote_access_selectlist_parenselect"]')
        element = driver.find_element('xpath', '//*[@id="remote_Enable_selectlist_SmallSelectBoxScrollItemID"]')
        element.click()
    except NoSuchElementException:
        pass
    
    # Here the we're configuring the router's remote acess, first the code types the port and then the IP
    clean_and_type(driver, '//*[@id="port_ctrl"]', "YOUR_PORT")
    clean_and_type(driver, '//*[@id="address_ctrl"]', "SELECTED_IP")
    click_element(driver, '//*[@id="SendSettings_submitbutton"]', delay=3)

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
