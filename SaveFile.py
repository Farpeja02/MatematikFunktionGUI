from tkinter.filedialog import asksaveasfile



def Save():



    filename = asksaveasfile(initialfile='Untitled.png', defaultextension=".png", filetypes=[("All Files", "*.*")])
    print(filename.name)
    self.fig.savefig(filename.name)
