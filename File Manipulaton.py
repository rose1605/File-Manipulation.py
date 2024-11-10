def count_words_in_file(filename):
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase for case-insensitive counting

        # Use regex to find words and count occurrences
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)

        # Sort words alphabetically and display counts
        print("Word Counts (Alphabetical Order):")
        for word in sorted(word_counts):
            print(f"{word}: {word_counts[word]}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the filename (with extension): ")
count_words_in_file(filename)
