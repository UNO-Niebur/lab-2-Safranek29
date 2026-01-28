#Magic8Ball.py
#Name: Louis Safranek
#Date: 01/28/2026
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers=["yes","no","Maybe","potentially","Perhaps","I'm too busy ignoring you to answer you","ask again later","please go away"]
  #Prompt the user for their question.
  question=input("Ask a question")
  #Answer question randomly with one of the options from your earlier list.
  response=random.choice(answers)
  print(response)

if __name__ == '__main__':
  main()
