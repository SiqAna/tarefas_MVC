from datetime import datetime

from tarefas.models.database import Database


class Tarefa_classe:
    """Provê métodos para armazenar, recuperar e processar os dados 
    das tarefas criadas a partir do formulário principal"""
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo=titulo
        self.data_conclusao=data_conclusao

    def salvarTarefa(self):
        """
        Salva a tarefa no banco de dados.
        """
        sql = 'INSERT INTO tarefas (titulo_tarefa, data_conclusão) VALUES(%s, %s);'
        params = (self.titulo, self.data_conclusao)
            # O uso de binding protege contra o SQL Injection
        

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''
        SELECT id_tarefas, titulo_tarefa, data_conclusão 
        FROM tarefas LIMIT 100
        '''
        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    def apagarTarefa(id_tarefas : int):
        sql =  '''DELETE FROM tarefas WHERE id_tarefas = %s;'''
        params = (id_tarefas,)
        with Database() as db:
            db.executar(sql, params)
#Area 51
#tarefa = Tarefa('Minha nova tarefa')
#tarefa.salvarTarefa()