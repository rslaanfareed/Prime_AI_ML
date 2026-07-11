#calculate average------------------------
def calculate_average_marks(marks):
    
    sum=0
    for i in marks:
        sum+=i
    average=(sum/len(marks))
    return average
    


#calculate grade--------------------------------
def calculate_grade(marks):
    grade=""
    average=calculate_average_marks(marks)
    if average>=90:
        grage='A+'
    elif average>=80 and average<90:
        grade='A'
    elif average>=70 and average<80:
        grade='B'
    elif average>=60 and average<70:
        grade='C'
    elif average>=50 and average<60:
        grade='D'
    else:
        grade='F'
    
    return grade    


#update marks
def update_marks():
    try:
        roll=int(input("Enter roll no to update marks: "))
        
        for d in students:

            if d["roll"]==roll:
                new_marks=[]
                i=0
                while i<5:
                    mark=int(input(f"Enter marks for subject {i+1}:"))
                    new_marks.append(mark)
                    i+=1
                print(new_marks)
                d["marks"]=new_marks
                
                d["average"]=calculate_average_marks(new_marks)

                d["grade"]=calculate_grade(new_marks)
                print("Student updated")
                break
    except ValueError:
        print("Invalid value entered")
        


#search student---------------------------------
def search():
    try:
        roll=int(input("Enter roll no to search: "))
        for d in students:
            if d["roll"]==roll:
                print("Student found")
                print(d)
                return
            else:
                print("Student not found")
    except ValueError:
        print("Roll no Invalid")





#add student---------------------------------
def add_student():
    print("\nadding new student\n")

    try:
        roll=int(input("Enter roll no: "))
        #important: accessing dictionary elements if dictionary is inside a list [{key: value}]-----------------
        for i in students:
            if i["roll"]==roll:
                print("Roll No already added")
                return
        name=input("Enter student name: ").casefold()
        age=int(input("Enter student age: "))

        if age<15 or age>30:
            print("Age must be between 15 and 30")
            return

        dep=input("Enter department: ").casefold()
        marks=[]
        i=0
        while i<5:
            mark=int(input(f"Enter marks for subject {i+1}: "))
            if mark<0 or mark>100:
                print("Marks must be between 0 and 100")
                continue
            marks.append(mark)
            i+=1
    except ValueError:
        print("Invalid Value entered")
        return
        #adding to the dictionary
    students.append({
            "roll":roll,
            "name":name,
            "age":age,
            "dep":dep,
            "marks":marks,
            "average":calculate_average_marks(marks),
            "grade":calculate_grade(marks)
        })
    print(f"Student {name} added successfully!")




#delete student
def delete_student():
    try:
        roll=int(input("Enter roll no to delete student:"))
        for d in students:
            if d["roll"]==roll:
                students.remove(d)
                break
        print("Student deleted")
    except ValueError:
        print("invalid value for roll no")    



#reports----------------------------------------
def generate_reports():

#HIGHEST SCORER
    highest=0
    for d in students:
        if d["average"]>highest:
            highest=d["average"]
            roll=d["roll"]
            h_dict=d
    print("----------------------------")
    print("HIGHEST SCORER")
    print(f"Roll no: {roll}")
    print(f"Marks: {highest}")
    print(h_dict)
    print("----------------------------")

#LOWEST SCORER
    lowest=100
    for e in students:
        if e["average"]<lowest:
            lowest=e["average"]
            roll=e["roll"]
            l_dict=e
    
    print("LOWEST SCORER")
    print(f"Roll no: {roll}")
    print(f"Marks: {lowest}")
    print(f"{l_dict}")
    print("----------------------------")


#PASSED AND FAILED COUNT
    passed=0
    failed=0
    for i in students:
        if i["average"]>=50:
            passed+=1
        else:
            failed+=1
    print(f"Passed Students: {passed}")
    print("----------------------------")

    print(f"Failed Students: {failed}")
    print("----------------------------")


#OVERALL CLASS AVERAGE
    sum=0
    for d in students:
        sum=sum+d["average"]
    average=sum/len(students)
    print(f"Overall Average: {average}")
    print("----------------------------")

#HIGHEST MARKS IN EACH SUBJECT
    
    for i in range(5):
        
        highest = 0
        
        for s in students:
            current_mark = s["marks"][i]
            
            if current_mark > highest:
                highest = current_mark
                
        print(f"Subject {i+1} highest marks: {highest}")
    print("---------------------------------------")
    for i in range(5):
        
        lowest=100
        
        for s in students:
            current_mark=s["marks"][i]
            
            if current_mark<lowest:
                lowest = current_mark
                
        print(f"Subject {i+1} lowest marks: {lowest}")

    print("--------------------------------------")

#display all students---------------------------
def display_all():
    print("----------------------------")
    print("Roll\tName\t\tDept\tAverage\tGrade")
    for val in students:
        print(val.get("roll"),"\t",val.get("name"),"\t\t",val.get("dep"),"\t",val.get("average"),"\t",val.get("grade"))
    print("----------------------------")



#main 
students=[
    {
        "roll":101,
        "name":"ali",
        "age":23,
        "dep":"sed",
        "marks":[45,45,45,90,0],
        "average":45,
        "grade":'F'
    }
    ,
    {
        "roll":102,
        "name":"sam",
        "age":22,
        "dep":"ced",
        "marks":[80,90,90,90,90],
        "average":88,
        "grade":'A+'
    }
    ,
    {
        "roll":103,
        "name":"abc",
        "age":20,
        "dep":"med",
        "marks":[60,60,60,60,90],
        "average":66,
        "grade":'C'
    }
]
while True:
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student")
    print("4. Update student marks")
    print("5. delete student")
    print("6. generate reports")
    print("7. exit")

    user_input=int(input("Choose one option (1-8):"))
    match user_input:
        case 1:
            add_student()

        case 2:
            display_all()

        case 3:
            search()
        
        case 4:
            update_marks()

        case 5:
            delete_student()

        case 6:
            generate_reports()
        case 7:
            break
        case _:
            print("Invalid Input")