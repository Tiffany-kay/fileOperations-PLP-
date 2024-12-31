def read_and_write_file():
    try:
        # Asking the user for the filename to read from
        input_filename = input("Enter the name of the file to read from: ")

        # Attempting to open the file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            # Here you can modify the content as needed
            modified_content = content.upper()  # Example modification: converting content to uppercase

        # Asking the user for the filename to write to
        output_filename = input("Enter the name of the file to write to: ")

        # Writing the modified content to the new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Content successfully written to {output_filename}")

    except FileNotFoundError:
        print("Error: The file you are trying to read does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Calling the function
read_and_write_file()

