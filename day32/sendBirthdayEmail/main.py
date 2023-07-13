from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "xxx@gmail.com"
MY_PASSWORD = "abcd1234()"
# s292-1-1-1 get currnet date and time
today = datetime.now()
today_tuple = (today.month,today.day)

# s292-1-1-2 read users' birthday data
data = pandas.read_csv("birthdays.csv")

# s292-1-1-3 create a dict to mapping user birthday and user data
birthdays_dict = {
    (data_row["month"],data_row["day"]): data_row for(index,data_row) in data.iterrows()
}

# s292-1-1-4 if today there is a user birthday,then send him/her an email
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # s292-1-1-5 read email template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # s292-1-1-6 replace template with user data
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    # s292-1-1-7 send user an email
    with smtplib.SMTP("smpt.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


