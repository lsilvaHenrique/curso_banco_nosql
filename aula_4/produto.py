class Produto:
    def __init__(self, id=None, nome=None, valor=None):
        self.id = id
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Valor: {self.valor}"