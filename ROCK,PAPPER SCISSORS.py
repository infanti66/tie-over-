




import random 

youDict = {"R": 1, "P": -1, "S": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}

system = random.choice([1, 0, -1])
print("Game begins now!")

youstr = input("Enter your choice(r,p,s) :").upper()

# ✅ Check if input is valid
if youstr not in youDict:
    print("❌ Invalid input! Please choose R, P, or S.")
else:
    you = youDict[youstr]   # 'you' is always defined safely

    print(f"You chose {reverseDict[you]} \nSystem chose {reverseDict[system]}")

    if system == you:
        print("⚔️  Both warriors struck at the same time!! Draw 🎭")
    elif (system == 1 and you == 0):
        print("☠️ Defeat... but legends rise again!...")
    elif (system == 1 and you == -1):
        print("🚀💥 Ultra Instinct Activated!! You WIN 🔥⚔️...")
    elif (system == -1 and you == 0):
        print("🏆 YOU CRUSHED THE SYSTEM! ⚡...")
    elif (system == -1 and you == 1):
        print(" 💣 System laughed at your weakness… GAME OVER!...")
    elif (system == 0 and you == 1):
        print("🐧 you winnnnn...")
    elif (system == 0 and you == -1):
        print("🤦‍♀️u lost this round...")
    else:
        print("🏆 You win! Warrior spirit lives on!")
