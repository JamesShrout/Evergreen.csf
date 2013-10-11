# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test
a=0
x=1
while (x<= hw2_test.n):
    a=a+x
    x=x+1
print a

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

y=10
c=1

while (c<= y):
    c=c+1
    print 1/float(c)
    
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range (1 ,(n +1)):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n* (n + 1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n=10
s=1
for j in range (1 ,(n + 1)):
    s = s * j
print s


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
s=1
for j in range (1 ,(n + 1)):
    s = s * j
for i in range (numlines,0 , -1):
    print s
    s= s/i
    

       



###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

for c in range (1,11):
    f = 1
    for d in range (1, c+1):
        f = f * d
        print f


###
### Collaboration
###

I had help from my tudor brice and kahea the tudor for class, I also used the python book


###
### Reflection
###

# ...This assignment took three hours to complete and an hour reading
# ... I used the tutorials and did the reading
# ... the lecture did not contain everything I needed I felt the speaking was to fast and I did not remember discussing range

