class undo_redo_stack:
    document=""
    undo_stack=[]
    redo_stack=[]

    def __init__(self):
       self.document=""
       self.undo_stack=[]
       self.redo_stack=[]

    def add_data(self,document):
        self.undo_stack.append(self.document)
        self.document+=document
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("no data to undo")
            return
        self.redo_stack.append(self.document)
        self.document=self.undo_stack.pop()
    def redo(self):
        if not self.redo_stack:
            print("no data to redo")
            return
        self.undo_stack.append(self.document)
        self.document=self.redo_stack.pop()
    def show(self):
        print("\n📄 Current Document Data:")
        print(self.document if self.document else "(empty document)")

    
#main function
d=undo_redo_stack()
flg=True
while flg:
    print("\n===== TEXT EDITOR MENU =====")
    print("1. Add Text")
    print("2. Undo")
    print("3. Redo")
    print("4. Show Current Text")
    print("5. Exit")
    try:
        ch = int(input("Enter the choice: "))
    except ValueError:
        ch = 1  # default to 1 if non-numeric input

    if ch not in [1, 2, 3, 4, 5]:
        print("Invalid input! Defaulting to Add Text (1).")
        ch = 1
    if ch==1:
        text=input("Enter data to add :")
        d.add_data(text)
        d.show()
    elif ch==2:
        d.undo()
        d.show()
    elif ch==3:
        d.redo()
        d.show()
    elif ch==4:
        d.show()
    elif ch==5:
        print("exit\n Thank you")
        flg=False
    else:print("invalid input") 