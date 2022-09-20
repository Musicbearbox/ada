from tokenize import String
from xml.etree.ElementTree import tostring


class Node(object):

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    #print tree
    def printT(self):
        #print left
        #print right
        #print middle
        #hint:use recursive
        if(self.left):
            self.left.printT()
        print(self.key)
        #if self.parent:
        #    print(self.parent)
        if(self.right):
            self.right.printT()
        

    def insert(self,key):
        #if we already have a root node
        if(self.key):
            #hten check left and right
            #cond1: if less than :go left
            if(key<self.key):
                #condi1.1 if the left is nil, fill it
                if(self.left == None):
                    n = Node(key)
                    self.left = n
                    n.parent = self
                #cond1.2 if the left is not nil, recursive
                else:
                    self.left.insert(key)


            #cond2: if greater than : go right
            else:
                #cond2.1 if the right is nil, fill it
                if(self.right == None):
                    n = Node(key)
                    self.right = n
                    n.parent = self
                #cond2.2 if the right is not nil, recursive
                else:
                    self.right.insert(key)
        
        #if we don't have the root node
        else:
            #this key is the root node
            self.key = key

    def minimum(self):
        x = self
        while x.left != None:
            x = x.left
        return x

    def maxmum(self):
        x = self
        while x.right != None:
            x = x.right
        return x
    
    def treeSuccessor(self):
        # the node with the smallest key greater than x.key
        x = self
        if x.right != None:
            return x.right.minimum()
        y = x.parent
        while (y != None) and (x == y.right):
            x = y
            y = y.parent
        return y

    def search(self,k):
        if k == self.key:
            return self
        if k < self.key:
            return self.left.search(k)
        else:
            return self.right.search(k)

    def delete(self,z):
        #case 1
        if z.left == None:
            z.transplant(z.right)
        elif z.right == None:
            z.transplant(z.left)
        #case 2
        else:
            #case 4
            y = z.right.minimum()
            if y.parent != z:
                y.transplant(y.right)
                y.right = z.right
                y.right.parent = y
            #case 3
            z.transplant(y)
            y.left = z.left
            y.left.parent = y
        del(z) #destroy


    def transplant(self,v):
        p = self.parent
        #self.parent == None
        if p == None:
            pass
        elif self is p.left:
            p.left = v
            #print(p.left.key)
        else:
            #p.right is self
            p.right = v
            #print(p.right.key)
        if v != None:
            v.parent = p
        

root = Node(10)
root.insert(11)
root.insert(5)
root.insert(3)
root.insert(56)
root.insert(42)
root.insert(7)
root.insert(8)
root.insert(12)
root.insert(61)
root.insert(57)
root.insert(59)
root.printT()
#print(root.minimum().key)
#print(root.maxmum().key)

n = root.search(56)
print("-------------")
print(n.treeSuccessor().key)
print("-------------")
root.delete(n)
root.printT()