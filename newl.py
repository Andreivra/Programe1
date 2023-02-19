dicx ={'nume':'na', 'prenume':'pa','tel':78}

text_1 = ''

for key, value in dicx.items():
    #print(key, value)
    text_1 += f'{key} is = {value}\n'

print(text_1)