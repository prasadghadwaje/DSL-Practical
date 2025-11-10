class Hashing_UsChaining:
    def __init__(self,size=10):
        self.size=size
        self.table=[[] for _ in range(self.size)]

    def hashFunction(self,key):
        return key% self.size
    
    def insertKey(self, key ,value):
        index=self.hashFunction(key)
        for pair in self.table[index]:
            if pair[0]==key :
                pair[1]=value
                print(f" For Key {key} Value is Update to {value} at Index :{index}")
                return
        self.table[index].append([key,value])
        print(f"Key :{key} And Value :{value} Is Inserted At Index :{index}")

    def searchKey(self,key):
        index=self.hashFunction(key)
        if not self.table[index]:
            print(f"No data Available In Table at Index {index}")        
            return
        for pair in self.table[index]:
            if pair[0]==key:
                print(f"Key {key} found With Value Of {pair[1]} At Index : {index}")
                return
        print(f"Key {key} Not Found In The Table")

    def deletKey(self,key):
        index=self.hashFunction(key)
        for pair in self.table[index]:
            if pair[0]==key:
                self.table[index].remove(pair)
                print(f"Key {key} is Remove From index {index}")
                return
            
        print(f"Key {key} Not Found In The Table...")

    def display(self):
        for i in range(self.size):
            print(f" Table [{i+1}] :{self.table[i]}")

t=Hashing_UsChaining()
flg=True
while flg:
    print("\t\tWlecome")
    print("1--> insert key")
    print("2-->search key")
    print("3--> delete key")
    print("4-->display")
    print("5-->exit")
    ch=input("Enter the choice :")
    if ch=='1':
        key=int(input("Enter key  to insert(Integer Only):"))
        value=input("Enter value:")
        t.insertKey(key,value)
    elif ch=='2':
        key=int(input("Enter key to search (Integer Only):"))
        t.searchKey(key)
    elif ch=='3':
        key=int(input("Enter key to delete (Integer Only):"))
        t.deletKey(key)
    elif ch=='4':
        t.display()
    elif ch=='5':
        flg=False
        print("Exit ...")
    else:print("Invalid Input...")
