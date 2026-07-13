filename = input("Enter file name: ")

if "." in filename:
    extension = filename.split(".")[-1]
    print("File Extension:", extension)
else:
    print("No extension found.")