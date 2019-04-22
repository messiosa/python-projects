from sys import getsizeof

dict = {}

def function(x):
    
    i, list = 0, []
    
    while i < x:
        dict[len(list)] = getsizeof(list)
        list.append(i)
        i += 1
        
    for a, b in dict.items():
        print(a, b)
