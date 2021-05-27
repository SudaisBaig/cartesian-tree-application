from queue import Queue
from priority_queue import PriorityQueue

# This file contains two Major classes

# class Node: -> This class the defines the attributes of a Node 
# some of these attributes are general tree attributes and below them are attributes related to application  
# so basically each node represents a country (based on Data)

# class CartesianTree: -> This class constructs the Cartesian Tree 
# it reads the array (covidDataNodes) and makes a node of each sub array (1 country) and then arranges the array in a fashion
# to make a tree (binary) (maintaining the max heap struture)
# in order to do so it uses multiple functions such as 
# addNode -> creates a node and adds it to tree
# findmaxNode-> to find the correct position to put the Node in the Cartesian Tree 

# This class also contains function of Priority Queue. This function takes the root node of cartesian Tree and makes a 
# sorted array.           

class Node:
    def __init__(self,country,confirmed,deaths,recovered,active,region,incidentRate,fatality):
        self.value = 0
        self.left = None
        self.right = None
        self.parent = None

        self.country = country
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered
        self.active = active
        self.region = region
        self.incidentRate = incidentRate
        self.fatalityRatio = fatality


class CartesianTree:

    def __init__(self, arr, index):
        
        self.root= Node(None,None,None,None,None,None,None,None)
        self.last = Node(None,None,None,None,None,None,None,None)
        self.root = None
        self.last = None

        for row in arr:
            self.addNode(row,index)

    def __findMaxNode(self, node:Node, x) -> Node:
       
        if float(node.value) > float(x):
            return node
        elif node.parent != None:
            return self.__findMaxNode(node.parent, x)
        else:
            return None

    def getRoot(self) -> Node:
        return self.root

    def addNode(self, row, index):
        
        new_Node = Node(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
     
        
        new_Node.value = row[index]
        if self.root == None:
            self.last = new_Node
            self.root = new_Node
            return

        max_Node = self.__findMaxNode(self.last, row[index])

        if max_Node == None:
            new_Node.left = self.root
            self.root.parent = new_Node
            self.root = new_Node

        else:
            new_Node.left = max_Node.right
            max_Node.right = new_Node
            new_Node.parent = max_Node
            

        self.last = new_Node
      

    def InorderTraversal(self, node:Node, lst):
        if node == None:
            return 
        
        self.InorderTraversal(node.left, lst)
        print(node.value , end = " ")
        self.InorderTraversal(node.right, lst)

    def priorityQueue(self, is_max, top):
        pq = PriorityQueue()
        #print(pq.isEmpty())

        sortedList = []
        temp = Node(None,None,None,None,None,None,None,None)
        pq.insert(self.root)
        while not pq.isEmpty():
            temp = pq.delete()
            sortedList.append(temp)
            if temp.left != None:
                pq.insert(temp.left)
            if temp.right != None:
                pq.insert(temp.right)
        
        if is_max == False: 
            sortedList = sortedList[::-1]
        sub_sortedlist = []
        for i in range(top):
            sub_sortedlist.append(sortedList[i])
        return sub_sortedlist
              


# # print(tree.InorderTraversal(tree.getRoot(), lst))




        







       