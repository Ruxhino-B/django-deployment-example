# mylist = [1,2,3]
# mylist.append() # append eshte nje metode. me oop do mesojme te krijojme metodat tona

# class Dog():
#     #CLASS OBJECT ATTRIBUTE
#     special = 'gjitare' #cfardolloj qeni te jete ai eshte gjitar pavarsisht emrit/lloji
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog(breed='Lab',name='Puvi')
# print(mydog.breed) #eshte atribut e jo metode
# print(mydog.name)


# class Circle():
#     pi = 3.14
#     def __init__(self,radius=1):
#         self.radius = radius
#     def area(self):
#         return self.radius*self.radius*Circle.pi
#     def set_radius(self,new_r): #kjo eshte nje metode se si te ndryshosh radius
#         self.radius = new_r
# myc= Circle(3)
# myc.set_radius(10) #kjo eshte menyra e thirrjes
# print(myc.area())


#INHIRITANCE
# class Animial():
#     def __init__(self):
#         print('Animal Created')
#     def whoAmI(self):
#         print('Animal')
#     def eat(self):
#         print("EATING")
# class Dog(Animial): #keshtu trashegohen atributet e klases
#     def __init__(self):
#         Animial.__init__(self)
#         print("Dog Created")
# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()

#CPECIAL METHODS
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {} , Author:{}, Pages:{}".format(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("Book is deletet")

b = Book("Python","Jose",200)
print(b)
