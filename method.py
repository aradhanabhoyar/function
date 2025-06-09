l = ["ravi",78,"purva",10.5,True]
l.remove(78)            #only remove the element which we give
print(l)
l.remove(l[3])                  
print(l)
l.remove(l[5])                 # list index out of range
print(l)                        
l.remove(l[1],"purva")         # one argument only
print(l)


#l.pop()
#print(l)
#l.pop(2)
#print(l)
#l.pop(4)               # index out of range
#print(l)
#l.pop(l[2],"purva")        # 1 argument
#print(l)

