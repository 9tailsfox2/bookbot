from stats import word_count
from stats import characters
from stats import character_sort
def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
	return text

def main():
	text = get_book_text("books/frankenstein.txt")
	num_words = word_count(text)
	char_counts = characters(text)
	sorted_chars = character_sort(char_counts)
	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at books/frankenstein.txt...")
	print ("----------- Word Count ----------")
	print (f"Found {num_words} total words")
	print ("--------- Character Count -------")

	for char_dict in sorted_chars:
		char = char_dict["char"]
		count = char_dict["num"]
		if char.isalpha():
			print (f"{char}: {count}")
	print ("============= END ===============")

main()
