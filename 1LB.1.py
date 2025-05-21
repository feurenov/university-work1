def word_count(text):
    words = text.lower().split()
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

text = "яблуко банан яблуко груша яблуко банан груша яблуко банан банан"
word_dict = word_count(text)
print("Словник:", word_dict)

frequent_words = [word for word, count in word_dict.items() if count > 3]
print("Слова, що зустрічаються більше 3 разів:", frequent_words)

