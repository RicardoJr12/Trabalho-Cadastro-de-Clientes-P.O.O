import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class Pessoa:
    def __init__(self, nome, idade, cpf, email, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.data_nascimento = data_nascimento

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, data_nascimento):
        super().__init__(nome, idade, cpf, email, data_nascimento)

class GerenciadorClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    def alterar_cliente(self, index, novo_cliente):
        if 0 <= index < len(self.clientes):
            self.clientes[index] = novo_cliente

    def excluir_cliente(self, index):
        if 0 <= index < len(self.clientes):
            del self.clientes[index]

    def salvar_clientes_em_json(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([cliente.__dict__ for cliente in self.clientes], f, indent=4)


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Clientes")
        
        self.gerenciador = GerenciadorClientes()

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

    def atualizar_lista(self):
        self.lista_clientes.delete(0, tk.END)
        for cliente in self.gerenciador.listar_clientes():
            self.lista_clientes.insert(tk.END, f"{cliente.nome}, {cliente.idade} anos, {cliente.cpf}, {cliente.email}, {cliente.data_nascimento}")

    def adicionar_cliente(self):
        nome = simpledialog.askstring("Nome do Cliente", "Digite o nome do cliente:")
        idade = simpledialog.askinteger("Idade do Cliente", "Digite a idade do cliente:")
        cpf = simpledialog.askstring("Número do CPF", "Digite o CPF:")
        email = simpledialog.askstring("E-Mail", "Digite o seu E-Mail:")
        data_nascimento = simpledialog.askstring("Data de Nascimento", "Digite sua Data de Nascimento:")
        if nome and idade and cpf and email and data_nascimento is not None:
            cliente = Cliente(nome, idade, cpf, email, data_nascimento)
            self.gerenciador.adicionar_cliente(cliente)
            self.atualizar_lista()

    def alterar_cliente(self):
        selecionado = self.lista_clientes.curselection()
        if selecionado:
            index = selecionado[0]
            nome = simpledialog.askstring("Novo Nome do Cliente", "Digite o novo nome do cliente:")
            idade = simpledialog.askinteger("Nova Idade do Cliente", "Digite a nova idade do cliente:")
            cpf = simpledialog.askstring("Reescreva o CPF do Cliente", "Digite o CPF do cliente:")
            email = simpledialog.askstring("Novo E-Mail do Cliente", "Digite o novo E-Mail do cliente:")
            data_nascimento = simpledialog.askstring("Reescreva a Data de Nascimento do Cliente", "Digite a Data de Nascimento do cliente:")
            if nome and idade and cpf and email and data_nascimento is not None:
                novo_cliente = Cliente(nome, idade, cpf, email, data_nascimento)
                self.gerenciador.alterar_cliente(index, novo_cliente)
                self.atualizar_lista()
        else:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um cliente para alterar.")

    def excluir_cliente(self):
        selecionado = self.lista_clientes.curselection()
        if selecionado:
            index = selecionado[0]
            self.gerenciador.excluir_cliente(index)
            self.atualizar_lista()
        else:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um cliente para excluir.")

    def salvar_clientes(self):
        arquivo = simpledialog.askstring("Salvar Clientes", "Digite o nome do arquivo (com .json):")
        if arquivo:
            self.gerenciador.salvar_clientes_em_json(arquivo)
            messagebox.showinfo("Sucesso", "Clientes salvos com sucesso!")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x400")
    root.resizable(False, False)
    app = App(root)
    root.mainloop()