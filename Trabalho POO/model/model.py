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