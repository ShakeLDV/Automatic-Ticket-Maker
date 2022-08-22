from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


def microsoft_login():
    refresh_screen()
    print("Please sign-in to your account and wait 10 seconds.")
    sleep(10)


def fill_ticket(name, email, chosen_script):
    PLACEHOLDER = '[name]'
    sleep(10)
    requester_box = driver.find_element(By.CLASS_NAME, "controllerSelector.input_common__input___3x9J-.Input__inputIconRight___2KMWt")
    requester_box.clear()
    requester_box.send_keys(email)
    title_box = driver.find_element(By.NAME, "name")
    #This has to change everytime it is a different ticket
    title_box.send_keys(chosen_script)
    chosen_script = chosen_script + ".txt"
    sleep(1)
    iframe = driver.find_element(By.ID, 'react-tinymce-0_ifr')
    driver.switch_to.frame(iframe)
    description_box = driver.find_element(By.ID, 'tinymce')
    with open(f"Ticket-Scripts/{chosen_script}") as script:
        selected_script = script.read()
        selected_script = selected_script.replace(PLACEHOLDER, name)
        description_box.send_keys(selected_script)
    driver.switch_to.default_content() 


def select_category(category):
    subcategory = driver.find_element(By.XPATH, '//*[@id="new_incident"]/div/div[2]/div/div/div/div[1]/div[1]/div[6]/div/div/span[2]/div/div/div/div/div[1]/div/div/span')
    subcategory.click()
    subcategory = driver.find_element(By.CLASS_NAME, 'DropdownSearch__searchInput___2cj2_')
    #This has to change everytime it is a different ticket
    subcategory.send_keys(category)
    sleep(2)
    subcategory.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)


def send_ticket():
    create_ticket_button = driver.find_element(By.CLASS_NAME, 'Button__button___2F6IB.ButtonSkins__commonSkin___2Proz.ButtonSkins__main___30X1Z.Button__large___1_y4D.Button__nowrap___26yBf')
    create_ticket_button.click()
    sleep(5)
    driver.quit()


def get_name():
    return input("What is the name? (first names only) ").title()


def get_email():
    return input("What is the email? ")


def refresh_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def list_scripts():
    list_folder = os.listdir("Ticket-Scripts")
    list_folder = [i.split(".txt")[0] for i in list_folder]
    length = (len(list_folder))
    for i in range(length):
        print (f"{i}.) {list_folder[i]}")
    chosen_script = int(input("Choose a script: "))
    chosen_script = list_folder[chosen_script]
    return chosen_script

    
def main():
    finish = False
    while finish == False:
        global service
        global driver
        name = get_name()
        if name == "Exit":
            break
        email = get_email()
        script = list_scripts()
        options = Options()
        options.add_argument("--user-data-dir=C:\\temp\\userdata")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://eitc.samanage.com/incidents/new")
        driver.minimize_window()
        sleep(5)
        if driver.title == "Sign in to your account":
            microsoft_login()
        fill_ticket(name, email, script)
        select_category(script.split()[0])
        send_ticket()
        refresh_screen()


if __name__ == "__main__":
    main()