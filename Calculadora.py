import tkinder as tk

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text= "Por favor, insira números válidos.")
        
root = tk.Tk()
root.title("Calculadora")

label_num1 = tk.Label(root, text = "Número ':")
