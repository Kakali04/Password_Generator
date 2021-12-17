#Password Generator Project
import support
import random
letters= support.letters
numbers= support.numbers
symbols=support.symbols
def main():



    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password? "))
    nr_symbols = int(input("How many symbols would you like? "))
    nr_numbers = int(input("How many numbers would you like? "))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    list1=''
    for i in range (1,nr_letters+1):
        i=random.choice(letters)
        list1 +=i
    for j in range (1,nr_numbers+1):
        j=random.choice(numbers)
        list1 +=j
    for k in range (1,nr_symbols+1):
        k=random.choice(symbols)
        list1 +=k
    #print(list1)
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    #to randomly chosing any integer , strings or any varriables we use random.choice
    password=[]
    for c in range (1,nr_letters+1):
        password.append(random.choice(letters))

    for l in range(1,nr_symbols+1):
        password.append(random.choice(symbols))

    for m in range(1,nr_numbers+1):
        password.append(random.choice(numbers))
    print(password)
    #without shuffling the list
    New_password1 = ''
    for r in password:
        New_password1 +=r
    print(New_password1)
    #To chosse any value from a list we use random.shuffle
    random.shuffle(password)

    print(password)

    New_password=''
    for q in password:
        New_password +=q
    print(New_password)

if __name__ =="__main__":
    main()



