import random
# Define a list of riddles and their corresponding answers with clues
riddles = [
("I'm not alive, but I can grow. I don't have lungs, but I need air. What am I?", "fire", "It's a natural phenomenon associated with combustion."),
("The more you take, the more you leave behind. What am I?", "footsteps", "Think about what gets left behind when you walk."),
("I'm a word of letters three, add two and fewer there will be. What am I?", "few", "The word becomes shorter when you add two letters."),
("I am always hungry, I must always be fed. The finger I touch will soon turn red. What am I?", "fire", "I'm a source of heat that can cause burns."),
]
# Define a function to generate a random Caesar cipher def generate_caesar_cipher():
shift = random.randint(1, 25)
return shift
# Define a function to encrypt a message using a Caesar cipher def encrypt_caesar_cipher(message, shift):
encrypted_message = ""
for char in message: if char.isalpha():
if char.islower():
shifted = ord(char) + shift if shifted > ord('z'):
shifted -= 26 encrypted_message += chr(shifted)
elif char.isupper():
shifted = ord(char) + shift if shifted > ord('Z'):
shifted -= 26 encrypted_message += chr(shifted)
else:
encrypted_message += char
return encrypted_message
def main():
print("Welcome to the Cipher Riddle Challenge!")
print("Solve the cipher to uncover the secret riddle.")
print("You can ask for a clue if you're stuck. Type 'clue' for a hint
or 'skip' to skip a riddle.\n")
while True:
# Select a random riddle and its answer riddle, answer, clue = random.choice(riddles)
# Generate a random Caesar cipher shift = generate_caesar_cipher()
# Encrypt the riddle using the Caesar cipher encrypted_riddle = encrypt_caesar_cipher(riddle, shift)
print("Here's your cipher:") print(encrypted_riddle)
attempts = 0 max_attempts = 3
while attempts < max_attempts:
guess = input("Enter the deciphered riddle, 'clue' for a hint,
or 'skip' to skip: ").lower()
if guess == answer:
print("Congratulations! You solved the riddle.") break
elif guess == 'skip':
print("The answer was: ", answer) break
elif guess == 'clue':
attempts += 1
print("Here's your clue: " + clue)
else:
attempts += 1
print("Sorry, that's not correct.")
if attempts == max_attempts:
print("Out of attempts. The answer was: ", answer)
play_again = input("Play again? (yes/no): ").lower() if play_again != "yes":
break
print("Thank you for playing the Cipher Riddle Challenge!")
if __name__ == "__main__": main()
