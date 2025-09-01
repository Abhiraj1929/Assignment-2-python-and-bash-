def write_content_to_file():
    file_path = 'my_document.txt'
    content = "This is the first line written to the file.\n" \
              "Here is a second line with some more text.\n" \
              "File handling in Python is straightforward!"

    try:
        with open(file_path, 'w') as file:
            file.write(content)
        
        print(f"Successfully wrote content to '{file_path}'.")

    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# Main execution block
if __name__ == "__main__":
    write_content_to_file()
