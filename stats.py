def word_count(text):
        words_list = len(text.split())
        return words_list
def characters(text):
	character_dict = {}
	for every_character in text:
		every_character = every_character.lower()
		if every_character not in character_dict:
			character_dict[every_character] = 1
		else:
			character_dict[every_character] += 1
	return character_dict
