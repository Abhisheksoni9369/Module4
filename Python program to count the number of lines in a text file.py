def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  

num_lines = count_lines(filename)
if isinstance(num_lines, int):
    print(f"Number of lines in '{filename}': {num_lines}")
else:
    print(num_lines)
