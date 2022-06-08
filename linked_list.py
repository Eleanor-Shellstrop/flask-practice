class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


# wrapper to keep tabs on head of list
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

#           Node2                             Node1
# _______________________            ________________________
# |                     |            |                      |
# |  Data    |  Node1   |--------->  |  Data    |   *       |----> None
# |                     |            |                      |
# _______________________            ________________________