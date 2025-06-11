import psycopg2
from psycopg2 import OperationalError

class DatabaseConnection:
    def __init__(self, host, database, user, password, port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port,
                connect_timeout=5
            )
            self.cursor = self.connection.cursor()
            print("✅ Conexão estabelecida com o PostgreSQL!")

            # Mostrar versão do PostgreSQL
            self.cursor.execute("SELECT version();")
            db_info = self.cursor.fetchone()
            print("📦 Versão do PostgreSQL:", db_info[0])

        except OperationalError as e:
            print("❌ Erro ao conectar ao PostgreSQL:", e)
            self.connection = None

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("🔒 Conexão fechada com sucesso.")
