# #logical Operators
# (1 > 2) and (2<3)
#

if 1<2:
    print('yes')

if 3<4:
    if 4<2:
        print('yes')
    else:
        print('no way!!!')

#For Loops
seq = [1,2,4,5,6]
for ckemi in seq:
    print(ckemi)
for hej in seq:
    print('O SHOK')


d = {'sam':1,'Frenk':2,'Dan':3}
for item in d:
    print(item)
    print(d[item])

mypairs = [(1,2),(3,4),(5,6)] #ketu kemi tuples(te pa ndryshueshme) brenda nje liste
for cift in mypairs:
    print(cift) #printon elementet 2 nga dy

for (cift1,cift2) in mypairs: #ko quhet TUPLE UN PACKING
    print(cift1)
    print(cift2)


#WHILE LOOPS
i = 1
while i<5:
    print("i is: {}".format(i))
    i = i+1

for item in range(5):
    print(item)

x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)
#e njejta gje si me siper.
outof = [num**3 for num in x]
print(outof)
