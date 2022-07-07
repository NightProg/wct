import pathlib, os


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

        elif pathlib.Path(item).is_file():
            self.file_count += 1

    def get_statistics(self):
        return f"{self.folder_count} folders, {self.file_count} files."

    def get_tuple_content(self, tup):
        array_for_conv = []
        array_for_conv.append(str(tup))
        array_for_conv[0].replace('(', '').replace('WindowsPath', '').replace(')', '').replace('\"', '')

        return array_for_conv[0]

    def explorer(self, directory: str, pattern: str):
        list_paths = sorted([path for path in os.listdir(directory)])

        for index in range(len(list_paths)):
            if pattern in list_paths[index]:
                self.target_paths.append((self.get_tuple_content(directory) + "/" + list_paths[index]).replace('\\', '/'))

            absolute = pathlib.Path(directory) / list_paths[index]
            self.set_statistics(absolute)
            
            if pathlib.Path(absolute).is_dir():
                self.explorer(absolute, pattern)