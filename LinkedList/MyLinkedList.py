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
        Sel = self.HEAD;
        while(not(Sel.Next == 0)):
            X = Sel.Next
            while (not(X == 0)):
                if  (Sel.Value > X.Value):
                    Temp = X.Value;
                    X.Value = Sel.Value
                    Sel.Value = Temp
                X = X.Next
            Sel = Sel.Next        
            
    def SortDESC(self):
        Sel = self.HEAD;
        while(not(Sel.Next == 0)):
            X = Sel.Next
            while (not(X == 0)):
                if  (Sel.Value < X.Value):
                    Temp = X.Value;
                    X.Value = Sel.Value
                    Sel.Value = Temp
                X = X.Next
            Sel = Sel.Next

    def CutNode(Node):
        if not(bool(Node.Previous) or bool(Node.Next)):
            return Node
        if not(bool(Node.Previous)):
            Node.Next.Previous = 0
            Node.Next = 0
            return Node
        if not(bool(Node.Next)):
            Node.Previous.Next = 0
            Node.Previous = 0
            return Node
        if (bool(Node.Next) and bool(Node.Previous)):
            Node.Previous.Next = Node.Next
            Node.Next.Previous = Node.Previous
            Node.Next = 0
            Node.Previous = 0
            return Node
        
    def InsertNodeAfter(Node,Target):
        if bool(Target.Next):
            Temp = Target.Next
            Target.Next = Node
            Node.Previous = Target
            Node.Next = Temp
            Temp.Previous = Node
        
    def SelectSort(self):
        HeadOSort = self.HEAD;
        while bool(HeadOSort.Next):
            Sel = HeadOSort.Next;
            if (HeadOSort.Value <= Sel.Value ):
                HeadOSort = Sel
            elif (self.HEAD.Value > Sel.Value):
                LinkedList.CutNode(Sel)
                self.HEAD.Previous = Sel
                Sel.Next = self.HEAD
                self.HEAD = Sel
            else:
                Sorted = HeadOSort
                while (Sorted.Value>Sel.Value):
                    Sorted = Sorted.Previous
                LinkedList.CutNode(Sel)
                LinkedList.InsertNodeAfter(Sel,Sorted)

    def DeleteAt(self, Index):
        if(Index == 0):
            self.HEAD = self.HEAD.Next;
            return True
        
        Targ = self.HEAD
        I = 0
        while (I < Index and bool(Targ)):
            I += 1
            Targ = Targ.Next
        if (bool(Targ)):
            if (Targ == self.TAIL):
                self.TAIL = self.TAIL.Previous
                self.TAIL.Next = 0
                return False
            Targ.Previous.Next = Targ.Next
            Targ.Next.Previous = Targ.Previous
            return True
        return False

    def Delete(self,Value):
        if (self.HEAD.Value == Value):
            self.HEAD = self.HEAD.Next
            return True
        if (self.TAIL.Value == Value):
            self.TAIL = self.TAIL.Previous
            self.TAIL.Next = 0
            return True
        
        Targ = self.HEAD
        bFound = False
        while (not(Targ.Value == Value)):
            Targ = Targ.Next
        bFound = Targ.Value == Value
        if (bFound):
            Targ.Previous.Next = Targ.Next
            Targ.Next.Previous = Targ.Previous
        return bFound
    
Thing = LinkedList()
Thing.AddValue(8)
Thing.AddValue(1)
Thing.AddValue(9)
Thing.AddValue(4)
Thing.AddValue(3)
Thing.AddValue(5)
Thing.AddValue(7)
Thing.AddValue(9)
Thing.AddValue(6)

print(Thing.toString())
Thing.SelectSort()
print(Thing.toString())
