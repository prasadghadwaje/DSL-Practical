from statistics import mode,StatisticsError
print("\t Welcome to Prasad's library/n")

member_records={
    "prasad":4,
    "sumit":2,
    "shivam":3,
    "nishant":0,
    "kunal":0
}

book_borrowed={
    "DSA":3,
    "OS":22,
    "DE":1,
    "ED":0,
    "OOP":2
}

print("\n1--> calculate the average. \n2-->calculate the max and min book borrowed. \n3-->No. of member with zero book borrow. \n4--> frequency/n")
ch=int(input("Enter the choice for the menu :"))
if ch==1:
    total_member =len(member_records)
    totalBook_borrowed=sum(member_records.values())
    print("Average Book Borrowed :",totalBook_borrowed/total_member)
elif ch==2:
    max_borrowed=max(book_borrowed,key=book_borrowed.get)
    min_borrowed=min(book_borrowed,key=book_borrowed.get)
    print("Max Count :",max_borrowed,book_borrowed[max_borrowed]," times")
    print("Min Count :",min_borrowed,book_borrowed[min_borrowed]," times")
elif ch==3:
    count=0
    for i in member_records.values():
        if i==0:
            count=count+1
    print("members wich borrow zero books are :", count)
elif ch==4:
    try:
        m = mode(book_borrowed.values())
        most_frequent = []
        for k, v in book_borrowed.items():
            if v == m:
                most_frequent.append(k)
        print("Most frequent book(s):", most_frequent, "borrowed", m, "times")
    except StatisticsError:
        print("No unique mode found among book borrowings.")
