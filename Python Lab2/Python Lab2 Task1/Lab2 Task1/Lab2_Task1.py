#This program combines dictionaries and calculate avergae mark

s1 = {"amy": 75, "bobby": 62, "david": 50}                                                  #given dictionaries
s2 = {"helen": 80, "joseph": 72, "stephen": 66}

sd = {**s1, **s2}                                                                           #combined s1 and s2 into sd

sum = sd["amy"] + sd["bobby"] + sd["david"] + sd["helen"] + sd["joseph"] + sd["stephen"]    #sum = sum of every number in sd
average = sum/len(sd)                                                                       #len(sd) == 6
print(average)                                                                              #print average mark, which is 67.5