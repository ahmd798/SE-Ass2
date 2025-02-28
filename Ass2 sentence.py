def word_frequency(sentence):
    words = sentence.split()  
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1  
    return frequency
sentence = "apple orange banana apple orange apple"
print(word_frequency(sentence))