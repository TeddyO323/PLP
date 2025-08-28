def read_and_modify_file(input_filename, output_filename):
    """
    Reads the content of input_filename, modifies it,
    and writes the result into output_filename.
    In this example, the modification is converting text to uppercase.
    """
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify content (convert to uppercase here)
        modified_content = content.upper()

        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ask the user for the input file name
    input_file = input("Enter the name of the file to read: ").strip()
    output_file = "modified_" + input_file

    # Perform file read, modify, and write
    read_and_modify_file(input_file, output_file)
