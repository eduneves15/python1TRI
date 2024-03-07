import tkinter as tk  

def calcular():
    try: 
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2 
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")
        
root = tk.Tk()
root.title("Calculadora")
        
label_num1 = tk.Label(root, text="Número 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
        
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0, padx=5, pady=5)
        
label_num2 = tk.Label(root, text="Número 2:")
label_num2.grid(row=1, column=1, padx=5, pady=5)
        
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)
        
btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
       
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
       
       #Inicia o loop principal da aplicação
root.mainloop()
