#Guest name
def get_guess():
    return input('What is your guess')

x=get_guess()
print(x)
#Generojme 3 nr nga kompjuteri
def generate_code():
    digits = [str(num) for num in range(10)]
    #Shufle the digits
    random.shuffle(digits)
    #then grap the first three
    return digits[:3]

#Generate the clues
def denerate_clues(code,user_guess):
    if user_guess==code:
        return "Code Cracked"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('match')
        elif num in code:
            clues.append('Close')
    if clues = []:
        return ['nope']
    else:
        return clues
#run game logic
print("Wellcome Code Breaker")
secret_code = generate_code()
clue_report = []
while clue_report ! " code cracked!":
    guess = get_guess()
    clue report = generate_clues(guess,secret_code)
    print('')
