import customtkinter as ctk

import time


janela_principal = ctk.CTk()
janela_principal.title("Frutaria Do zé")
janela_principal.geometry("340x600")
janela_principal.resizable(False,False)


#label 1
def label_text():
    print("Frut")
label=ctk.CTkLabel(janela_principal, text="Seja bem-vindo") 
label.pack(pady = 30, padx= 20)

#label 2
def label_text():
    print()
label=ctk.CTkLabel(janela_principal, text="Qual fruta deseja?")
label.pack()


#box
itens=["Banana","Maçã","Kiwi"]
combobox = ctk.CTkComboBox (janela_principal, values=itens)
combobox.pack(pady=10, padx=30)

#label 3
def label_text():
    print("Frut")
label=ctk.CTkLabel(janela_principal, text="Qual a quantidade de frutas ?")
label.pack()



def entry_message():
    print()
entry = ctk.CTkEntry(janela_principal, placeholder_text="Digite aqui")
entry.pack()


def button_event():
    print("Ok")
button = ctk.CTkButton(janela_principal, text="ok", command=button_event, anchor="W")
button.pack(pady=10, padx=20)


def label_text():
    print("Frut")
label=ctk.CTkLabel(janela_principal, text="Qual forma de pagamento? ")
label.pack()


itens=["Pix", "Dinheiro ", "Cartão"]
combobox = ctk.CTkComboBox (janela_principal, values=itens)
combobox.pack()

janela_principal.mainloop()