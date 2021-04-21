import tkinter as tk

# Aplicacion = Tk()

# Aplicacion.iconbitmap('key_1564.ico')
# Aplicacion.title('Generador de Contraseñas')

# Aplicacion.configure(bg = '#25256F')
# Aplicacion.geometry('500x200')
# # ttk.Button(Aplicacion, text='Salir', command=quit).pack(side=BOTTOM)

# #Declaración de los frames
# AppsFrame=Frame()
# botonesFrame=Frame()

# #Ubicación de los frames
# AppsFrame.pack(side='top')
# botonesFrame.pack(side='bottom')



# Aplicacion.mainloop()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()