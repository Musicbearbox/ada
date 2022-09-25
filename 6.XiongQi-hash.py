#here i gonna perform chaining method 
#assignment: linear probing

from ast import Delete
from multiprocessing.connection import answer_challenge
from operator import truediv
from re import M
from turtle import Turtle


class HashTable:
    def __init__(self,m) -> None:
        self.m = m
        self.hashtable = self.create_hash_table()
        print(self.hashtable)

    def create_hash_table(self):
        return [ [] for _ in range(self.m)]

    def insert(self,key,value):
        key = self._prehash(key)

        bucket = self._hash(key)

        found ,pos_dup,_ = self.search(key)

        #if the key is duplicate .update the value
        if(found):
            bucket[pos_dup][1] = value
        else:
            bucket.append([key,value])

        #if the key does not exist ,append

        #if  something is there already, append
        print(self.hashtable)

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
        bucket = self.hashtable[index]
        return bucket
        
    def search(self,key):
        key = self._prehash(key)
        bucket = self._hash(key)

        found = False
        answer = -9999
        pos_dup = -9999
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                found = True
                pos_dup = i
                answer = bucket[i][1]
                break
            
        return found, pos_dup ,answer

    def delete(self,key):
        key = self._prehash(key)
        bucket = self._hash(key)
        found,pos_dup,_ = self.search(key)
        if found:
            print(bucket[pos_dup])
            del(bucket[pos_dup])
        print(self.hashtable)
    
        


tb = HashTable(11)
tb.insert(1,'chaky')
tb.insert(2,'peter')
tb.insert(2,'ptersons')
tb.insert(2,'jimmy')
tb.insert(3,'john')
tb.insert(12,'Mathew')
tb.delete(1)
