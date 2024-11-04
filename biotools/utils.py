def count_words(seq, word_size):
    d = {}
    for i in range(0, len(seq) - word_size + 1):
        word = seq[i:i + word_size]
        if word not in d:
            d[word] = 0
        d[word] += 1
    return d