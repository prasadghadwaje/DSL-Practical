class Hashing_linearProbing:

    def __init__(self,size=10):
        self.size=size
        self.table=[-1]*self.size
        self.DELETED=-2

    def hashFunction(self,key):
        return key%self.size
    
    def insertKey(self,key):
        index=self.hashFunction(key)
        for i in range(self.size):
            new_index=(index+i)%self.size
            if self.table[new_index] in (-1,self.DELETED):
                self.table[new_index]=key
                print(f"Key is inserted at index :{new_index}")
                return
        print(f"Hash table is Full no key can inserted further...")
     
    def searchKey(self,key):
        index=self.hashFunction(key)
        for i in range(self.size):
            new_index=(index+1)%self.size
            if self.table[new_index]==-1:
                print(f"Key {key} not Found in table")
                return
            if self.table[new_index]==key:
                print(f"Key {key} is found at index :{new_index}")
                return
        print(f"Key {key} not found!")

    def deleteKey(self,key):
        index=self.hashFunction(key)
        for i in range(self.size):
            new_index=(index+i)%self.size
            if self.table[new_index]==-1:
                print(f"Key {key} not found can not be delete/remve ...")
                return
            if self.table[new_index]==key:
                self.table[new_index]=self.DELETED
                print(f"Key {key} is deleted ...")
                return
        print(f"Key {key} not Found cannot be deleted")
    
    def displayTable(self):
        for i in range(self.size):
            print(f"Index [{i}] :{self.table[i]}")
        print()

t=Hashing_linearProbing()
flg=True
while flg:
    print("\nMENU:")
    print("1 → Insert Key")
    print("2 → Search Key")
    print("3 → Delete Key")
    print("4 → Display Table")
    print("5 → Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        key = int(input("Enter key to insert: "))
        t.insertKey(key)
    elif ch == '2':
        key = int(input("Enter key to search: "))
        t.searchKey(key)
    elif ch == '3':
        key = int(input("Enter key to delete: "))
        t.deleteKey(key)
    elif ch == '4':
        t.displayTable()
    elif ch == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")