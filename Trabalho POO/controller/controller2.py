import tkinter as tk
from model import GerenciadorClientes, Cliente
from view import App

class Controller:
    def __init__(self, view):
        self.view = view
        self.gerenciador = GerenciadorClientes()

    def atualizar_lista(self):
        self.view.atualizar_lista(self.gerenciador.listar_clientes())

    def adicionar_cliente(self):
        dados_cliente = self.view.adicionar_cliente()
        if all(dados_cliente):
            cliente = Cliente(*dados_cliente)
            self.gerenciador.adicionar_cliente(cliente)
            self.atualizar_lista()

    def alterar_cliente(self):
        selecionado = self.view.excluir_cliente()
        if selecionado:
            index = selecionado[0]
            dados_cliente = self.view.alterar_cliente()
            if all(dados_cliente):
                novo_cliente = Cliente(*dados_cliente)
                self.gerenciador.alterar_cliente(index, novo_cliente)
                self.atualizar_lista()
        else:
            self.view.mostrar_aviso("Seleção Inválida", "Por favor, selecione um cliente para alterar.")

    def excluir_cliente(self):
        selecionado = self.view.excluir_cliente()
        if selecionado:
            index = selecionado[0]
            self.gerenciador.excluir_cliente(index)
            self.atualizar_lista()
        else:
            self.view.mostrar_aviso("Seleção Inválida", "Por favor, selecione um cliente para excluir.")

    def salvar_clientes(self):
        arquivo = simpledialog.askstring("Salvar Clientes", "Digite o nome do arquivo (com .json):")
        if arquivo:
            self.gerenciador.salvar_clientes_em_json(arquivo)
            self.view.mostrar_mensagem("Sucesso", "Clientes salvos com sucesso!")

def main():
    root = tk.Tk()
    root.geometry("700x400")
    root.resizable(False, False)
    view = App(root)
    controller = Controller(view)
    root.mainloop()

if __name__ == "__main__":
    main()