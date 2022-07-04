import os, sys


class Explorer:    
    def __init__(self):
        self.file_count = 0
        self.folder_count = 0
        self.target_paths = []

    def get_target_paths(self):
        target_paths_filter = []

        for i in self.target_paths:
            if i not in target_paths_filter:
                target_paths_filter.append(i)
        return target_paths_filter

    def set_statistics(self, item):
        if os.path.isdir(item):
            self.folder_count += 1

        elif os.path.isfile(item):
            self.file_count += 1

    def get_statistics(self):
        return f"{self.folder_count} folders, {self.file_count} files."

    def explorer(self, directory, target):
        list_paths = sorted([path for path in os.listdir(directory)])

        for index in range(len(list_paths)):
            if target in list_paths[index]:
                self.target_paths.append((directory + list_paths[index]))

            absolute = os.path.join(directory, list_paths[index])
            self.set_statistics(absolute)

            if index == len(list_paths) - 1:
                if os.path.isdir(absolute):
                    self.explorer(absolute, target)
            else:
                if os.path.isdir(absolute):
                    self.explorer(absolute, target)
