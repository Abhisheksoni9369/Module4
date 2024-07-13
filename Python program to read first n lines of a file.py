def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = []
            for i in range(n):
                line = file.readline()
                if not line:  
                    break
                lines.append(line.strip())
        return lines
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  
n = 5  

first_n_lines = read_first_n_lines(filename, n)
for line in first_n_lines:
    print(line)
