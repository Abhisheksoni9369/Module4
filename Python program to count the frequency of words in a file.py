def count_word_frequency(filename):
    try:
        word_freq = {}
        with open(filename, 'r') as file:
            
            for line in file:
                
                words = line.split()
                
                for word in words:
                    
                    word = word.strip('.,!?:"')
                    
                    word = word.lower()
                    
                    if word:
                        if word in word_freq:
                            word_freq[word] += 1
                        else:
                            word_freq[word] = 1
        
        return word_freq
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  

word_frequency = count_word_frequency(filename)
if isinstance(word_frequency, dict):
    print("Word Frequency:")
    for word, freq in word_frequency.items():
        print(f"{word}: {freq}")
else:
    print(word_frequency)
