def number_to_word(n):  #Creat a function name
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"
    elif n == 20:
        return "twenty"
    else:
        return None 

# user input here
word = input("Give me a string to provide the black hole numbar: ")

#calculate length user name
length = len(word)
print(f"{word} has {length} letters.")
#While loop 
while True:
    word_form = number_to_word(length)

    if word_form is None:
        print(f"Sorry! Number '{length}' is not supported in this version.")
        break

    next_length = len(word_form)
    print(f"{word_form.capitalize()} has {next_length} letters.")

    if next_length == 4:
        print("Four has 4 letters.")
        print("And 4 is the black hole number!!")
        break
    else:
        length = next_length