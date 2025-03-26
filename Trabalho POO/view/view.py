import tkinter as tk
from tkinter import messagebox, simpledialog

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Clientes")
        
        self.lista_clientes = tk.Listbox(master)
        self.lista_clientes.pack(fill=tk.BOTH, expand=True)

        self.btn_adicionar = tk.Button(master, text="Adicionar Cliente", command=self.adicionar_cliente)
        self.btn_adicionar.pack(fill=tk.X)

        self.btn_alterar = tk.Button(master, text="Alterar Cliente", command=self.alterar_cliente)
        self.btn_alterar.pack(fill=tk.X)

        self.btn_excluir = tk.Button(master, text="Excluir Cliente", command=self.excluir_cliente)
        self.btn_excluir.pack(fill=tk.X)

        self.btn_salvar = tk.Button(master, text="Salvar Clientes em JSON", command=self.salvar_clientes)
        self.btn_salvar.pack(fill=tk.X)

    def atualizar_lista(self, clientes):
        self.lista_clientes.delete(0, tk.END)
        for cliente in clientes:
            self.lista_clientes.insert(tk.END, f"{cliente.nome}, {cliente.idade} anos, {cliente.cpf}, {cliente.email}, {cliente.data_nascimento}")

    def adicionar_cliente(self):
        return simpledialog.askstring("Nome do Cliente", "Digite o nome do cliente:"), \
               simpledialog.askinteger("Idade do Cliente", "Digite a idade do cliente:"), \
               simpledialog.askstring("Número do CPF", "Digite o CPF:"), \
               simpledialog.askstring("E-Mail", "Digite o seu E-Mail:"), \
               simpledialog.askstring("Data de Nascimento", "Digite sua Data de Nascimento:")

    def alterar_cliente(self):
        return simpledialog.askstring("Novo Nome do Cliente", "Digite o novo nome do cliente:"), \
               simpledialog.askinteger("Nova Idade do Cliente", "Digite a nova idade do cliente:"), \
               simpledialog.askstring("Reescreva o CPF do Cliente", "Digite o CPF do cliente:"), \
               simpledialog.askstring("Novo E-Mail do Cliente", "Digite o novo E-Mail do cliente:"), \
               simpledialog.askstring("Reescreva a Data de Nascimento do Cliente", "Digite a Data de Nascimento do cliente:")

    def excluir_cliente(self):
        return self.lista_clientes.curselection()

    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

    def mostrar_aviso(self, titulo, mensagem):
        messagebox.showwarning(titulo, mensagem)