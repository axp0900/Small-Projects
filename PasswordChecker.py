password = input("Please enter a password: ")
numbersinpassword = 0
characters = 0
for i in password:
  if i.isdigit() == True:
    numbersinpassword += 1

for i in password:
  if i.isdigit() != True:
    characters += 1

x = True
while True:
  if (password[0].isnumeric() == True):
    print("First Character cannot be an integer")
    break
  if (len(password)<8):
    print("Your password must at least be 8 characters long")
    break
  if (len(password)>18):
    print("Your password is too long")
    break
  if ((numbersinpassword >= 2) != True):
    print("Your password must contain at least 2 numbers")
    break
  else:
    x = False
    print("It is a valid password. Thank you. Here are some details of password: ")
    print("The total length of your password is:", len(password))
    print("Your password", password, "has", numbersinpassword, "integers." )
    print("Your password", password, "has", characters, "characters")
    break

if (x == True):
  print("Not a valid password please try again.")
  

#(len(re.sub("\D", "", password))) >= 2









 
