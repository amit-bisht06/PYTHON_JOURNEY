# Writing to a file

# Write mode ("w") --> Overwrites file
with open("C:\\Users\\ambis\\OneDrive\\Desktop\\Python Journey\\PYTHON_JOURNEY\\Day12_File_Handling\\sample.txt", "w") as f:
    f.write("Hello, this is my first file write!\n")
    f.write("Python makes file handling easy.\n")


# Append mode ("a") --> adds new content"
with open("C:\\Users\\ambis\\OneDrive\\Desktop\\Python Journey\\PYTHON_JOURNEY\\Day12_File_Handling\\sample.txt", "w") as f:
    f.write("This linne is appended.\n")

print("Data written successfully!")    