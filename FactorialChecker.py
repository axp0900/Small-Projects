'''
main.py
'''
import math
import sys
import code
  
code.factorial(3,0)

'''
code.py
'''
import math
import sys


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def factorial(attempt, tries):
  while (tries != 3):
    integer = (input("Please enter a positive integer to compute for factorial: "))

    

    if (integer.isalpha() == True) or (integer == "") or (isfloat(integer) == True) and ((float(integer).is_integer()) != True):
      print("Sorry no strings or floats")
      attempt -= 1
      tries += 1
      print("This was attempt #" + str(tries)+" you have", attempt, "attempts left" )
      if attempt == 0:
        print("Sorry you've exhausted all of your attempts")
        sys.exit("Terminating program. BYE BYE!")

    
    elif (int(integer) <= 0):
      print("Please enter a positive integer greater than zero")
      attempt -= 1
      tries += 1
      print("This was attempt #" + str(tries)+" you have", attempt, "attempts left" )
      if attempt == 0:
        print("Sorry you've exhausted all of your attempts")
        sys.exit("Terminating program. BYE BYE!")
      
  
    

    else:
      print("The factorial of", integer, "is:",math.factorial(int(integer)))
      attempt -= 1
      tries += 1
      print("This was attempt #" + str(tries)+" you have", attempt, "attempts left" )
      if attempt == 0:
        print("Sorry you've exhausted all of your attempts")
        sys.exit("Terminating program. BYE BYE!")
  
  
    
