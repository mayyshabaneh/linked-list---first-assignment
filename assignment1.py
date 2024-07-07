class Node:
    def __init__(self , value) :
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def display_List(self):
        current_node = self.head
        print("Linked list is:")
        while current_node:
            print(current_node.value, end=" ---> ")
            current_node = current_node.next
        print("None")  


    def add_First_Node(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node



    def add_Last_Node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_At_Index(self, index, value):
        if index == 0:
            self.add_First_Node(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for _ in range(index - 1):
                if current_node is None:
                    return
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        

    def add_Values(self, value):
        new_node = Node(value)
        current_node = self.head
        if self.head is None or self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
            return
        while current_node.next and current_node.next.value < value:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
            



    def delete_First(self):
        if self.head is None:
            print("Your linked list is empty")
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node


    def delete_Last(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        elif self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node
        else:
            current_node = self.head
            prev = None
            while current_node.next:
                prev = current_node
                current_node = current_node.next
            prev.next = None
            deleted_node = current_node
            return deleted_node
        

    def delete_At_Index(self, index):
        if index == 0:
            return self.delete_First()
        else:
            current_node = self.head
            for _ in range(index - 1):
                if current_node is None or current_node.next is None:
                    return
                current_node = current_node.next
            deleted_node = current_node.next
            if current_node.next.next:
                current_node.next = current_node.next.next
            else:
                current_node.next = None
            return deleted_node

    

    def count_Item(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    

    def remove_duplicates(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node:
            temp = current_node
            while temp.next:
                if temp.next.value == current_node.value:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            current_node = current_node.next


    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def merge_Lists(self, ll1, ll2):
        merged_ll = LinkedList()
        current1 = ll1.head
        current2 = ll2.head
        while current1:
            merged_ll.add_Values(current1.value)
            current1 = current1.next
        while current2:
            merged_ll.add_Values(current2.value)
            current2 = current2.next
        return merged_ll

    def merge_Sorted(self, ll1, ll2):
        merged_ll = LinkedList()
        current1 = ll1.head
        current2 = ll2.head
        while current1 and current2:
            if current1.value < current2.value:
                merged_ll.add_Last_Node(current1.value)
                current1 = current1.next
            else:
                merged_ll.add_Last_Node(current2.value)
                current2 = current2.next
        while current1:
            merged_ll.add_Last_Node(current1.value)
            current1 = current1.next
        while current2:
            merged_ll.add_Last_Node(current2.value)
            current2 = current2.next
        return merged_ll
            

    def split_Halves(self):
        length = self.count_Item()
        if length < 2:
            return None, None
        mid = length // 2
        count = 0
        current_node = self.head
        first_half = LinkedList()
        second_half = LinkedList()
        while current_node:
            if count < mid:
                first_half.add_Last_Node(current_node.value)
            else:
                second_half.add_Last_Node(current_node.value)
            current_node = current_node.next
            count += 1
        return first_half, second_half



    def reduce_List(self):
        sum = 0
        current_node = self.head
        while current_node:
            sum += current_node.value
            current_node = current_node.next
        return sum


    def return_Index(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                index += 1
                current = current.next



    def print_Asterisk(self):
        current_node = self.head
        while current_node:
            for _ in range(current_node.value):
                print("*", end="")
            print("\n")
            current_node = current_node.next                


      
