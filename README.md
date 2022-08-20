# Automatic-Ticket-Maker

Automatic Ticket Maker, with easy to make and choose scripts for the ticket.

## Saving selenium cookies with this guide
https://ashley-tharp.medium.com/how-to-stay-logged-in-when-using-selenium-in-the-chrome-browser-869854f87fb7

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Optionsoptions = Options()
options.add_argument("--user-data-dir=C:\\Users\\Ashley\\Desktop\\UserData")options.page_load_strategy = 'normal'driver = webdriver.Chrome(options=options)driver.get("https://www.pexels.com/")
```
