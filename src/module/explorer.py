import pathlib, os


class Explorer:    
    def __init__(self):
        self.file_count = 0
        self.folder_count = 0

        self.target_paths = []

    def get_target_paths(self):
        """ returns the paths to the desired pattern """

        target_paths_filter = []
        for i in self.target_paths:
            if i not in target_paths_filter:
                target_paths_filter.append(i)
        return target_paths_filter

    def set_statistics(self, item):
        """ collects the number of folders and files browsed """

        if pathlib.Path(item).is_dir():
            self.folder_count += 1

        elif pathlib.Path(item).is_file():
            self.file_count += 1

    def get_statistics(self):
        """ returns the number of folders and files browsed, collected by set_st """
        return f"{self.folder_count} folders, {self.file_count} files."

    def get_tuple_content(self, tup):
        """ Expects a tuple of a single element and the resort its filtered content in the case of Windows """

        array_for_conv = []
        array_for_conv.append(str(tup))
        array_for_conv[0].replace('(', '').replace('WindowsPath', '').replace(')', '').replace('\"', '')

        return array_for_conv[0]

    def explorer(self, directory: str, pattern: str):
        """ performs the search where it was dropped off. Uses other functions to operate and is therefore not independent """
        
        list_paths = sorted([path for path in os.listdir(directory)])

        for index in range(len(list_paths)):
            full_path = pathlib.Path(directory) / list_paths[index]

            if pattern in list_paths[index]:
                self.target_paths.append((self.get_tuple_content(directory) + list_paths[index]).replace('\\', '/'))
                self.set_statistics(full_path)

            try:
                if pathlib.Path(full_path).is_dir():
                    self.explorer(full_path, pattern)
            except PermissionError as error:
                print(f"Sorry. You are not allowed to enter in '{full_path}'.")
                continue
            except OSError as error:
                print(error)
                continue