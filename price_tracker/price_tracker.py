import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.canadacomputers.com/product_info.php?cPath=43_557_559&item_id=195035&language=en'
email = '' # the sender and receiver of the message
price_limit = 1500
user_agent = ''
g_app_pass = '' # google app password

# fetches price, checks for drop
def check_price():
    headers = {"User-Agent": user_agent}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # id/class names and string manipulation should be adjusted if the site is changed
    price = soup.find(class_="h2-big").getText()
    price_int = int(price[2:7].replace(',', ''))
    item_name = soup.find(class_="h3 mb-0").getText()

    if(price_int < price_limit):
        send_mail(item_name)

# notifies the price drop by email
def send_mail(i_name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, g_app_pass)

    subject = "Item price drop, from price_tracker.py"
    body = "The price for the following item has dropped below $" + str(price_limit) + ":\n\n" + i_name + ".\n\n\nLink: " + url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(email, email, msg)

    print("Email sent to " + email)

    server.quit()

# while script is open, checks price hourly
while(True):
    check_price()
    time.sleep(3600)