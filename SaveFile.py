from tkinter.filedialog import asksaveasfile
from MFfile import listWindowClass


def Save():
    # åbner save vindue
    file = asksaveasfile(initialfile='Untitled.png', defaultextension=".png", filetypes=[("All Files", "*.*")])
