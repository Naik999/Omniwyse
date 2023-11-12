file_name = "data.tst"

with open(file_name, 'rt') as new_file:
        words = new_file.read().lower().split()
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        total_words = sum(word_count.values())

        print(f"Total words: {total_words}")
        while True:
            user_word = input("Enter a word").lower()
            if user_word == 'stop':
                break

            if user_word in word_count:
                num_word = word_count[user_word]
                word_ratio = num_word / total_words if total_words > 0 else 0
                print(f" word {user_word}' {word_ratio:.2%} / total words {total_words}")
            else:
                print(f"Word '{user_word}' is not in the text.")

