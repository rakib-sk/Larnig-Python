print("This is word game!! gase word")
word_list = set()
fast_word = input("Enter any name!: ")
sec_word = input("Enter agin any name!: ")
thard_word = input("Enter agin any name!: ")
last_word = input("Enter agin nay name!: ")

word_list.add(fast_word)
word_list.add(sec_word)
word_list.add(thard_word)
word_list.add(last_word)

gase_word = input("Enter the word what i remove!!: ")
remove_word = word_list.pop()
if gase_word == remove_word:
    print("You are Wine!!!",remove_word)

else:
    print("You are lose!! try agin", remove_word ,"is remove word")
    



