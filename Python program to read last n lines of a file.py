from collections import deque

def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = deque(file, maxlen=n)
        return list(lines)
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  
n = 5  

last_n_lines = read_last_n_lines(filename, n)
for line in last_n_lines:
    print(line, end='') 
