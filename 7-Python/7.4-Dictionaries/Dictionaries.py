my_stuff = {'key1':'value1','key2':'value2'}
(my_stuff['key1'])
my_stuff2 = {'key1':'value1','key2':'value2','key3':123,'key4':{'key4.1':'me gjej','key4.2':[1,2,3,'me gjej prap']}}
#dua te printoj fjalen me gjej
(my_stuff2['key4']['key4.2'][3])

my_stuff3 = {'lunch':'pizza','bfast':'eggs'}
my_stuff3['lunch'] = 'hamburger' #Sintaksa per te ndryshuar fjalorin
print(my_stuff3['lunch'])
my_stuff3['darka'] = 'kos' #kjo eshte sintaksa per te shtuar dicka te re ne fjalor
print(my_stuff3['darka'])
