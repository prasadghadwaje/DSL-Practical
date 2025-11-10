print("\t\t ...Wellcomt to my company...")

def bubbleSort(salaries):
    for i in range(len(salaries)):
        for j in range(len(salaries)-1):
            if salaries[j]>salaries[j+1]:
                salaries[j],salaries[j+1]=salaries[j+1],salaries[j]

total_employee=int(input("Enter the total number of employee :"))
print("Enter the salaries of the Employee :")
salaries=[]
for i in range(total_employee):
    sl=float(input(f"Enter salary of Employee {i+1} : "))
    salaries.append(sl)

print(f"Salaries of the Employee before Sorting :{salaries}")
bubbleSort(salaries)
print(f"Salaries after the Bubble Sort (Acssending) :{salaries}")
print("\n\t-----Thank you ------")