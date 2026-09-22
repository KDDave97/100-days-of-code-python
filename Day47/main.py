from bs4 import BeautifulSoup
import requests
import smtplib
import os

my_email = os.environ.get("SMTP_EMAIL")
password = os.environ.get("SMTP_PASSWORD")

threshold_price = 100

product_link = "https://appbrewery.github.io/instant_pot/"
response = requests.get(product_link)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

price_whole = float(soup.find(name="span", class_="a-price-whole").getText())
product_name = " ".join(soup.find(name="span", id="productTitle").getText().split())

message =(f"{product_name} is available!\n"
          f"The product that you wanted to buy is now under the set threshold!\n"
          f"You set the threshold to {threshold_price}, the current price is {price_whole}!\n"
          f"Buy it now at {product_link} ")

if price_whole < threshold_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Price below threshold\n\n"
                                                                                         f"{message}".encode("utf-8"))
