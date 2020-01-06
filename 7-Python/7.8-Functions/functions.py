# def my_func(param1='default'):
#     """
#     THIS IS THE DICSTRING KY ESHTE SJARIMI SE CA PERBEN KY FUNKSIONI
#     """
#     print('This is my first function in python in this time')
#

# def hello():
#     return 'hello'
#
# result = hello()
# print(result)

# def add_num(num1,num2):
#     return num1+num2
# result= add_num(1,2)
# print(result) #kjo nxjerr shumen e 1 dhe 2shit qe eshte e barabarte me 3
# result1 = add_num("3","5") #kjo nxjerr 35 pra i shikon te dy nr si string
# def add_num(num1,num2):
#     if type(num1) == type(num2):
#         return num1+num2
#     else:
#         print("Keto jane dy tipe te ndryshme inputesh. Ju lutem sigurohuni qe te jene te tjeta")
# var1 = add_num(2,"3")
# print(var1)

#LAMBDA EXPRESSION
#FILTER
# mylist = [1,2,3,4,5,6,7,8,]
# def even_bool(num):
#     return num%2 == 0
# even=filter(even_bool,mylist)
# print(list(even))
# even = filter(lambda num:num%2 == 0,mylist) #kjo eshte e njejta gje si me siper
# print(list(even))

#nqs duam te dim eshte apo jo dicka ne liste shkr
print('x' in [1,2,3,4]) #kjo eshte boolead dhe thot false nqs jo true nqs po
