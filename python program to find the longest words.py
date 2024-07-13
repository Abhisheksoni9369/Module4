def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
        
        
        max_length = max(len(word) for word in words)
        
        
        longest_words = [word for word in words if len(word) == max_length]
        
        return longest_words
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  

longest_words = find_longest_words(filename)
if isinstance(longest_words, list):
    print("The longest word(s):")
    for word in longest_words:
        print(word)
else:
    print(longest_words)
