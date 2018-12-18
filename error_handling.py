#TRY AND EXCEPT STATEMENTS

def cats(num):
    try:
        if int(num)>10:
            print("That is a lot of cats")
        else:
            print('You do not have that many cats')
    except: 
        print("There is some error, I don't know what it is, I am just a machine")

print('Enter number of cats')
no=input()
cats(no)



