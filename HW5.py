#1-1: pwd
#1-2: ls
#1-3: cd brianna_repo, gti pull origin master
#1-4: mv homework.py ../python_decal/judy_decal/homework/
#1-5: cd ../python_decal/judy_decal/homework/, cat.py
#1-6: nano homework.py
#1-7: git add ., git commit -m "hello", git push origin master
#1-8: git stash, git pull, Judy made changes her remote repository and didn't pull them before editing her local repository
#1-9: cd ~/recents/

#2.1 
def checkDataType(data):
    return type(data)

#2.2
num = int(input("Enter a number: "))
def evenOrOdd():
    if (num % 2) == 0:
        print("{0} in Even".format(num))
    else:
        print("{0} is Odd".format(num))

#3
numbers = [1, 2, 3, 4, 5]
def sumWithLoops(numbers):
    for number in numbers:
        total += number
    return total

#4.1 - need help, can't quite figure out...
og_list = 'a','b','c'
def duplicatelist([og_list]):
    for i in og_list:
        og_list.append([i, i]) # append? google says extand works too but it's not working when I run it in jupyter
    return og_list

#4.2
def square(num):
    num = num * num
    return num

