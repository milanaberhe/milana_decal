#HW4 so sorry it's a million yrs late mb chat

#2.1
im_so_sorry_this_is_so_late = list(range(21)):
print(im_so_sorry_this_is_so_late) #forgot to put parenthesis at first whoops

#2.2
this_is_totally_on_time = im_so_sorry_this_is_so_late 
def squareList(im_so_sorry_this_is_so_late):
    squared_numbers = [x**2 for x in im_so_sorry_this_is_so_late]
    return squared_numbers
im_so_sorry_this_is_so_late = list(range(21))
squared_numbers = squareList(im_so_sorry_this_is_so_late)

#2.4
your_dogs_ears = squareList(list)
def first_fifteen_elements(your_dogs_ears): #forgot a colon here
    return your_dogs_ears[:15]
#2.4
unicorn_tail = squareList(list)
def every_fifth_element(unicorn_tail):
    every_5th = unicorn_tail[::5]
    return every_5th

#2.5
sippy_cup = squareList(list)
def fancy_function(sippy_cup):
    sliced_list = sippy_cup[-3:]
    every_3rd = [::3]
    return every_3rd[::-1]

#3.1
numbers = []
for i in range(1,25):
    other = []
    for j in range(1,6):
        other.append(j)
    numbers.append(other)
    for k in range(6,11):
        other.append(k)
    numbers.append(k)
    for l in range(11,16):
        other.append(k)
    for m in range(16,21):
        other.append(m)
    for n in range(21,26):
        other.append(n)