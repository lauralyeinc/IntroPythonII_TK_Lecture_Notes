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
complex variables get passed by reference  -lists -dictoinaries -tupl -sets
-class objects 

list compherhenion is creating a new list (1)

'''

some_nums = [1, 2, 3, 4]
print(some_nums)
mult2_list(some_nums)
print(some_nums)


'''
UPER METHOD - important in interviews. interview problems are phrased into english words, up to us to break it down into the details. (state, numbers, rules)

U - understand the problem, ask tons of questions. constraits (ex: mobile, slow computers, or high power machines) (who what where   when) money, time, speed, resources, performance, parameters. What are my inputs and outputs?  - edge cases(source of most bugs) ( ex: large numbers) -what input will break the program? - off by one bugs  
    spend most of your time in this section to get out all ideas and questions
P - planning, pseudo code, MVP goal, Can you describe a MVP or brute force solution? Tinker and tailor it to a better solution if you have time. Have all the work laid out.  
E - excute - should be simple, use the pseuo code from Planning and set up the project in a clean organized way.  
R - reflect/repeat/refactor/run - if there's an error, start back at Understand and begin again. 

'''

''' 
problem example:centered_average
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, expect ignoring the largest and smallest values in the array.  If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average.  You may assume that the array is length 3 or more. 

Understand - lenght 3 or more. average = sum of all nums divided by the list minus 2 & ( in each list, minus the largest and smallest values.) int divison? (rounding the number) nerver have floats. //   no multible copies of the numbers in each array.  Are they presorted? Assume not sorted. 

Planning - pre sort to remove the min and max numbers. then take the average / sum of all numbers divided len(list). sorting is expensive. OR pop off the min and max numbers of each list. removing is expensive as well. or ignore using slices. 

def center_average(nums):
    max_num = max(nums)
    min_num = min(nums)
    current_sum = sum(nums)
    final_sum = current_sum - max - min
    return final_sum // (len(nums -2)
    # find max number of nums
    # find the min number
    # get the sum of nums
    # subtract the max and min
    # divide the value by len(nums) - 2

'''

def center_average(nums):
    max_num = max(nums)
    min_num = min(nums)
    current_sum = sum(nums)
    final_sum = current_sum - max_num - min_num
    return final_sum // (len(nums -2))

center_average([1, 2, 3, 4, 100]) 
center_average([1, 1, 5, 5, 10, 8, 7])
center_average([-10, -4, -2, -4, -2, 0])

'''
lines 135 to 144 there's an error. 
line 140, in center_average
    return final_sum // (len(nums -2))
TypeError: unsupported operand type(s) for -: 'list' and 'int'
'''