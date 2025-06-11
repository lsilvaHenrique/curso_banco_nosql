import psycopg2
from psycopg2 import OperationalError

class Produto:
    def __init__(self, id=None, nome=None, valor=None):
        self.id = id
        self.nome = nome
        self.valor = valor

class ProdutoDAO:
    def __init__(self):
        try:
            self.con = psycopg2.connect(
                host='datawarehouse.graded.br',
                database='sgp_datawarehouse',
                user='lucas.henrique',
                password='Graded@2024',
                port=5432,
                connect_timeout=5
            )
            print("✅ Conectado ao servidor PostgreSQL!")
            self.cursor = self.con.cursor()

            self.cursor.execute("SELECT version();")
            db_info = self.cursor.fetchone()
            print("📦 Versão do PostgreSQL:", db_info[0])

        except OperationalError as e:
            print("❌ Erro ao conectar ao PostgreSQL:", e)
            self.con = None

    def pesquisa_todos(self):
        if not self.con:
            print("⚠️ Conexão não está estabelecida.")
            return []

        try:
            url = "SELECT * FROM atividade.produtos"
            self.cursor.execute(url)
            result = self.cursor.fetchall()
            lista = []
            for linha in result:
                p = Produto()
                p.id = int(linha[0])
                p.nome = linha[1]
                p.valor = linha[2]
                lista.append(p)
                print(f"ID: {p.id} | Nome: {p.nome} | Valor: {p.valor}")
            return lista

        except Exception as e:
            print("❌ Erro ao executar a consulta:", e)
            return []

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()
            print("🔒 Conexão fechada com sucesso.")

if __name__ == "__main__":
    conexao = ProdutoDAO()
    conexao.pesquisa_todos()
    conexao.fechar_conexao()
