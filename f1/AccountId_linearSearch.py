total_employee=int(input("Enter total number of employes :")) 

employee=[]
print("Enter the ID's of Employe....")
for i in range(total_employee):
    id=int(input())
    employee.append(id)

print("----Search the Id Linearly----")
ch=int(input("Enter the Employee Id :"))

found=False
for i in range(len(employee)):
    if employee[i]==ch:
        print("Employee Id Found At Position :",i+1 )
        found=True
        break
    else:
        found=False
if found==False:
     print("Employee Id Not Found In The Record's")
        

