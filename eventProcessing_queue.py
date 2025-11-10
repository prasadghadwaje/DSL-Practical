from collections import deque
class EventProcessing:

    def __init__(self):
        self.eventQueue=deque()
    
    def addEvent(self,eventName):
        self.eventQueue.append(eventName)
        print(f"Event {eventName} is Successfuly Added To Queue ...")
    
    def processEvent(self):
        if not self.eventQueue:
            print("No Event To Proceed ...")
        else:
            event=self.eventQueue.popleft()
            print(f"Event {event} is Proceed ...")
    def showEvent(self):
        if not self.eventQueue:
            print(f"No Event Are Available...")
        else:
            print("All Pending Events :")
            for i in self.eventQueue:
                print(f"Event :{i}")
    
    def removeEvent(self,eventName):
        if not self.eventQueue:
            print(f"No Event to Remove...")
            return
        if eventName in self.eventQueue:
            self.eventQueue.remove(eventName)
            print(f"Event {eventName} is Remove From Queue...")

e=EventProcessing()
flg=True
while flg:
    print("\t\tWelcome")
    print("1--> Add Event")
    print("2--> Process Event ")
    print("3--> show All Pending Event's")
    print("4--> Cancle The Event")
    print("5--> Exit")
    ch=input("Enter the Choice: ")

    if ch=='1':
        eventName=input("Enter the Event Name :")
        e.addEvent(eventName)
    elif ch=='2':e.processEvent()
    elif ch=='3' : e.showEvent()
    elif ch=='4':
        eventName=input("Enter Event To Remove :")
        e.removeEvent(eventName)
    elif ch=='5' : 
        flg=False
        print("Exit , ThankYou...")
    else:
        print("Invalid Input...Try Again.")