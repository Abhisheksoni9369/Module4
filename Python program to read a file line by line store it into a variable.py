def read_file_into_variable(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  

file_content = read_file_into_variable(filename)
if isinstance(file_content, list):
    for line in file_content:
        print(line, end='')  
else:
    print(file_content)
