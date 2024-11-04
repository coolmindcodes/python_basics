#dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime("%a,  %d-%m-%Y")  # 19-01-2024
print(formatted_date)

after_forty_days = today + timedelta(weeks=40)  # Ctl + Click
print(after_forty_days)

dob = "1990-01-25"
#convert to date object
date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
age  = today.year - date_of_birth.year
print("I am ", age, " years old")


age_in_days = datetime.today() -  date_of_birth
print(age_in_days.days // 365)
