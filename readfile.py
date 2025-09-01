def read_content_from_file():
    """
    Opens 'my_document.txt' in read mode, reads all its content,
    and prints it to the console.
    """
    file_path = 'my_document.txt' 

    try:

        with open(file_path, 'r') as file:
            content = file.read()
        
        print(f"--- Content of '{file_path}' ---")
        print(content)
        print("---------------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please run the 'write_to_file.py' script first to create it.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")


if __name__ == "__main__":
    read_content_from_file()
