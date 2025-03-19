class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def enqueue(self, info):
       
        new_node = Node(info)     
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
       
        if self.front is None:
            return None
        removed_info = self.front.info
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed_info

    def peek(self):
      
        return None if self.front is None else self.front.info

    def is_empty(self):
      
        return self.front is None

    def get_size(self):
       
        return self.size

    def print_queue(self):
       
        print("********* QUEUE DUMP *********")
        print(f"Size: {self.size}")
        node = self.front
        index = 1
        while node:
            print(f"** Element {index}")
            print(node.info)
            node = node.next
            index += 1

class Order:
    def __init__(self, customer, qtty):
        self.customer = customer
        self.qtty = qtty
    
    def __str__(self):
        return f"  Customer: {self.customer}\n  Quantity: {self.qtty}\n  ------------"

if __name__ == "__main__":
    order_queue = Queue()
    order_queue.enqueue(Order("gato", 10))
    order_queue.enqueue(Order("perro", 25))
    order_queue.enqueue(Order("gusano", 15))
    order_queue.enqueue(Order("gallina", 40))
    order_queue.enqueue(Order("Elefante", 30))
    order_queue.enqueue(Order("raton", 50))
    order_queue.enqueue(Order("delfin", 20))
    order_queue.enqueue(Order("Hormniga", 35))
    order_queue.enqueue(Order("Iguano", 45))
    order_queue.enqueue(Order("J", 60))
    
    order_queue.print_queue()
