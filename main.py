def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
	return text

def word_count(text):
	words_list = len(text.split())
	return words_list

def main():
	text = get_book_text("books/frankenstein.txt")
	num_words = word_count(text)
	print(f"{num_words} words found in the document")
main()
