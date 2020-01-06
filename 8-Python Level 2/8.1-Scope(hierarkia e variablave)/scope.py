# x = 25
# def my_func():
#     x = 50
#     return x
# print(x) #Ketu printohet 25 sepse eshte variabel global
# print(my_func()) #Ketu printohet 50 sepse merret x i funksionit
# my_func()
# print(x) #Ketu serisht printohet 25 edhe pse eshte thirrur my_func mesiper

#locals
#lambda x: x**2 #ky eshte nje varibel lokal
#eclosing function locals (funksione te bashkegjitur lokal)
# name = 'this is a global name!'
# def greet():
#     name = "Samy"
#     def hello():
#         print("hello " + name)
#     hello() #jo jep hello Samy. sepse jo kerkon nje shkalle me lart per vaiablin name
#             #nqs name brenda func greet fshihet at here hello kerkon nje shkalle
#             #me lart per variablin name dhe printon hello this is a global name!
# greet() #nuk publikon asgje sepse vetem sa i jep funksionit vleren Samy
# print(name) #kjo printon serisht This is a global name

#Billd in level jane funksione ose varibla qe i ka python vete psh len-->jep gjatsi
#len = 23 #kjo eshte gabim sepse nqs therasim len del 23 e jo me funksini me mat gjatsin

x = 50
def func(x):
    print('x is: ',x) #jep x is 50
    global x = 100 #ben ndryshimin e variablit global x
    x = 100
    print('x u be: ',x)#jep x u be 100
func(x)
print(x) #jep vleren 100 sepse x u ndryshu vlera global
