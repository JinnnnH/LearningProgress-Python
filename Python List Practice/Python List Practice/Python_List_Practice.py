"""

***Python list practice***

"""

mylist = [1, 2, 3, "one", "two", "three"]
print(len(mylist))                                           #print length of mylist, in this case: 6
print(mylist)                                               #print all elements of mylist: [1, 2, 3, 'one', 'two', 'three']
print(mylist[0])                                            #print 0th element of mylist: 1
print(mylist[1])                                            #print 1st element of mylist: 2
print(mylist[1:])                                           #print 1 element of mylist, starting from the left hand side: 1
print(mylist[:5])                                           #print 1 element of mylist, starting from the right hand side
                                                            #output: [2, 3, 'one', 'two', 'three']

#adding new elements
mylist + ["new element"]                                    #add "new element" to list, but it's not permenant, 
                                                            #so mylist stays the same in the next print, [] is needed
print(mylist)                                               #[1, 2, 3, 'one', 'two', 'three']
print(mylist + ["new element"])                             #[1, 2, 3, 'one', 'two', 'three', 'new element']
mylist = mylist + ["permenant element"]                     #add "new element" to list permenantly
print(mylist)                                               #[1, 2, 3, 'one', 'two', 'three', 'permenant element']
mylist*2                                                    #duplicate mylist 2 once but still, not permenant
print(mylist)                                               #stays the same: [1, 2, 3, 'one', 'two', 'three', 'permenant element']
print(mylist*2)                                             #permenant, so: [1, 2, 3, 'one', 'two', 'three', 'permenant element', 1, 2, 3, 'one', 'two', 'three', 'permenant element']

