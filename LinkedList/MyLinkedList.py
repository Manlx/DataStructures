class LinkedList:
    class Node:
        Value =0
        Next =0
        Previous =0
        def __init__(self,Value):
            print("Created Node")
            self.Value = Value
    
    HEAD = 0;
    TAIL = 0;
    def __init__(self):
        print("Created LinkedList")
    def AddValue(self,Value):
        if not(self.HEAD):
            self.HEAD = LinkedList.Node(Value)
            self.TAIL = self.HEAD
        else:
            Temp = LinkedList.Node(Value)
            self.TAIL.Next = Temp
            Temp.Previous = self.TAIL
            self.TAIL = Temp
            
    def GetValueAt(self,Value):
        Index = 0
        Temp = self.HEAD
        while (Index < Value and bool(Temp)):
            Temp = Temp.Next
            Index += 1
        if (Index == Value):
            return Temp.Value
        else:
            return 0;
        
    def toString(self):
        Temp = self.HEAD
        sOut = ""
        while (bool(Temp)):
            sOut += f'{Temp.Value};'
            Temp = Temp.Next
        return sOut;
    
    def toStringBack(self):
        Temp = self.TAIL
        sOut = ""
        while (bool(Temp)):
            sOut += f'{Temp.Value};'
            Temp = Temp.Previous
        return sOut;
    
    def Contains(self,Value):
        Temp = self.HEAD;
        bLooking = True
        while(bLooking and bool(Temp)):
            bLooking = not(Temp.Value == Value)
            if (bLooking):
                Temp = Temp.Next
        return not(bLooking)
    
    def SortASC(self):
        Start = self.HEAD
        while(not(Start == self.TAIL )):
            Iter = Start    
            if (Iter.Value > Iter.Next.Value):
                Temp = Iter.Value
                Iter.Value = Iter.Next.Value
                Iter.Next.Value = Temp
            Start = Start.Next
            
    def SortDESC(self):
        print()
        
Thing = LinkedList()
Thing.AddValue(1)
Thing.AddValue(2)
Thing.AddValue(3)
Thing.AddValue(4)
Thing.AddValue(5)
Thing.AddValue(8)
Thing.AddValue(7)
Thing.AddValue(6)
print(str(Thing.GetValueAt(0)))
print(Thing.toString())
print(Thing.toStringBack())
print(Thing.Contains(6))
print(Thing.Contains(5))

print(Thing.SortASC())
print(Thing.toString())
