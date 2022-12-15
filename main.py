from _datetime import datetime
import pandas
import random
import smtplib

# Check if today matches a birthday in the birthdays.csv
today = datetime.now()
print(today)
today_tuple = (today.month, today.day)
text_number = random.randint(1,4)

#create email and password
my_email = "manafreedom@gmail.com"
my_password = "deptazfajupzldvx"

# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates
    file_path = f"letter_templates/letter_{text_number}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # replace the [NAME] with the person's actual name from birthdays.csv
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        # Send the letter generated to that person's email address
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

