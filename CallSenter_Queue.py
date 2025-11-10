from collections import deque
class CallSenter_Queue:

    def __init__(self):
        self.call_Queue=deque()

    def addCall(self,callId,callTime):
        self.call_Queue.append((callId,callTime))
        print(f"Call :{callId} With Call Time :{callTime} is Added To Queue...")
    
    def answerCall(self):
        if self.isQueueEmpty():
            print(f"No CAll To Answer...")
            return
        call=self.call_Queue.popleft()
        print(f"Call {call[0]} with tine :{call[1]} is proceed...")

    def viewCall(self):
        if self.isQueueEmpty():
            print("No Call's Are Available...")
            return
        print("All Available Call's :")
        for i in self.call_Queue:
            print(f"Call :{i[0]} And Time :{i[1]}")
    
    def isQueueEmpty(self):
        return len(self.call_Queue)==0
    
c=CallSenter_Queue()
flg=True
while flg:
    print("\t\tWelcome")
    print("1--> Add Call")
    print("2--> Answer Call")
    print("3--> View Calls")
    print("4--> check Call Queue Is Empty ")
    print("5--> Exit")

    ch=input("Enter The Choice :")
    if ch=='1':
        callId=input("Enter The Call Id :")
        callTime=input("Enter The Call Time :")
        c.addCall(callId,callTime)

    elif ch=='2':c.answerCall()
    elif ch=='3':c.viewCall()
    elif ch=='4':
        if c.isQueueEmpty():
            print("Queue IS Empty")
        else: print("Queue Is Not Empty")
    elif ch=='5':
        flg=False
        print("Exit...")
    else:print("Invalid input...Try Again.")