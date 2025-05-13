from stats import word_count
from stats import characters
def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
	return text

def main():
	text = get_book_text("books/frankenstein.txt")
	num_words = word_count(text)
	print (f"{num_words} words found in the document")
	print (characters(text))
main()
