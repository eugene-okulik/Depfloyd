texts = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

words = texts.split()
marks = '.,'
modified_words = []


for word in words:
    punctuation = ''
    core = ''
    
    for char in word:
        if char in marks:
            punctuation += char
        else:
            core += char

    new_word = core + 'ing' + punctuation
    modified_words.append(new_word)

result = ' '.join(modified_words)
print(result)
