import json

with open("dict.json", "r") as data_son:
    data = json.load(data_son)
dict = {}
for student in data['student']:

    if student['m_Name'] != "null":
        fn = student['f_Name']+student['m_Name']+student['l_Name']
        email =f"{student ['collage']}.{student['id']}{student['f_Name']}{student['m_Name']}{student['l_Name']}@gmail.com"
    else:
        fn =student['f_Name']+student['l_Name']
        email =f"{student ['collage']}.{student['id']}.{student['f_Name']}{student['l_Name']}@gmail.com"
    dict[email]={"id": student["id"],"fullname": fn}
details = json.dumps(dict,indent=(3))   
print(details)
