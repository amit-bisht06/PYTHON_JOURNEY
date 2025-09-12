# Reading from an existing file

# Open file in read mode
f = open("C:\\Users\\ambis\\OneDrive\\Desktop\\Python Journey\\PYTHON_JOURNEY\\Day12_File_Handling\\overview.txt", "r")

# Read full content
content = f.read()
print("File Content : \n", content)

f.close()   # A Good Practice

# Another but Better way(no need to close manually)
with open("C:\\Users\\ambis\\OneDrive\\Desktop\\Python Journey\\PYTHON_JOURNEY\\Day12_File_Handling\\overview.txt", "r") as f:
    for line in f:
        print("Line: ", line.strip())