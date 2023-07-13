import smtplib
import datetime as dt
import random

#s290-1-1-1 define email address and password
MY_EMAIL = "xxx"
MY_PASSWORD = "YYY"

now = dt.datetime.now()
weekday = now.weekday()

# s290-1-1-2 when it's monday, it will be triggered
if weekday == 1:
    # s290-1-1-3 get one line from the file
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    # s290-1-1-4 send the line to email,it's pretty a fixed writing method
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


