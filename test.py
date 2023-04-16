s = 'hello'
count = 0
for char in s:
    if char.isalpha(): # check if the character is a letter
        count += 1
        print(count)