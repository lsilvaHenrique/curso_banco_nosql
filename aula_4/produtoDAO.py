from produto import Produto

class ProdutoDAO:
    def __init__(self, db_connection):
        self.db = db_connection

    def pesquisar_todos(self):
        if not self.db.connection:
            print("⚠️ Conexão não está estabelecida.")
            return []

        try:
            query = "SELECT * FROM atividade.produtos"
            self.db.cursor.execute(query)
            resultados = self.db.cursor.fetchall()
            produtos = []
            for linha in resultados:
                produto = Produto(
                    id=int(linha[0]),
                    nome=linha[1],
                    valor=linha[2]
                )
                produtos.append(produto)
                print(produto)
            return produtos

        except Exception as e:
            print("❌ Erro ao executar a consulta:", e)
            return []
