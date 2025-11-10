
def binary_search(employee,targetId):
    low=0
    high=len(employee)-1
    
    while low<=high:
        mid=(low+high)//2
        if(employee[mid]==targetId):
            return mid
        if employee[mid]<targetId:
            low=mid+1
        else:
            high=mid-1
    return -1


total_employee=int(input("Enter total number of employes :")) 

employee=[]
print("Enter the ID's of Employe....")
for i in range(total_employee):
    id=int(input("Employee:"))
    employee.append(id)
employee.sort()

print("----Search the Id Binary----")
targetId=int(input("Enter the Employee Id :"))
result=binary_search(employee,targetId,)
if result!=-1:
    print("Inputed Id found At :", result+1)
else:
    print("not found")