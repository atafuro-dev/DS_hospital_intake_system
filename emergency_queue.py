class Patient:
    def __init__(self, name, urgency):
       self.name = name
       self.urgency = urgency


class MinHeap:
    def __init__ (self):
        self.data = [] #list of patients

    def heapify_up(self, index): #used after inserting a new patient
        while index > 0: 
            parent = (index -1) // 2

            if self.data[index].urgency < self.data[parent].urgency: #comparing urgencies
                self.data[index], self.data[parent] = ( #relating/comparing back to the parent 
                    self.data[parent],
                    self.data[index]
                )
                index = parent
            else: 
                break
    def heapify_down(self, index): #used after removing the root
        size = len(self.data)
        while True:
            smallest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if (left < size and self.data [left].urgency < self.data[smallest].urgency):
                smallest = left
            if (right < size and self.data[right].urgency < self.data[smallest].urgency):
                smallest = right
            if smallest != index:
                self.data[index], self.data[smallest] = (
                    self.data[smallest],
                    self.data[index]
                )  
                index = smallest
            else:
                break
    def insert (self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)
    def print_heap(self):
        for patient in self.data:
            print(f"Name: {patient.name}, Urgency: {patient.urgency}")
    def peek(self):
        if not self.data:
            return None
        return self.data[0] 
    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data [0]

        self.data[0] = self.data.pop() #moves last patient to the root  
        self.heapify_down(0)
        return root    
    
# Test your MinHeap class here including edge cases
#NORMAL TEST CASES
p1 = Patient("Riley", 2)
print(p1.name)       # Riley
print(p1.urgency)    # 2

heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency) # Taylor, 1 

served = heap.remove_min()
print(served.name) # Taylor
heap.print_heap()

#EDGE CASES
empty_heap = MinHeap()
print(empty_heap.peek())
print(empty_heap.remove_min())
#returns None



#DESIGN MEMO
# A tree for the doctor is an appropriate structure for its relation between data. You want the root to store information, as well as the left and right data stored along side it.
# A queue or heap would not make sense for the doctors, as it does for the patients. You are not queueing doctors, you want to access their information not their status or ugrency in this case. 
# A software engineer could use preorder, inorder, or postorder traversals based on the task at hand. Preorder is for when the root matters most, and inorder is when you want left to right evaluation. Postorder is when
# the children nodes must be handled prior to the parent nodes. 
# Heaps help simulate real-time systems like emergency room intake scenarios as they are simulating how a realistic queue system works. In this specific setting, the people with the highest urgency need to be helped first. It is 
# not the order in which they arrive or the time they've waited, but how urgently them must be seen. We can also see this in service ticket request systems as well. If there is an issue that leaves you unable to work - it must be handled first
# before a lower priority issue not preventing someone from working. A queue system is not always the order of arrival, sometimes there are prioritizations that must take place. 
