s = 'django'
print(s[0]) #d
print(s[-1]) #o
print(s[:5]) #djang
print(s[1:4]) #jan
print(s[-2:]) #go

# print(s[::-1]) #ognajd
#
l = [3,7,[1,4,'hello']]
# #ndrysho hello ne "goodbye"
l[2][2] = 'goodbye'
print(l)

#kap hello nga dictionaries:
d1 = {'simple_key':'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

#Perdor set per te gjetur vlerat unike
mylist = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
print(set(mylist))

#String ushtrime
age = 4
name = 'sammy'

print("Hello my dog's name is {name} and he is {age} years old".format(age=age,name=name))
