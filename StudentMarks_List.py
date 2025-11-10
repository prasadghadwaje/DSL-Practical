from statistics import mode,StatisticsError
def average(student_info_DSA):
    total_marks=sum(student_info_DSA.values())
    total_student=len(student_info_DSA)
    return total_marks/total_student

def highest(student_info_DSA):
    return max(student_info_DSA,key=student_info_DSA.get)

def lowest(student_info_DSA):
    return min(student_info_DSA,key=student_info_DSA.get)
def absent(student_info_DSA):
    count=0
    for i in student_info_DSA.values():
        if i==0:
            count+=1
    return count
def freqency(student_info_DSA):
    try:
        m=mode(student_info_DSA.values())
        mark=[]
        for k,v in student_info_DSA.items():
            if v==m:
                mark.append(k)
        print("Most frequent marks:", mark, "get", m, "marks")
    except StatisticsError:
        return  mark
    
# starting point of program 
student_info_DSA={
    "prasad":55,
    "sumit":54,
    "shivam":0,
    "nishant":34,
    "kunal":0
}
ch=int(input("\t\t Welcome \n1--> calculate average \n2--> Min Max marks \n3-->absent stdents number \n4-->frequency \nEnter the choice :"))
if ch==1:
   print("Average Marks :", average(student_info_DSA))
elif ch==2:
    print("Max marks :",highest(student_info_DSA),student_info_DSA[highest(student_info_DSA)])
    print("Min :",lowest(student_info_DSA),student_info_DSA[lowest(student_info_DSA)])
elif ch==3:
    print("Number of absent student's :",absent(student_info_DSA))
elif ch==4:
   freqency(student_info_DSA)
else:
    print("invalid input")