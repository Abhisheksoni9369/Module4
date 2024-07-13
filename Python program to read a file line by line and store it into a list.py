def read_file_into_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file]
        return lines
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  

lines_list = read_file_into_list(filename)
if isinstance(lines_list, list):
    for line in lines_list:
        print(line)
else:
    print(lines_list)
