text = input("Type your text here : ")

#using strip() function to check empty input
if text.strip()=='':
    print("Invalid input.\nWord count : 0")

else:
    #using split() function to create a list of words from the given string 
    words = text.strip().split()

    count = len(words)
    print(f'Word count : {count}')