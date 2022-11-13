from collections import Counter

#every node object will have two children, otherwise is a leave
class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def getChild(self):
        return self.left, self.right

def get_code(node, code = ''):
    
    if type(node) is str:
        #stop!!!
        return {node : code}
    
    #get the children
    left, right = node.getChild()
    
    #recursive function
    huffman_code = dict()
    huffman_code.update(get_code(left, code+'0'))
    huffman_code.update(get_code(right, code+'1'))
    
    return huffman_code

def decode(message,code):
    original = ''
    key_temp = ''
    key_value = code.items()
    for s in message:
        key_temp = key_temp + s
        for each in key_value: 
            if (key_temp == each[1]):
                original = original + each[0]
                key_temp = ''
                break
    return original

def calculateTotalCost(message,code):
    key_values = code.items()
    totalCost = 0
    totalCost = totalCost + len(message)
    for each in key_values:
        totalCost = totalCost + len(each[0])*8
        totalCost = totalCost + len(each[1])
    return totalCost

def make_the_tree(freqs_sorted):
    
    #as long as freqs_sorted.length > 1
    while len(freqs_sorted) > 1:
        
        #combine the two smallest one
        key1, value1 =  freqs_sorted[0]
        key2, value2 =  freqs_sorted[1]
        
        #delete them
        freqs_sorted = freqs_sorted[2:]
        
        #add the new combination to freqs_sorted
        new_value = value1 + value2
        new_node  = Node(key1, key2)
        
        #add to freqs_sorted
        freqs_sorted.append((new_node, new_value))
                
        #sort again!!
        freqs_sorted = sorted(freqs_sorted, key=lambda item: item[1])
        
    return freqs_sorted[0][0]
    #return root node (so we can use this generating coding....)

#input
message = 'AAABBBBBBEEEDABEEDCC'


#count the letters
#use Counter, then convert to dictionary
freqs = dict(Counter(message)) #{'A': 4, 'B': 7, 'E': 5, 'D': 2, 'C': 2}
# print(freqs['A'])  #4

#sort them from smallest to biggest
#{'C': 2, 'D': 2, 'A': 4, 'E': 5, 'A': 7}
freqs_sorted = sorted(freqs.items(), key=lambda item: item[1])

#make the tree by combining the smallest one, and delete those guys
root = make_the_tree(freqs_sorted)

#get the code
huffman_code = get_code(root)

#print the code
print(huffman_code)
#{'A': '01'; 'B': '11'; 'C': '000'; 'D': '001'; 'E': '10'}

def encoding(code):
    afterEncoding = ''
    for s in message:
        afterEncoding = afterEncoding + code[s]
    
    # allKeys = code.keys()
    # for key in allKeys:
    #     afterEncoding = afterEncoding + key + code[key]

    return afterEncoding

newMessage = encoding(huffman_code)
print(newMessage)

#task1: decode the encoded message to the original message
# original_message = decode(huffman_code)

original_message = decode(newMessage,huffman_code)
print(original_message)

#task2: calculate the total cost --> message + table
print(calculateTotalCost(newMessage,huffman_code))
