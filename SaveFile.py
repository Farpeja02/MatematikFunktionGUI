from tkinter.filedialog import asksaveasfile

#This file was used so the group could work on both MFfile and the Save function at ones.
#This function was then moved into MFfile and is no longer operaional or used.

def Save(fig):



    filename = asksaveasfile(initialfile='Untitled.png', defaultextension=".png", filetypes=[("All Files", "*.*")])
    print(filename.name)
    fig.savefig(filename.name)
