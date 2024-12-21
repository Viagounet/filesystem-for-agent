from dataclasses import dataclass
from glob import glob
import os

@dataclass
class FileSystem:
    origin_path: str
    
    def __post_init__(self):
        if not os.path.exists(self.origin_path):
            raise ValueError(f"Path {self.origin_path} does not exist")
    
    def tree(self, path=None, prefix=""):
        """Returns a string representation of the file tree starting from path"""
        if path is None:
            path = self.origin_path
            
        # Get contents of directory
        contents = os.listdir(path)
        tree_str = ""
        
        for i, item in enumerate(contents):
            is_last = i == len(contents) - 1
            item_path = os.path.join(path, item)
            
            # Add item to tree string
            if is_last:
                tree_str += f"{prefix}└── {item}\n"
                new_prefix = prefix + "    "
            else:
                tree_str += f"{prefix}├── {item}\n"
                new_prefix = prefix + "│   "
            
            # Recursively add subdirectories
            if os.path.isdir(item_path):
                tree_str += self.tree(item_path, new_prefix)
                
        return tree_str
    
    def __str__(self):
        return self.tree()