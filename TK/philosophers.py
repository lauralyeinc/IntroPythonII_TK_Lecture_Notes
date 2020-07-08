# 3 implement 
# def feed_philosophers():
#     eating = [True, False, True, False, False]
#     i = 0
#     while i <len(eating):
#         if i == 0:
#             if eating[4]:
#                 eating[4] = False
#                 eating[i] = True
#         else: 
#             if eating[ i-1]
#                 eating[i-1] = False
#                 eating[i] = True 
#         i = (i+1) % 5 

''' [4] is the index of the 5th philosopher, the above pass is a never ending eating or thinking loop. The the philosophers are  inmoral. '''

# 4 relfecting 
''' 
linear data sturctures are not ideal for circular construct
    -> doubly linked list? circular linked list? 
could we generalize soultion to work with ANY number of philosophers?


# Polya's Problem Solving Techniques

1.Understand  2.Devise a Plan  3.Implement  4.Reflect 
'''