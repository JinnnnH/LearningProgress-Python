"""
My practice file on my Python journey

******Self-taught******

"""

print("hello wordl")                                                            #a simple hello world
print("Python", end= ", ")                                                      #"end=" make the next print statement follow the current
                                                                                #print statment before moving to the next line on output
print("hi")                                                                     
print("Data Sciecne") 

s = "I love you"
print(s)                                                                        #output: I love you
print(s.replace("I", "He"))                                                     #replace "I" with "He", output: He love you
print(s)                                                                        #output: I love you
print(s.split('o'))                                                             #split the str when 'o' is found, output: ['I l', 've y', 'u']

s = "hahahahhahaha"
print("Why are you laughing %s" %(s))                                           #Both statements mean the same
print("Why are you laughing", s)

a = 123                                                                         #"a" is an int, let z be the length of "a"
print ("The character printed(including spaces) is 1 %d" %a)                    #"%d" expects an integer as variable
print ("The character printed(including spaces) is 1 %1d" %a)                   #%yd means print (y-z) spaces before the int. If y < the length of "a"
                                                                                #prints the whole "a". output: "123"
print ("The character printed(including spaces) is 2 %2d" %a)                   
print ("The character printed(including spaces) is 3 %3d" %a)
print ("The character printed(including spaces) is 4 %4d" %a)                   #since "a" has a length of 3 and 3 < 4, so (4-3), which is 1, extra space
                                                                                #would be printed. output: " 123" 
print ("The character printed(including spaces) is 5 %5d" %a)
print ("The character printed(including spaces) is 6 %6d" %a)
print ("The character printed(including spaces) is 7 %7d" %a)
print ("The character printed(including spaces) is 8 %8d" %a)

b = 345.678                                                                     #b is a double (float), let z be the length of "b"
print("floating number is %f" %b)                                               #"%b" expects a double as variable
print("floating number is %1.0f" %b)                                            #"y.xf" means print (y-b) spaces before the double with x decimals. output: 345
print("floating number is %1.5f" %b)                                            #since 345.678 only has 3 decimals, extra decimals would be printed
                                                                                # as "0". output: "345.67800"
print("floating number is %1.2f" %b)
print("floating number is %1.7f" %b)
print("floating number is %2.0f" %b)
print("floating number is %10.1f" %b)
print("floating number is %10.5f" %b)                                           #output: " 345.67800"

c = "asdsgsfdhsgafsdaafdsfgf"
print("object 1: {a}, object 2: {b}, object: {c}".format(a=a, b=b, c=c))        #a nicer way of outputting.
                                                                                #output: "object 1: 123, object 2: 345.678, object: asdsgsfdhsgafsdaafdsfgf"


i = input("Please input an integer: ")                                          #i is a string 
print(i)                                     

ii = i+i                                                                        #ii is still a string as i is a sting
print(ii)                                                                       #ii gives a "i+i" string in stead of i*2 in integer form

i = int(input("Please input an integer: "))                                     #i is an int
print(i)                                     

ii = i+i                                                                        #ii is an integer as i is int
print(ii)                                                                       #ii gives a "i+i" string in stead of i*2 in integer form