import smtplib

from pysss import password

my_email = "idealshubham1998@gmail.com"
passwd = "shubham123()"
with smtplib.SMTP("smpt.gmail.com") as connection:
# connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=passwd)

    connection.sendmail(from_addr=my_email, to_addrs="f10.shubham@gmail.com", msg="Subject: Hello from Shubham\n\nThis is the body of my email.")
# connection.close()