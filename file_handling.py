def file_read_write():
    import os

    # Step 1: Ask the user for the input filename
    filename = input("Enter the filename to read: ").strip()

    # Step 2: Handle potential errors during file opening
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error file'{filename}' cannot be read")
        return
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Step 3: Modify the content
    text = "THANK YOU SO MUCH"

    # Step 4: Write the modified content to a new file
    try:
        with open(filename, 'w') as outfile:
          file.write
        print(f"Modified content has been written to '{output_filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Run the program
file_read_write()
