import json

with open("dict.json", "r") as data_son:
    data = json.load(data_son)
new_dict = {}
for student in data['student']:

    if student['m_Name'] != "null":
        fn = student['f_Name']+student['m_Name']+student['l_Name']
        email =f"{student ['collage']}.{student['id']}{student['f_Name']}{student['m_Name']}{student['l_Name']}@gmail.com"
    else:
        fn =student['f_Name']+student['l_Name']
        email =f"{student ['collage']}.{student['id']}.{student['f_Name']}{student['l_Name']}@gmail.com"
    new_dict[email]={"id": student["id"],"fullname": fn}
    
with open('change_data.json',"w") as file_data:
    json.dump(new_dict,file_data,indent=(3))
print(file_data)
