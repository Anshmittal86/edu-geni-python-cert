# File Handling:- File Handling means open, close, write, read and append file. 

# Opening file:- open(filename, mode)
f = open('./data.txt', "r")

# Closing file:- close() 
f.close()

# Reading data into file:- using read() function
f = open('./data.txt', "r")
data = f.read()
print(data)
f.close()

# Reading file methods
# - read():- read all content
# - read(5) :- read first 5
# - readline():- read one line of the file data
# - readlines():- read all line of the file data and return a list

f = open('./data.txt', "r")
print(f.read(5))
print(f.readline())
print(f.readlines())
f.close()


# with method :- automatically close file
with open('./data.txt', "r") as f:
    data = f.read()
    print(data)
    
# write file:- write() method is used to write data 
# w overwrite the old data
with open('./data.txt', 'w') as f:
    f.write("Hello I am sample write data")
    

# Writing methods:- 
# - write()
# - writelines(["klsdfjd\n", "ksjdfhsdf\n", "sdjfdsf"])

with open('./data.txt', 'w') as f:
    f.write("Hello I am sample write data")
    f.writelines(['Line1\n', 'Line2'])
    
# Append file (add data at end)
with open("data.txt", "a") as f:
    f.write("\nHello I am append data")
    
    
# Create :- Create new file (error if exist)
with open("data2.txt", "x") as f: # creates file, error it exist
    pass

# Binary Mode
with open("admin-login.png", "rb") as f:
    data = f.read()
    print(data)
    

# File mode summary
# - 'r':- read file (default)
# - 'w':- write (overwrite)
# - 'a':- append
# - 'x': create
# - 'b': binary mode
# - 't': text mode


# always close file or use with
# 'w' mode overwrite old data
# use 'b' for binary files(images, audio, video etc.)