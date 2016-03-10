'''
Travis Rowe
3/10/16
This program creates a balanced binary search tree after the user inputs the
number of integers to put into the tree (note the tree will only be completely
balanced if the number of integers in the tree is 2^n-1, where n is an integer)
'''

import random

class BalancedSearchTree(object):
    def __init__(self,size=2):
        self.tree = [-1 for x in range(size)]
        self.size = size
        self.root = 1
        self.items = 0
    
    
    def insert(self,val):
        # If list (tree) is empty, put value at root
        if self.tree[self.root] == -1:
            self.tree[self.root] = val
        # loop until you find the location to insert
        # even if you have to extend this list
        else:
            i = self.root
            loop = True
            while loop:
                if val > self.tree[i]:
                    i = self.rightChild(i)
                else:
                    i = self.leftChild(i)
                
                if i >= self.size:
                    self.extend()
                
                if self.tree[i] == -1:
                    self.tree[i] = val
                    self.items += 1
                    loop = False

    '''
    @Name: insertList
    @Description:
        Receives a list of unordered integers and recursively inserts them into the binary tree in such a manner that the resulting tree is balanced.
    @Params:
        values (List) - unordered list of integers
    @Returns: None
    '''
    def insertList(self,list):
        
        list.sort()   #sorts the list which will be put into the tree
        if len(list) > 0:
            med = int(len(list)/2)  #sets med at the index of the median element of list

            self.insert(list[med])  #inserts the current median value into the tree
            if self.items+1 == uniqueLength:
                print(self.tree)

        else:
            return

        if not med == 0:   #If there is more than one element in this iteration of the list
            self.insertList(list[0:med]) #Passes the first half of the list into insertList (leftChild)
            self.insertList(list[med+1:len(list)]) #Passes the second half of the list into insertList (rightChild)

        

    def extend(self):
        temp = [-1 for x in range(self.size)]
        self.tree.extend(temp)
        self.size *= 2
        #print(self.items)
        
    def find(self,key):
    
        self.comparisons = 1

        if key == self.tree[self.root]:
            return True
        else:
            i = self.root
            while True:
                if key < self.tree[i]:
                    i = self.leftChild(i)
                else:
                    i = self.rightChild(i)
                    
                if i >= self.size:
                    return False
                
                if self.tree[i] == -1:
                    return False   
                    
                if self.tree[i] == key:
                    return True
                    
                self.comparisons += 1
                
                
    def leftChild(self,i):
        return 2 * i
        
    def rightChild(self,i):
        return 2 * i + 1
     
random.seed(342345)
bs = BalancedSearchTree()

uniqueLength = int(float(input('Number to insert: (1-100000) ')))
unique = []
while len(unique) < uniqueLength:   #Creates an unsorted list with uniqueLength number of unique integers
    r = random.randint(0,99999)
    if r not in unique:
        unique.append(r)

bs.insertList(unique)

"""
random.seed(342345)
bs = BinarySearchTree(4096)
for x in range(1000):
    bs.insert(random.randint(0,99999))

if __name__ == '__main__':
    
    print(bs)
"""