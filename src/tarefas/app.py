from tarefas.models.database import init_db 

from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.tarefa import Tarefa_classe

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor online!'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # casa com o  nome do input no form
        data_conclusao_form = request.form['dataConclusao'] # casa com o nome do input no form

        data_corrigida = data_conclusao_form or None

        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa_classe(titulo=titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa
        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa_classe.listarTarefas()

    return render_template(
        'base.html', 
        titulo_da_pagina ='Home', 
        tarefas_da_pagina = tarefas
    )

@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefa_classe.apagarTarefa(id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()