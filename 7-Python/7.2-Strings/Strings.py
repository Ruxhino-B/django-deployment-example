#Basic
'hello' #string mund te jete me thojza teke ose si me poshte me thojza dyshe
"Hello"

"I'am a profesional programer" #nqs duam te fusim ne thojza dicka krijojme si fillim thojza dyshe dhe brenda tyre fusim thojza teke

Indexing
mystring = 'abcdefg'
print(mystring[0]) #Shkronja e pare
print(mystring[-1]) #Shkronja e fundit

Slicing
mystring = 'abcdefg'
print(mystring[2:]) #Kapelementet nga indeksi 2 e mbrapa
print(mystring[4:]) #Kap elementet nga indeksi 4 e mbrapa. ne rastin tone kap elementin efg
print(mystring[:3]) #Kap elementet nga 0 deri te 3shi pa e perfshire 3shin. do me thenee abcdefg
print(mystring[2:5]) #kap elemetet nga 2shi duke e perfshire 2shin deri te 5sa pa e perfshire 5sen me pak fjale cde
print(mystring[::]) #kap gjithcka nga fillimi deri ne fund
print(mystring[::2]) #kap elemetet nga fillimi duke i kaluar me nga 2 o me thene aceg
# mystring[0] = 'x' # nuk funksionon sepse stringu eshte i pa ndryshueshem drejtprdrejt

Metodat Bazike
mystring = 'abcdefg'
x = mystring.upper() #te gjitha shkronjat qe jan brenda i ben me shkronja kapitale
print(x)
y = mystring.lower() #e kudnerta e upper qe i zmadhon eshte lower qe i zvogelon
print(y)
mystring = 'Hello World'
x = mystring.split() #Ben ndarjen ne liste te elementeve te cilat jan ndare nga nje hapsire
print(x)
y = mystring.split('o') #Ben ndarjen ne liste duke mare ne konsiderate shkronjen "o" dhe jo hapsipern boshe
print(y)

#Print Formating
x = "Fut nje shtring tjeter ketu: {}".format("Une Futem!")
print(x)
y = "Item One: {} Item Two {}".format("dog","cat")
print (y)
z = "Item One: {y} Item Two {x}".format(x="dog",y="cat") #keshtu i vendos sipas deshires elementet
print (z)
