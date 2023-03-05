import datetime
import pandas as pd
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
SMTP_SERVER = "YOUR EMAIL PROVIDER SMTP SERVER ADDRESS"

def get_birthdays():
    data = pd.read_csv("birthdays.csv")
    birthdays_dict = {(row["month"], row["day"]): row for _, row in data.iterrows()}
    return birthdays_dict

def get_letter(name):
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name)
        return contents

def send_email(to_addr, contents):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_addr, msg=f"Subject: Happy Birthday!\n\n{contents}")

def main():
    today = datetime.datetime.now().strftime('%m-%d')
    birthdays = get_birthdays()
    if today in birthdays:
        birthday_person = birthdays[today]
        contents = get_letter(birthday_person["name"])
        send_email(birthday_person["email"], contents)

if __name__ == '__main__':
    main()

