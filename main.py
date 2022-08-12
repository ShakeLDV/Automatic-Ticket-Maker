from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
username = os.environ['username']
password = os.environ['password']


def microsoft_login():
    sleep(5)
    login_email = driver.find_element(By.ID, "i0116").send_keys(username, Keys.ENTER)
    sleep(2)
    login_password = driver.find_element(By.ID, "i0118").send_keys(password, Keys.ENTER)


def fill_ticket(name, email):
    PLACEHOLDER = '[name]'
    sleep(5)
    requester_box = driver.find_element(By.CLASS_NAME, "controllerSelector.input_common__input___3x9J-.Input__inputIconRight___2KMWt")
    requester_box.clear()
    requester_box.send_keys(email)
    title_box = driver.find_element(By.NAME, "name")
    title_box.send_keys("Password Reset")
    sleep(1)
    iframe = driver.find_element(By.ID, 'react-tinymce-0_ifr')
    driver.switch_to.frame(iframe)
    description_box = driver.find_element(By.ID, 'tinymce')
    with open("Ticket-Scripts/Password Reset") as script:
        selected_script = script.read()
        selected_script = selected_script.replace(PLACEHOLDER, name)
        description_box.send_keys(selected_script)
    driver.switch_to.default_content() 
# description_box.send_keys(f"Hello {name},\nThe password for your school account has been reset at your request. Please let us know if you have any other issues concerning your login information\nThank you!\nIT Help Desk\n(208)535-5444")

def select_category():
    subcategory = driver.find_element(By.XPATH, '//*[@id="new_incident"]/div/div[2]/div/div/div/div[1]/div[1]/div[6]/div/div/span[2]/div/div/div/div/div[1]/div/div/span')
    subcategory.click()
    subcategory = driver.find_element(By.CLASS_NAME, 'DropdownSearch__searchInput___2cj2_')
    subcategory.send_keys("Password Reset", Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)


def send_ticket():
    create_ticket_button = driver.find_element(By.CLASS_NAME, 'Button__button___2F6IB.ButtonSkins__commonSkin___2Proz.ButtonSkins__main___30X1Z.Button__large___1_y4D.Button__nowrap___26yBf')
    create_ticket_button.click()


def get_name():
    return input("What is the name? (first names only) ").title()
    
    
def get_email():
    return input("What is the email? ")


if __name__ == "__main__":
    name = get_name()
    email = get_email()
    driver.get("https://eitc.samanage.com/incidents/new")
    driver.maximize_window()
    microsoft_login()
    fill_ticket(name, email)
    select_category()

