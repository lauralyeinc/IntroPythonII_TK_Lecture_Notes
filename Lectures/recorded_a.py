'''
REVIEW 

functions, spacing, important features how varibles work. 
framework upder problem solving tool kit

03_modules
collection of code where you can create bunch of functions that are used together

sys.argv  can add [1] [344] arguments after 

print out sys.argv 
read input from files or command line 
for arg in sys.argv:     # for one per line 
    print(arg)
OR
print(sys.argv)


print out the os platform 
print(sys.platform)

print of verison of python using
print(sys.version)

import os 

print(os.getpid())

print(os.pgetcwd())

print(os.getlogin())

07_slices
a = [2, 4, 1, 7, 9, 6]
print(a[2])
print(a[4])  OR print(a[len(a)-2]) same as print(a[-2])

:  slicing operator print(a[ start  : stop ])
starting left to right |  right to left - 

print(a[3:]) OR print(a[-3])
print(a[2:4]) left side is inclusive right is NOT inclusive, will not end at place you want, go right one more time. 
print(a[1:])
print(a[:4]) OR print(a[:-1])


s = "hello, world!" 
print(s[7:12])

08_comprehensions
x = input("Enter comma-separated numbers: ").split(',')
print(x)

y = [ # int(var) for var in some_list if int(var) % 2 == 0 ]
'''

'''
function.py 

def double_func(x):  <--- : starting a new block, then four spaces 
    return 

def = define a function with a name 
js function double(x) {} OR  const double = () => {}
hello_world = _ under_case or snake_case 
'''

def mult2(x):    # x passed by value  made a copy and using a different x 
    return x * 2

y = mult2(12)
print(y)
# √√ 

# define a doubling function for a list of variables passed by reference 
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
    # return l 
'''
we passed reference l, <-- "a pointer" to the list, we are modifing the list directly and don't have to return it to use it outside of the scope of the function mult2_list

pass by reference cup = ☕️  fillcup(☕️)  <-- same cup being used within the method fillcup. Changing it's value/index as you use it. 

^^^^^ it works that way because of memory.  memory = ram. 

simple variables get passed by value -int -str -boolens 
complex variables 

'''

some_nums = [1, 2, 3, 4]
print(some_nums)
mult2_list(some_nums)
print(some_nums)