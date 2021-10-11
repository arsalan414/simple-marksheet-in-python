print(".....WELCOME TO THE PROGRAM.....");
print("Enter obtained Marks out of 100");
eng = float(input("English: "));
isl = float(input("Islamiat: "));
maths = float(input("Mathematics: "));
obtainedMarks = eng + isl + maths;
totalMarks = 300;

percentage = (obtainedMarks / totalMarks)*100;


if percentage >=80 and percentage <=100:
    grade="A+"
elif percentage >=70 and percentage <=100:
    grade = "A"
elif percentage >=60 and percentage <=100:
    grade = "B"
elif percentage >=50 and percentage <=100:
    grade = "C"
elif percentage >=40 and percentage <=100:
    grade = "D"
elif percentage <40 and percentage <=100:
    grade = "F"
else:
    grade="Unknown"  

    
print("\n\n")
print(".......Marksheet.......");
print("Subject \tTotal marks \tObtained marks")
print(f"ENGLISH \t100 \t\t{eng}\nIslamiat \t100 \t\t{isl}\nMathematics \t100 \t\t{maths}\n");

print(f"percentage: {round(percentage,2)}% \tGrade: {grade} ")
