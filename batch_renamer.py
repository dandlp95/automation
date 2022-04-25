import os

search = "file"
replace = "document"

# Get files in current directory (that's what the dot means)
dir_content = os.listdir(".")

# list comprehension
docs = [doc for doc in dir_content if os.path.isfile(doc)]

print(f"{len(docs)} of {len(dir_content)} are files")

# Files that have been renamed in the process
renamed = 0

for doc in docs:
    
    if search in doc:

        new_name = doc.replace(search, replace)
        os.rename(doc, new_name)
        renamed += 1

        print(f"Renamed file {doc} to {new_name}")