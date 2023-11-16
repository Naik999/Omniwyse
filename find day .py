import datetime

name = input("enter your date of birth-this formate(yyyy-mm-dd):")
day = datetime.datetime.strptime(name ,"%Y-%m-%d")
born = day.strftime("%A")
print(f'you born in {born}')