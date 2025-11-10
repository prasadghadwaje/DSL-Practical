import array 

def linear_search(students,target_roll):
    for i in range(len(students)):
        if students[i]==target_roll:
            return i
    return -1       
    

print("\t\t----Welcome----")
total_student=int(input("Enter the total Number of student :"))

students=array.array('i',[])
print("Enter the roll Numbers :")
for i in range(total_student):
    roll=int(input(f"Student {i+1} :"))
    students.append(roll)
students=array.array('i',sorted(students))
target_roll=int(input("Enter Roll No. to search :"))
if linear_search(students,target_roll)!=-1:
    print("Given Roll Number Is Found At position :",linear_search(students,target_roll))
else:
    print("Roll number is not foung : Not Present ")




