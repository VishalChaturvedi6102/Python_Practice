# py program to print coontent of the directory using the os module

import os  #yeah per nah maine apne os module import maara hai 

directory_path = '/'  # yeah wala variable mere directory ka path specify karega
contents = os.listdir(directory_path)   # yeah meri ditrectory main present all files and folder ko list karega

for items in contents:   # yeah toh loop mere each file and directory name ko print karne ke liye
    print(items)




#The os module in Python is a built-in standard utility that provides a portable way to interact with the underlying operating system. It allows Python code to perform OS-dependent tasks like file system management, process management, and handling environment variables, working consistently across Windows, macOS, and Linux when the functionality is supported by the specific OS. 
# Key Functionality and Common Methods
# To use the module, you must first import it into your script: 
# python
# import os
# Here are some of the most commonly used functions within the os module:
# os.getcwd(): Returns the current working directory.
# os.chdir(path): Changes the current working directory to the specified path.
# os.listdir(path='.'): Returns a list containing the names of the entries in the directory given by path.
# os.mkdir(path): Creates a new directory at the specified path.
# os.rename(src, dst): Renames a file or directory from source (src) to destination (dst).
# os.remove(path) / os.rmdir(path): Deletes a file (os.remove()) or an empty directory (os.rmdir()).
# os.environ: A dictionary representing the user's environment variables, allowing you to access or modify them (e.g., os.environ["HOME"]).
# os.path: A sub-module for common pathname manipulations (e.g., os.path.exists(), os.path.isdir(), os.path.basename()).
# os.system(command): Executes a command in a subshell (e.g., running command-line tools). 
# For more in-depth examples