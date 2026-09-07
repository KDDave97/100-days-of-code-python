import smtplib
import random
import pandas
import datetime as dt

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
now = dt.datetime.now()

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"


for birthday in data_dict:
    if birthday["month"] == now.month and birthday["day"] == now.day:
        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        random_lettter = random.choice(letters)
        with open(random_lettter) as file:
            letter = file.read()
            letter = letter.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday["email"], msg=f"Subject:Happy Birthday {birthday["name"]}\n\n"
                                                                                     f"{letter}")
