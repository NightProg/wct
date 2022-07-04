import pathlib 
import errors
class Tree:
    """
    a tree represents a directory structure.
    """
    def __init__(self, path) -> None:
        self.path = pathlib.Path(path) if type(path) is str else path
        
    def get_path(self) -> pathlib.Path:
        return self.path
    
    def get_name(self) -> str:
        return self.path.name
    
    def is_directory(self) -> bool:
        return self.path.is_dir()
    
    def is_file(self) -> bool:
        return self.path.is_file()
    
    def __getitem__(self, key) -> pathlib.Path:
        tree = Tree(self.path / key)
        if tree.path.exists():
            return tree
        raise errors.DirectoryNotFoundError(f"'{tree.path}' does not exist.")
    
    def __str__(self) -> str:
        return str(self.path.absolute())
    
    def __iter__(self) -> iter:
        return map(Tree, self.path.iterdir())
    
    def __div__(self, other) -> pathlib.Path:
        return Tree(self.path / other)
    


if __name__ == "__main__":
    a = Tree(".")

    print(a.get_path())
    print(a.get_name())
    print(a.is_directory())
    print(a.is_file())

    print(a["src"])
    print(a["src"]["module"])
    