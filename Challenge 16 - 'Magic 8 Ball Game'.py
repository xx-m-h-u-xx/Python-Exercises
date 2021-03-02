#Challenge 16 - Magic 8 Ball#



import random
 
answer1 = ("Obviously")
answer2 = ("Your Kidding...")
answer3 = ("Try It Out!!!")
 
print("Welcome to the Magic 8 Ball Game - Use it to help answer any of your questions...")
question=input("Ask me for any advice and I’ll help you out! Type in your question and then press 'Enter' for an answer...”)
print("shaking.... \n" * 4)
 
choice = random.randint(1,3)
if choice == 1:
    answer = answer1
elif choice == 2:
    answer = answer2
else:
    answer = answer3
print(answer)
