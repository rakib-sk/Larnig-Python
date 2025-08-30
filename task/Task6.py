word = input("Enter a word or some numbar : ") #input numbar or a word

word_lower = word.lower() #convart to lower casw
char_list = list(word_lower)#casting list
reversed_list = char_list[::-1] #reverse word or numbat
#
#Logic part
if char_list == reversed_list:
    print(f"Yes! The word '{word}' is a palindrome.")
else:
    print(f"No, The word '{word}' is not a palindrome.")