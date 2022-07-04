import os, sys


class Explorer:
    
    def __init__(self):
        self.file_count = 0
        self.folder_count = 0
        self.target_paths = []

    def set_statistics(self, item):
        if os.path.isdir(item):
            self.folder_count += 1

        elif os.path.isfile(item):
            self.file_count += 1

    def get_statistics(self):
        return f"{self.folder_count} folders, {self.file_count} files."

    def explorer(self, directory, target, prefix=""):
        list_paths = sorted([path for path in os.listdir(directory)])

        for index in range(len(list_paths)):
            if target in list_paths[index]:
                self.target_paths.append((directory + list_paths[index]))

            absolute = os.path.join(directory, list_paths[index])
            self.set_statistics(absolute)

            if index == len(list_paths) - 1:
                print(prefix + "└── " + list_paths[index])
                if os.path.isdir(absolute):
                    self.explorer(absolute, "yarn", prefix + "    ")
            else:
                print(prefix + "├── " + list_paths[index])
                if os.path.isdir(absolute):
                    self.explorer(absolute, "yarn", prefix + "│   ")

research = Explorer()
result = research.explorer("/home/b4b4/", "yarn")
print(result)
print(research.target_paths)
print(research.get_statistics())
