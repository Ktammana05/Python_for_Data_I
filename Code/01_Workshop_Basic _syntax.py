
# defining a function

#define lasagna():
#    mince garlic
#    cut tomato
#lasagna()#oversimplified recipe, will not result in actual lasagna

def ux():
    print "Here is a function that listing out printing techniques."
    print 'Single quotes work too!'
    print "I'd  'use' double quotes to encapsulate 'single' quotes in your prints."
    print (''' Sometimes you need to include more detail when that is the case
           you can use parentheses and triple quotes in order to print 
           multiple lines''')
ux()

# Exercise How did you get here today?


### Commenting
'''
You should comment before each new section of code and can even comment line 
by line. Aside from that whenever you have a breakthrough comment instructions
on what you did for your future self to remember. Write your comment as though
someone who does not read code would understand what the code is doing from 
your comment. 
'''
# Typically, you just use the # (pound) sign to comment out everything that 
# follows it on that line.

print("Not a comment")
#print("Am a comment")


# Multiple line comments are slightly different. Simply use 3 single quotes before and after the part you want commented.

'''
print("We are in a comment")
print ("We are still in a comment")
'''
print("We are out of the comment") # learning about comments


# Exercise
''' Take the code you created from the functions exercise copy and paste it 
below and then put comments in the code to help you understand what you did 
6 months from now'''

# Matthew made us do this super awesome exercise
''' this is how I got here today
just playing around'''


def ux(): # def is how you start to defin a function
    print "Here is a function that listing out printing techniques."
    print 'Single quotes work too!'
    print "I'd  'use' double quotes to encapsulate 'single' quotes in your prints."
    print 'OK "maybe"  one more'
ux()

# STRINGS
''' If you have ever done any amount of working with SQL or EXCEL you will be 
familiar with the need to review and manipulate strings.
If you have not these basic concepts may come in handy 
in the future. '''



# creating
a = 'hello'     # can use single or double quotes

# slicing
a[0]        # returns 'h' (works like list slicing)

# slicing
a[1:3]      # returns 'el'

# slicing
a[-3]       # returns 'o'

# concatenating concats are the same as Excel or SQL you can concat blanks or multiple columns
a + ' there'        # use plus sign to combine strings

# concatenating ()
str(5) + ' there'   # cast 5 to a string in order for this to work

# uppercasing
a.upper()       # string method (this method doesn't exist for lists)

# upper casing 
a[0].upper()+a[1:] #Uppercase of first letter in word

# checking length
len(a)      # returns 5 (number of characters)

''' EXERCISE
Create a function called proper, write your first name in all lowercase into Variable 'first' and your last 
name into variable 'last' Combine your name together with upper case for first 
letter of your first name and upper case for first letter of your last name 
ie Terry Smith'''



# Basic Math
''' Part of any programming or analytics is basic math. 
We will now combine math functions and print functions. '''

print "I will now do some math:"

print "basic math", 1 + 9/ 2
print "basic math",  10/ 3
print "modelo", 10 % 3
print "division with dec", 10.0 /3.0

print "What about order of operations?"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print (3 + 2 + 1) - (5 + 4 % 2) - 1 / (4 + 6)

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "Example of printing and Math"
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print (3 ** 4) # 3 to the fourth power

print 'basic boolean', 3<7
print 'basic boolean', 3>7
print 'basic boolean', 1+2<7



# Exercise Basic Math functions
# Create your own basic math function  mixing text and the math problem maybe 
# one from work or a budget you are working on.


# Create a boolean function that brings back the text of what you are testing 
# and has an answer of False and 1 that has an answer of True



#### Variables and Math
'''  A variable is a container to hold a value
# X = 10
# X is a variable that now holds the number 10
# I can say X+1 and get 11
X = 100	
Y = 72	
Z = 14	
	(X-Y)+Z = ? '''
 
 
 
 
 
 
#VARIABLES
departments = 100
headcount_by_dept = 15
managers = 92
employees = 1498

# notice how you can concatinate strings with variables
print "There are", departments, " departments in our company"
print "There are only", managers," managers available"
 

# Finish the code EXERCISE
# Lets add some math in our variables with the above code

#VARIABLES
departments = 100
headcount_by_dept = 15
managers = 92
employees = 1498
managers_needed = departments
total_headcount = (departments * headcount_by_dept)+ managers_needed

# total_headcount minus (managers plus employees)
total_headcount_available= 

# employee divided by department

avg_employee_per_dept = 

# Create a print statement that tells you how many managers are needed, what 
# the total headcount is, the headcount 
# available and the average employee per department.


''' EXERCISE
Initial Markup (IMU) is the difference between the cost and selling price of 
an item when it is first introduced for sale. It is also called Initial Mark On, 
Markon or Markup. The formula for this calculation is: 
Selling price – cost = Initial Markup Dollars. 
If a buyer brings in a line of jeans with a cost of 25 per pair and initially 
prices them to sell at 55 per pair, the Initial Markup is 30. 
*Create an IMU calculator'''



''' PROJECT EXERCISE 
Create a function that lists all the skills you have learned so far
rate yourself for each skill

0 = Don't know
1 = Aquiring knowledge
2 = Can apply with 80% help from Google
3 = Can apply with 20% help from Google
4 = Can teach <20% help from Google
5 = Can design, review, optimize

What is your average score?
What areas are you doing great in, what areas do you need to study?

This Project will grow and be designed and redesigned several different ways
as you progress and revist.'''
