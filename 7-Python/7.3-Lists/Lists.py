#Lists
mylist=[1,2,3]
mylist = ['stringsdhfshdf',1,2,33,4.3,True,[2,4,4]]
print(mylist)
print(len(mylist)) #kjo jep gjatesine e listes
#Lista mund te indeksohet njesoj si steing
#lista ndryshe nga string mund te ndryshohen elementet e listes
mylist[0]='liste e re'
print(mylist)
mylist.append('Item i ri') #.append eshte menyra se si futet nje element i ri ne nje liste
print(mylist)
mylist.append([1,2,3]) #Shton nje liste brena liste
mylist.extend([1,2,3]) #shton elemente brenda liste por jo si liste por si element liste
mylist.pop() #heq elementin e fundit nga lista
mylist.pop(0) #heq elementin e pare nga lista
mylist.reverse() #kthen elementet mbrabsh ne menyre reverse
mylist.sort() #kthen nga me e vogla te me e madhja
mylist=[1,2,['x','y','z']]
print(mylist[2][1]) #printon elementin y qe eshte te lista e dyte. keshtu behet inkesimi
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [0][0] #kap elementine pare te listes se pare. pra kap elementin 1
LIST COMPREHENSION
first_col = [row[0] for row in matrix] #kap elementet e para te cdo liste 1,4,7
print(first_col)
