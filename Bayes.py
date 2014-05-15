# My Bayes solutions to problems from Udacity's Intro to Statistics: https://www.udacity.com/course/st101

#Function 1
#Goal: Calculate the probability of a positive result given that
#p0=P(C)
#p1=P(Positive|C)
#p2=P(Negative|Not C)

def f1(p0,p1,p2):
    return (1-p0)*(1-p2) + p0*p1

print f1(.3,.6,.2)
    
#Function 2
#Goal: Return the probability of A conditioned on B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 

def f2(p0,p1,p2):
#Insert your code here
    return (p0*p1)/((p0*p1) + (1-p0) * (1-p2))

print f2(.3,.4,.5)

#Function 3
#Goal: Return the probability of A conditioned on Not B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 

def f3(p0,p1,p2):
    return p0*(1-p1)/(p0*(1-p1)+(1-p0)*p2)

print f3(.3,.4,.7)
