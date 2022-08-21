# Importing the random module
import random

# Asking the basic questions to get the information we need
name=input("What is your name? ")
question=input("What is your question? ")
answer=""

# Generating a random integer
random_number=random.randint(1,9)

# Checking what is the random number and accordingly decide the respone
if random_number==1:
  answer="Yes - definitely."
elif random_number==2:
  answer="It is decidedly so."
elif random_number==3:
  answer="Without a doubt."
elif random_number==4:
  answer="Reply hazy, try again."
elif random_number==5:
  answer="Ask again later."
elif random_number==6:
  answer="Better not tell you now."
elif random_number==7:
  answer="My sources say no."
elif random_number==8:
  answer="Outlook not so good."
elif random_number==9:
  answer="Very doubtful."
else:
  answer="Error"

# Printing out the information
print(name+" asks:",question)
print("Magic 8-Balls answer:",answer)
