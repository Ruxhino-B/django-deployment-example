try:
    f = open('text.txt','w')
    f.write('Ttest write to simple text!')
except IoError:
    print('Error: Courld not find file or read Data!')
else:
    print("success!")
    f.close()
