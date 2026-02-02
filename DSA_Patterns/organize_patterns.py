import os
import re

base_dir = r'c:\Users\Ankit\Desktop\problem-solvng-methodologies\DSA_Patterns'
index_file = os.path.join(base_dir, '00_Pattern_Index.md')

# Read the index file
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Get all files in the directory
files = [f for f in os.listdir(base_dir) if f.endswith('.md') and f != '00_Pattern_Index.md']

for file_name in files:
    # Remove extension to get folder name
    folder_name = os.path.splitext(file_name)[0]
    folder_path = os.path.join(base_dir, folder_name)
    file_path = os.path.join(base_dir, file_name)

    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create Problems directory inside the pattern folder
    problems_dir = os.path.join(folder_path, 'Problems')
    if not os.path.exists(problems_dir):
        os.makedirs(problems_dir)

    # New file name inside the folder (using README.md for better GitHub browsing experience)
    new_file_name = 'README.md'
    new_file_path = os.path.join(folder_path, new_file_name)

    # Move the file
    if os.path.exists(file_path):
        os.rename(file_path, new_file_path)
        print(f"Moved {file_name} to {folder_name}/{new_file_name}")

    # Update the index content
    escaped_filename = re.escape(file_name)
    pattern = r'\(\./' + escaped_filename + r'\)'
    replacement = f'(./{folder_name}/{new_file_name})'

    index_content = re.sub(pattern, replacement, index_content)

# Update the index file
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Reorganization complete with Problems folders created.")
