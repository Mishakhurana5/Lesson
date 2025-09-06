new_file = open('File.txt', 'x')
new_file.close()

import os
print("Checking if File.txt exists or not...")
if os.path.exists("File.txt"):
    os.remove("File.txt")
else:
  print("The file does not exist")

  my_file = open("File.txt", "w")
  my_file.write("Hi! I am penguin and I am 1 yr old")
  my_file.close()

  os.remove('Codingal.txt')

  os.rmdir('Folder')