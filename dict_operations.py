def count_words_by_length(words):
  word_length_frequency = {}
  for word in words:
    word_length = len(word)
    if word_length not in word_length_frequency:
      word_length_frequency[word_length] = 1
    else:
        word_length_frequency[word_length] = word_length_frequency[word_length] + 1
  return word_length_frequency