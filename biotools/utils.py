def count_words(seq, word_size):
    d = {}
    # Count occurrences of each word of length `word_size`
    for i in range(0, len(seq) - word_size + 1):
        word = seq[i : i + word_size]
        if word not in d:
            d[word] = {"count": 0, "percentage": 0}
        d[word]["count"] += 1

    # Calculate the total number of occurrences
    total_occurrences = sum(word_data["count"] for word_data in d.values())

    # Calculate and store the percentage for each word
    for word in d:
        d[word]["percentage"] = (d[word]["count"] / total_occurrences) * 100

    return d
