#1_question_Answer
employees = [
    ("Vikram", 35, 8.75),
    ("Neha", 30, 12.50),
    ("Charlie", 50, 15.50),
    ("Rahul", 20, 7.00)
]
i = employee
for employee in employees:
    wage = employee[1]*employee[2]
    name = employee[0]
    print(f"{name} has to be paid ${wage} for this week")

#1_question_Answer
   
   employees = [
    ("Vikram", 35, 8.75),
    ("Neha", 30, 12.50),
    ("Charlie", 50, 15.50),
    ("Rahul", 20, 7.00 )]
hourly_wages = 0    
list =len(employees)

for s in employees:
    hourly_wage = s[2]
    hourly_wages= hourly_wages+hourly_wage

Avg_wages = hourly_wages/list
print("Average hourly wage: $",Avg_wages)

for n in employees:
    name = n[0]
    
    if n[2] > Avg_wages :
        print(f"{name} earns more than average")
    else:
        print(f"{name} earns less than average")


