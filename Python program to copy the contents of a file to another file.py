def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            with open(destination_file, 'w') as dest_file:
                for line in src_file:
                    dest_file.write(line)
        return f"Successfully copied contents from '{source_file}' to '{destination_file}'"
    except FileNotFoundError:
        return f"Error: The file '{source_file}' does not exist."
    except Exception as e:
        return f"Error: {e}"


source_filename = 'source.txt'  
destination_filename = 'destination.txt'  
result = copy_file(source_filename, destination_filename)
print(result)
