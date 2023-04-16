
import datetime as dt
import smtplib
import random

now = dt.datetime.today()

MY_EMAIL = "*********@****.com"#Write here the email you want to send from
MY_PASSWORD = "***************"#Write here the password of your email.
# It is better to take specific password for this resason

with open("quotes.txt", "r") as quotes:
    lines = quotes.readlines()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:#careful about this line and change SMTP accordingly with
    connection.starttls()                                    #your email type
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    if now.strftime("%A").lower() == "sunday" or now.strftime("%A").lower() == "tuesday" or\
            now.strftime("%A").lower() == "friday":
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="idrisbahce26@gmail.com",
            msg=f"Subject:MOTIVATION!\n\n{random.choice(lines)}"
        )
