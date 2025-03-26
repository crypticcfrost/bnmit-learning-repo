import time
import os
print("This is an example python program")
time.sleep(2)
print("We are going to print numbers from 0-10 every 3 seconds to demonstrate runtime . . .")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 11):
    time.sleep(1)
    print(i)
print("Program ending, clearing terminal now . . .")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

print("We can also make the terminal seem fast moving and cool by shortening the delay . . .")
time.sleep(4)
print("\n\n\n\n")
print("Ready?")
time.sleep(2)
arr = ["Permission denied? Challenge accepted.", "Decrypting payload...", "404: Ethics Not Found", "sudo rm -rf /world", "Brute forcing into system framework.."]
for elements in arr:
    time.sleep(0.5)
    print(elements)

print("Looks cool doesn't it? Now we're gonna clear the terminal again.")
time.sleep(4)
