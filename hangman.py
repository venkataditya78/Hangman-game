from words import words
import random
import string

def valid_word(words):

	word = random.choice(words)

	while '-' in word or ' ' in word:
		word = random.choice(words)

	return word.upper()


def hangman():

	word = valid_word(words)
	used_letter = set()
	alphabet = set(string.ascii_uppercase)
	word_letter = set(word)
	lives = 6
	while( len(word_letter) > 0 and lives > 0):

		print("You have ",lives,"left and have used these letters",''.join(used_letter))

		word_sofar = [letter if letter in used_letter else '-' for letter in word]
		print("Current word is: ",''.join(word_sofar))

		user_letter = input("Guess a letter? ").upper()

		if user_letter in alphabet - used_letter:
			used_letter.add(user_letter)

			if user_letter in word_letter:
				word_letter.remove(user_letter)
				print('')
			else:
				lives = lives - 1
				print("The letter ",user_letter,"is not in the word and you have", lives," lives left.")

		elif user_letter in used_letter:
			print("You have already used this letter!!")
		else:
			print("Please enter an alphabet")
	if lives == 0:
		print("You died loser. The word was ",word)
	else:
		print('YAY! You guessed the word', word, '!!')
	
if __name__ == '__main__':
    hangman()



