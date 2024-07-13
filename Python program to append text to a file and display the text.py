def append_and_display_text(filename, text_to_append):
    try:
        
        with open(filename, 'a') as file:
            file.write(text_to_append + '\n')
        
        
        with open(filename, 'r') as file:
            content = file.read()
        
        return content
    except Exception as e:
        return f"Error: {e}"


filename = 'sample.txt'  
text_to_append = 'This is the new line to be appended.'


file_content = append_and_display_text(filename, text_to_append)
print(file_content)
