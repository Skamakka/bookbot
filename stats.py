def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    lower = text.lower()
    for char in lower:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_count(character_count):
    report = []
    for key in character_count:
        dictionary = {"char": key, "num": character_count[key]}
        report.append(dictionary)

    report.sort(reverse=True, key=sort_on)
    return report