import pathlib

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
        if pathlib.Path(item).is_dir():
            self.folder_count += 1

        elif pathlib.Path(item).is_dir():
            self.file_count += 1

    def get_statistics(self):
        return f"{self.folder_count} folders, {self.file_count} files."

    def explorer(self, directory, target):
        list_paths = sorted(pathlib.Path(directory).iterdir(), lambda a: str(a))

        for index in range(len(list_paths)):
            if target in list_paths[index]:
                self.target_paths.append((directory + list_paths[index]))

            absolute = pathlib.Path(directory) / list_paths[index]
            self.set_statistics(absolute)

            
            if pathlib.Path(absolute).is_dir():
                self.explorer(absolute, target)
            
