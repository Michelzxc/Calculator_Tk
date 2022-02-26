from tkinter import ttk
from tkinter import *
from logica import operatron


class Calculadora(Frame):
    '''Construye la calculadora.'''

    def __init__(self, master=None):
        super().__init__(master)

        # Configuracion general del Frame
        self.config(bd=5)

        # Estilo general de la fuente
        ttk.Style(self).configure("TButton", font=("Helvetica", 22))

        # Logo de la calculadora
        self.image_logo = (PhotoImage(file='./images/python-image.png')).subsample(19,19)
        self.p_logo = ttk.Label(self, image=self.image_logo)
        self.l_logo = ttk.Label(self, text="Python Calc", font=("Helvetica", 9))

        # Display de la calculadora
        self.display = Entry(self)
        self.display.config(font=("Seven Segment", 16), justify="right",
                            state="readonly",
                            width=19, relief="sunken", bd=6, bg="#F7F7F7", fg="black")

        # Definicion de botones
        self.boton_0 = ttk.Button(self, text="0")
        self.boton_1 = ttk.Button(self, text="1")
        self.boton_2 = ttk.Button(self, text="2")
        self.boton_3 = ttk.Button(self, text="3")
        self.boton_4 = ttk.Button(self, text="4")
        self.boton_5 = ttk.Button(self, text="5")
        self.boton_6 = ttk.Button(self, text="6")
        self.boton_7 = ttk.Button(self, text="7")
        self.boton_8 = ttk.Button(self, text="8")
        self.boton_9 = ttk.Button(self, text="9")

        self.boton_coma = ttk.Button(self, text=",")
        self.boton_c = ttk.Button(self, text="C")
        self.boton_retroceso = ttk.Button(self, text="⌫")
        self.boton_eq = ttk.Button(self, text="=")
        self.boton_sum = ttk.Button(self, text="+")
        self.boton_res = ttk.Button(self, text="-")
        self.boton_mul = ttk.Button(self, text="*")
        self.boton_div = ttk.Button(self, text="/")

        # Ubicacion en el grid
        self.padx = 1
        self.pady = 1
        self.ipady = 0

        self.p_logo.grid(row=0,column=0, sticky="n")
        self.l_logo.grid(row=0,column=0,sticky="s")
        self.display.grid(row=0,column=1, columnspan=4, pady=4)
        self.boton_0.grid(row=6, column=0,
                          padx=self.padx, pady=self.pady, ipady=self.ipady,
                          columnspan=2, sticky="EW")
        self.boton_1.grid(row=5, column=0,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_2.grid(row=5, column=1,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_3.grid(row=5, column=2,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_4.grid(row=4, column=0,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_5.grid(row=4, column=1,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_6.grid(row=4, column=2,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_7.grid(row=3, column=0,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_8.grid(row=3, column=1,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_9.grid(row=3, column=2,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)

        self.boton_coma.grid(row=6, column=2,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_retroceso.grid(row=2, column=2,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_c.grid(row=2, column=0,
                          padx=self.padx, pady=self.pady, ipady=self.ipady,
                          columnspan=2, sticky="EW")
        self.boton_eq.grid(row=2, column=3,
                          padx=self.padx, pady=self.pady, ipady=self.ipady,
                          sticky="EW")
        self.boton_sum.grid(row=6, column=3,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_res.grid(row=5, column=3,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_mul.grid(row=4, column=3,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)
        self.boton_div.grid(row=3, column=3,
                          padx=self.padx, pady=self.pady, ipady=self.ipady)

        # Logica
        self.valores_del_display = StringVar()
        self.valores_del_display.set("0")
        self.display.config(textvariable=self.valores_del_display)

        def f_eq():
            valor_display = self.valores_del_display.get()
            resultado = operatron(valor_display)
            self.valores_del_display.set(resultado)
            
        def num_tecaldo(valor):
            # Valores directos al display
            
            if self.valores_del_display.get() == "0":
                self.valores_del_display.set("")
            
            self.valores_del_display.set(self.valores_del_display.get() + valor)

        def f_clear():
            # Limpia display
            self.valores_del_display.set("0")

        def f_retroceso():
            # Borra el ultimo valor del dysplay
            vdg = self.valores_del_display.get()
            if vdg != "0":
                self.valores_del_display.set(vdg[0:len(vdg)-1])
            
            if self.valores_del_display.get() == "":
                self.valores_del_display.set("0")

        # Configuracion de botones
        self.width = 4
        
        self.boton_0.config(width=self.width, command=lambda: num_tecaldo("0"))
        self.boton_1.config(width=self.width, command=lambda: num_tecaldo("1"))
        self.boton_2.config(width=self.width, command=lambda: num_tecaldo("2"))
        self.boton_3.config(width=self.width, command=lambda: num_tecaldo("3"))
        self.boton_4.config(width=self.width, command=lambda: num_tecaldo("4"))
        self.boton_5.config(width=self.width, command=lambda: num_tecaldo("5"))
        self.boton_6.config(width=self.width, command=lambda: num_tecaldo("6"))
        self.boton_7.config(width=self.width, command=lambda: num_tecaldo("7"))
        self.boton_8.config(width=self.width, command=lambda: num_tecaldo("8"))
        self.boton_9.config(width=self.width, command=lambda: num_tecaldo("9"))

        self.boton_coma.config(width=self.width, command=lambda: num_tecaldo("."))
        self.boton_c.config(width=self.width, command=f_clear)
        self.boton_retroceso.config(width=self.width, command=f_retroceso)
        self.boton_eq.config(width=self.width, command=f_eq)
        self.boton_sum.config(width=self.width, command=lambda: num_tecaldo("+"))
        self.boton_res.config(width=self.width, command=lambda: num_tecaldo("-"))
        self.boton_mul.config(width=self.width, command=lambda: num_tecaldo("*"))
        self.boton_div.config(width=self.width, command=lambda: num_tecaldo("/"))



def calculator():
    '''Inicia la aplicacion "CALCULATOR TKPy".'''

    raiz = Tk()
    raiz.wm_title("CALCULATOR TKPy")
    #raiz.wm_iconbitmap("./images/calculator.ico")  # No funciona en Ubuntu 20.04
    icono = Image("photo", file="./images/calc.png")
    raiz.call('wm','iconphoto',raiz._w, icono)
    raiz.resizable(width=False, height=False)

    calc = Calculadora(raiz)
    calc.pack()

    
    raiz.mainloop()


if __name__ == "__main__":
    calculator()
