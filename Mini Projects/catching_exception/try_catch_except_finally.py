file = None
try:
    # Try block begins: Python will attempt all the code here.

    # Try to open an existing file in read mode.
    # If the file does not exist, a FileNotFoundError will be raised.
    file = open("file.txt","r+")
    file.write("Hiii my name is shubham.")


    # Define a simple dictionary with one key.
    # my_dict = {"key": "value"}
    #
    # # Attempt to access a non-existent key.
    # # This will raise a KeyError since "keys" is not in the dictionary.
    # print(my_dict["keys"])

# This block will run ONLY if a FileNotFoundError occurred in the try block.
except FileNotFoundError:
    # Create and open the file in write mode.
    file = open("file.txt", "w")

    # Write some content to the file.
    file.write("write something in file")

# This block will run ONLY if a KeyError occurred in the try block.
except KeyError as error_message:
    # Print the error message that shows the missing key.
    print(f"{error_message} not found")

# The else block runs ONLY if no exception was raised in the try block.
# If everything in try succeeded, this block executes.
else:
    print("else: currently i am in else.")
    # file.open("file.txt","r")
    # Read and print the contents of the file.
    file.seek(0)
    content = file.read()
    print(f"{content} here is my content")

# The finally block ALWAYS runs, no matter what happened above.
# This is usually used for cleanup actions like closing files or releasing resources.
finally:
    try:
        file.close()  # Close the file if it was successfully opened.
        print("File was closed.")
    except FileNotFoundError:
        print("file not found")


#=========================================================================================================================================================================
# file = None
# try:
#     # Try to open an existing file in read mode
#     file = open("file.txt")
#
#     # Define a dictionary with a valid key
#     # my_dict = {"key": "value"}
#     #
#     # # Access an existing key (no exception)
#     # print(my_dict["key"])
#
# # Handle missing file
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("write something in file: hi how are you")
#
# # Handle invalid dictionary key
# except KeyError as error_message:
#     print(f"{error_message} not found")
#
# # Run only if no exceptions occurred
# else:
#     print("else:")
#     content = file.read()
#     print(content)
#
# # Always run this block
# finally:
#     # Only try to close the file if it was successfully opened
#     if file is not None:
#         file.close()
#         print("File was closed.")
