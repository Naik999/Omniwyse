import json
class New:

    
    def __init__(self,f_Name ,m_Name ,l_Name,id,collage):
      self.first = f_Name
      self.middle = m_Name
      self.last = l_Name
      self.id = id
      self.collage = collage
  
    def generate_mail(self):
        new_dict = {}
        for student in data_num['student']:
            if student['m_Name'] != 'null':
                full_name = student['f_Name']+student['m_Name']+student['l_Name']
                G_mail = f"{student ['collage']}.{student['id']}{student['f_Name']}{student['m_Name']}{student['l_Name']}@gmail.com"
            else:
                full_name =student['f_Name']+student['l_Name']
                G_mail = f"{student ['collage']}.{student['id']}.{student['f_Name']}{student['l_Name']}@gmail.com"
            new_dict[G_mail] = {"id": student['id'], "fullName": full_name}

        return new_dict
with open("dict.json","r")as file_name:
    data_num =json.load(file_name)

for student in data_num['student']:
    t = New(**student)
    mail = t.generate_mail()
print(mail)













# import json
 
# with open("dict.json", "r") as data_son:
#     data = json.load(data_son)
# dict = {}
# for student in data['student']:

#     if student['m_Name'] != "null":
#         fn = student['f_Name']+student['m_Name']+student['l_Name']
#         email =f"{student ['collage']}.{student['id']}{student['f_Name']}{student['m_Name']}{student['l_Name']}@gmail.com"
#     else:
#         fn =student['f_Name']+student['l_Name']
#         email =f"{student ['collage']}.{student['id']}.{student['f_Name']}{student['l_Name']}@gmail.com"
#     dict[email]={"id": student["id"],"fullname": fn}
# details = json.dumps(dict,indent=(3))   
# print(details)

        