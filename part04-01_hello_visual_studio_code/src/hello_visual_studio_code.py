

while True:
    string = input("Editor: ")
    string = string.lower()
    if string == "visual studio code":
        print("an excellent choice!")
        break
    elif string == "word" or string == 'notepad':
        print('awful')
    elif string == 'emacs' or string == 'atom' or string == 'vim':
        print('not good')