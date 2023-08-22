def constant_value(string):
    #container to store our vowels
    vowel = ("aeiou")
    current_value = 0
    max_value = 0
    #use the for loop to iterate through the code
    for char in string:
        if char not in vowel:
            current_value += ord(char) - ord('a') + 1
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    max_value = max(max_value, current_value)
    
    return max_value
print(constant_value("zodiac"))


