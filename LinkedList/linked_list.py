class Node():
    def __init__(self,data) :
        self.data = data
        self.next  = None

    # def __repr__(self) -> str:
    #     return f"Data:{self.data}, Next:({self.next})"




def add(data,head):
    new_node = Node(data=data)
    if head==None:
        head = new_node
        head.next = None
    else:
        new_node.next=head
        head = new_node
    return head

def printList(head):
   
    current = head
    print(current)
    while (current!=None):
        print(current.data , "->",end=" ")
        
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
            print(head)
            # print("Which no. to remove")
            # data = int(" ")

            

        elif option == 3:
            print("Which no. to insert")
            print("dsa")

        elif option == 4:
            
            printList(head)
        elif option == 5:
            print("dsa")
               