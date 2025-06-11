from databaseConnection import DatabaseConnection
from produtoDAO import ProdutoDAO

if __name__ == "__main__":
    db = DatabaseConnection(
        host='datawarehouse.graded.br',
        database='sgp_datawarehouse',
        user='lucas.henrique',
        password='Graded@2024'
    )
    db.conectar()

    produto_dao = ProdutoDAO(db)
    produto_dao.pesquisar_todos()

    db.desconectar()
