def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        return f"Successfully wrote {len(input_list)} items to '{filename}'"
    except Exception as e:
        return f"Error: {e}"


filename = 'output.txt'  
my_list = ['apple', 'banana', 'cherry', 'date']

result = write_list_to_file(filename, my_list)
print(result)
