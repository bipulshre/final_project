#queue is empty at the beginning

Queue={'front':None,'back':None}

#using node to keep track of elements
#in an queue which is represented by linked list

class Node:
    def __init__(self,data,next):
        self.data= data
        self.next=next


#adding elements to queue

def Enqueue(Queue,element):
    N=Node(element,None)
    if Queue['back']==None:
        Queue['front']=N
        Queue['back']=N
    else:
        Queue['back'].next=N
        Queue['back']=Queue['back'].next

#removing element from the queue

def Dequeue(Queue):
    if Queue['front']!=None:
        first=Queue['front']
        Queue['front']=Queue['front'].next
        return first.data
    else:
        if Queue['back']!=None:
            Queue['back']=None
            return 'cannot dequeue because the queue is empty'

Enqueue(Queue,'bipul')
Enqueue(Queue,'ribik')
Enqueue(Queue,'anjit')
print(Dequeue(Queue))
print(Dequeue(Queue))
print(Dequeue(Queue))
print(Dequeue(Queue))
