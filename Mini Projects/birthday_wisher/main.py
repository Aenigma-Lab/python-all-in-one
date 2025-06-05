import smtplib



# my_email = "idealshubham1998@gmail.com"
# passwd = "shubham123()"
# with smtplib.SMTP("smpt.gmail.com") as connection:
# ## connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(user=my_email, password=passwd)
#
#     connection.sendmail(from_addr=my_email, to_addrs="f10.shubham@gmail.com", msg="Subject: Hello from Shubham\n\nThis is the body of my email.")
# ## connection.close()


#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "shubham@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )