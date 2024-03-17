import os


def rename_files(directory):
    for filename in os.listdir(directory):
        if '.' in filename:
            # Replace the first instance of '.'
            new_filename = filename.replace('.', ' -', 1)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")


# Specify the directory path
directory_path = 'Terraria'

# Call the function to rename files
rename_files(directory_path)
