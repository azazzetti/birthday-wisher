import pandas as pd
import datetime as dt
import random
import smtplib

# my_email = COMPLETE WITH YOUR OWN MAIL
# password = COMPLETE WITH YOUR OWN PASSWORD

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read()
        final_letter = contents.replace("[NAME]", birthday_person["name"])
        print(final_letter)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{final_letter}"
                            )
