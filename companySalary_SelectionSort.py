print("\t\t ...Wellcomt to my company...")

def selectionSort(salaries):
    for i in range(len(salaries)):
        small=i
        for j in range(i+1,len(salaries)):
            if salaries[j]<salaries[small]:
               small=j
        salaries[i],salaries[small]=salaries[small],salaries[i]
        
def topFive(salaries):
    print("Top five salary :")
    counter=1
    for i in range(len(salaries)-1,0,-1):
        if i >=len(salaries)-5:
            print(f"Salary rank {counter}:{salaries[i]}")
    counter+=1

#main function
total_employee=int(input("Enter the total number of employee :"))
salaries=[]

print("Enter the salaries of the Employee :")
for i in range(total_employee):
    sl=float(input(f"Enter salary of Employee {i+1} : "))
    salaries.append(sl)

print(f"Salaries of the Employee before Sorting :\n{salaries}")
selectionSort(salaries)

print(f"Salaries after the selection Sort (Acssending) :\n{salaries}")
print("\n")

topFive(salaries)

print("\n\t-----Thank you ------")
