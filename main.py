import time
import os
print("This is an example python program")
time.sleep(3)
print("We are going to print numbers from 0-10 every 3 seconds to demonstrate runtime . . .")
os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 11):
    time.sleep(3)
    print(i)
print("End of program")
