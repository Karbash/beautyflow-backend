from database import get_connection
from datetime import datetime


class Paciente:

    @staticmethod
    def listar():
        conn = get_connection()
        try:
            pacientes = conn.execute(
                "SELECT * FROM pacientes ORDER BY id DESC"
            ).fetchall()
            return [dict(x) for x in pacientes]
        finally:
            conn.close()

    @staticmethod
    def buscar(id):
        conn = get_connection()
        try:
            paciente = conn.execute(
                "SELECT * FROM pacientes WHERE id=?", (id,)
            ).fetchone()
            return dict(paciente) if paciente else None
        finally:
            conn.close()

    @staticmethod
    def cadastrar(dados):
        if not isinstance(dados, dict):
            dados = dados.to_dict()

        conn = get_connection()
        try:
            conn.execute("""
                INSERT INTO pacientes(nome, idade, telefone, email, tipo_pele, queixa_principal, data_cadastro)
                VALUES(?,?,?,?,?,?,?)
            """, (
                dados["nome"],
                dados["idade"],
                dados["telefone"],
                dados["email"],
                dados["tipo_pele"],
                dados["queixa_principal"],
                datetime.now().isoformat(timespec='minutes')
            ))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def atualizar(id, dados):
        if not isinstance(dados, dict):
            dados = dados.to_dict()

        conn = get_connection()
        try:
            conn.execute("""
                UPDATE pacientes
                SET nome=?, idade=?, telefone=?, email=?, tipo_pele=?, queixa_principal=?
                WHERE id=?
            """, (
                dados["nome"],
                dados["idade"],
                dados["telefone"],
                dados["email"],
                dados["tipo_pele"],
                dados["queixa_principal"],
                id
            ))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def excluir(id):
        conn = get_connection()
        try:
            conn.execute("DELETE FROM pacientes WHERE id=?", (id,))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def estatisticas():
        conn = get_connection()
        try:
            row = conn.execute("""
                SELECT
                    COUNT(*) AS total_pacientes,
                    COALESCE(SUM(CASE WHEN tipo_pele='Oleosa' THEN 1 ELSE 0 END), 0) AS pele_oleosa,
                    COALESCE(SUM(CASE WHEN tipo_pele='Seca'   THEN 1 ELSE 0 END), 0) AS pele_seca,
                    COALESCE(SUM(CASE WHEN tipo_pele='Mista'  THEN 1 ELSE 0 END), 0) AS pele_mista,
                    COALESCE(SUM(CASE WHEN tipo_pele='Normal' THEN 1 ELSE 0 END), 0) AS pele_normal
                FROM pacientes
            """).fetchone()
            return dict(row)
        finally:
            conn.close()
