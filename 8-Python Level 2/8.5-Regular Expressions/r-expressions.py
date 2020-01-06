# import re
# patterns = ['term1','term2']
# text = 'this is a string with term1, and not the other!'
# for pattern in patterns:
#     print("i'm searching for: "+pattern)
#     if re.search(pattern,text):
#         print('Match!')
#     else:
#         print("No Match")

# import re
# split_term = '@'
# email = 'user@gmail.com'
# print(re.split(split_term,email))

# import re
# print(re.findall('match','test phrease match in middle'))

import re
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')
test_pharse = 'This is a string! But is has punctuation. How can we remove it?'
test_patterns = ['[A-Z]+']
multi_re_find(test_patterns,test_pharse)
