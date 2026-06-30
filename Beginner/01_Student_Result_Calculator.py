
marks=['marks1','marks2','marks3','marks4','marks5','marks6']
marks[0]=float(input('your english marks '))
marks[1]=float(input('your computer marks '))
marks[2]=float(input('your urdu marks '))
marks[3]=float(input('your maths marks '))
marks[4]=float(input('your science marks '))
marks[5]=float(input('your history marks '))
print(f"your marks are {marks}")
def average_calculator(marks):
    average=sum(marks)/len(marks)
    return average
print(f"your average marks are {average_calculator(marks)}")
total_marks=len(marks)*100
obtained_marks=sum(marks)
percentage=(obtained_marks/total_marks)*100
def grade(percentage):
    if percentage >=90:
        return 'your grade is A '
    elif 80 <= percentage < 90:
        return 'your grade is B'
    elif 70 <= percentage < 80:
        return 'your garde is C'
    elif 60 <= percentage < 70:
        return 'your grade is D'
    elif 40 <= percentage < 60:
        return 'your grade is F'
    else:
        return 'your grade is below F'
print(f"your percentage is {percentage:.2f}%") 
print(grade(percentage))

def final_decision(percentage):
    if 60 <= percentage <=100:
        return 'PASS'
    else:
        return 'FAIL'
    
print(final_decision(percentage))










    
