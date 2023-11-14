import json

with open("dict.json", "r") as data_son:
    data = json.load(data_son)
for student in data['student']:
    if student ['m_Name'] != "null":
        print(f"{student['id']}.{student['f_Name']}{student['m_Name']}{student['l_Name']}@gmail.com")
    else : 
        print(f"{student['id']}.{student['f_Name']}{student['l_Name']}@gmail.com")
    details = json.dumps(student,indent=4)
    print(details)
