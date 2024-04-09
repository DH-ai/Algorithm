class Node():
    def __init__(self,data) :
        self.data = data
        self.next  = None

    # def __repr__(self) -> str:
    #     return f"Data:{self.data}, Next:({self.next})"




# added a node
def add(data,head):
    new_node = Node(data=data)
    if head==None:
        head = new_node
        head.next = None
    else:   
        new_node.next=head
        head = new_node
    return head

#remove a node 
def rem(data,head):
    current = head
    while(data!=current.data):
        prev = current
        current = current.next
        
        if (data==current.data):
            prev.next=current.next
            break
        
        
        if (head.next==None):
            print("Unable to find the element")
            break
    
    
#Insert a element
def ins(data,pos,head):
    new_node = Node(data)
    
    current = head
    i =1
    while (current.next!=None and pos!=0):
       
        if (i==pos-1):
            temp = current.next
            current.next = new_node
            new_node.next = temp
            break
        else:
            current = current.next

            i+=1
        


def printList(head):
   
    current = head
    
    while (current!=None):
        print("current: " ,current , "current.next: ",current.next, "current.data: ",current.data, end="\n")
        
        current = current.next
   
              


    

def ui():
    print("\nWhat function you want to perform.")
    print("\t1. ADD to linkedlist")
    print("\t2. REMOVE from LinkedList")
    print("\t3. INSERT LinkedList")
    print("\t4. PRINT LinkedList")
    print("\t5. QUIT")
    

option = -1
head =None
while (option !=5):
    ui()
    option = int(input(""))
    if (option>=1 and option<=5):
        if option == 1:
            print("Data to add into the linked list")
            data = int(input(""))
            head = add(data,head)

        elif option == 2:
            
            print("Which no. to remove")
            data = int(input(""))
            rem(data,head)

            

        elif option == 3:
            print("Which no. to insert")
            data = int(input(""))
            pos= int(input("Position:"))
            ins(data,pos,head)

        elif option == 4:
            
            printList(head)
        
               