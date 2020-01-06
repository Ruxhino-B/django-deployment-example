import one
print('Top level two.py')
one.func()

if __name__ == '__main__':
    print('two.py being rn directly')
else:
    print('two is being imported')
