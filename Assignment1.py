#1_question_Answer

word = input("Enter word:")

length = len(word)

if length > 10:

  middle_part = str(length-2)

  print(word[0]+middle_part+word[-1])

else:

  print(word)
 


 
#2_question_Answer

marks=int(input("enter  the marks(out of 100):"))


if marks>=0 and marks <=100:

    if marks >=95:

       print("A+") 

    elif marks>=90:

       print("A") 

    elif marks>=85:

       print("B+") 

    elif marks>=80:

       print("B") 

    elif marks>=75:       

      print("C+") 

    elif marks>=65:

      print("C") 

    elif marks>=55:

      print("D+") 

    elif marks>=45:

      print("D") 

    elif marks<45:

      print("F")        


else:

     print("invalid input:")