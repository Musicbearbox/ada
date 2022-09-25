#here i gonna perform chaining method 
#assignment: linear probing

from ast import Delete
from multiprocessing.connection import answer_challenge
from operator import truediv
from re import M
from turtle import Turtle

class dot():
    taken = False
    key = -999
    value = -999
    deleted = False
    def __init__(self) -> None:
        pass
    def set(self,key,value):
        self.taken = True
        self.key = key
        self.value = value
    def delete(self):
        self.taken = False
        self.deleted = True

class HashTable:

    def __init__(self,m) -> None:
        self.m = m
        self.hashtable = self.create_hash_table()

    def create_hash_table(self):
        return [ dot() for _ in range(self.m)]

    def insert(self,key,value):
        key = self._prehash(key)
        found ,pos ,_ = self.search(key)

        #if pos==-9999, rebuild hashtable
        # if pos == -9999:
        #     oldTable = self.hashtable.copy()
        #     self.__init__(self.m*2)
        #     for i in range(oldTable.m):
        #         edot = oldTable.hashtable[i]
        #         if edot.taken == True:
        #             self.insert(edot.key,edot.value)
        #     found ,pos ,_ = self.search(key)
                    
        bucket = self.hashtable[pos]
        if(found):
            #if the key is existed .update the value
            bucket.value = value
        else:
            #if the key does not exist ,append
            bucket.set(key,value)

        #if  something is there already, append
        self.print()

    def _prehash(self,key):
        #chanllenge: handle negative keys and string
        if type(key) == str:
            key  = hash(key)  #return a number for you

        if (type(key) ==int) | (type(key) == float):
            if key<0 :
                key = hash(float(key)) * -1 #first convert to float, then hash it
            
        assert (key>0) & (type(key)==int)
        return key

    def _hash(self,key):
        #get the positition using division method
        index = key % self.m
        return index
        
    def search(self,key):
        index = self._hash(key)

        found = False
        answer = -9999
        pos = -9999

        for i in range(index,index+self.m,1):
            eDot = self.hashtable[i%self.m]
            #print("???")
            #print(eDot.key)
            #print(key)
            if eDot.key == key and eDot.taken == True:
                #print("found")
                #print(eDot.value)

                found = True
                pos = i%self.m
                answer = eDot.value
                break
            if eDot.deleted == False and eDot.taken == False:
                pos = i%self.m
                break  
        return found ,pos ,answer

    def delete(self,key):
        key = self._prehash(key)
        found,pos,_ = self.search(key)
        if found:
            bucket = self.hashtable[pos]
            
            bucket.delete()
        self.print()

    def print(self):
        for i in range(0,self.m):
            edot = self.hashtable[i]
            if edot.taken == True:
                print(edot.key,edot.value)
            else:
                print("[],[]")
        print("_____________")
    
        


tb = HashTable(11)
tb.insert(1,'chaky')
tb.insert(2,'peter')
tb.insert(2,'ptersons')
tb.insert(2,'jimmy')
tb.insert(3,'john')
tb.insert(12,'Mathew')
tb.insert(4,'jennifer')
tb.delete(1)
tb.insert(1,'chaky3')
tb.delete(1)