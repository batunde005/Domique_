#student_score = 60
#print(student_score >60 andstudent_score< 70)

name_of_user = int(input("enter a player age"))
year_of_player = 2024
if name_of_user == year_of_player:
    print("you are qualify")

elif name_of_user > year_of_player:
    print("you are under age")

elif name_of_user < year_of_player:
    print("you are way too low")

else:
    print("you are not eligible")