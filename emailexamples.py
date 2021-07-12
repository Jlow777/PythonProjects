# import smtplib
#
# my_email = "jwlow@email.wm.edu"
# password = "ExamplePass"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="to_person@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                         )
#
# The primary errors are with security settings tied to the email account

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
#
# date_of_birth = dt.datetime(year=1991, month=10, day=7)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "appbrewery@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )