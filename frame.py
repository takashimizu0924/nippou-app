import tkinter as tk

class Frame:
    def __init__(self,root) -> None:
        self._frame = tk.Frame(root)
        
    def get_frame(self) -> tk.Frame:
        return self._frame
        
class InputFrame(Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
    
class BrowseFrame(Frame):
    def __init__(self, root) -> None:
        super().__init__(root)
    