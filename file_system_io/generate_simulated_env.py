import os

def create_directory_structure(root_dir, level, max_level):
    if level > max_level:
        return

    for i in range(1, 4):
        dir_name = f"dir{i}"
        dir_path = os.path.join(root_dir, dir_name)
        os.mkdir(dir_path)
        file_path = os.path.join(dir_path, f"file{i}.txt")
        open(file_path, 'w').close()

        create_directory_structure(dir_path, level + 1, max_level)

if __name__ == "__main__":
    root_directory = "/home/astromanish/Projects/openai-api-experiment/sim-env"  # Change this to the desired root directory

    os.mkdir(root_directory)
    create_directory_structure(root_directory, 1, 3)  # Change the maximum level of subdirectories as needed

    home_directory = os.path.join(root_directory, "home")
    os.mkdir(home_directory)
    manish_file_path = os.path.join(home_directory, "manish.py")
    open(manish_file_path, 'w').close()
