# _*Gerenciador de tarefas*_
¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨
<span style="color:pink">
Este projeto servirá para aprimorarmos nossa lógica de programação ao mesmo tempo em que exploramos conceitos e técnicas de programação de back-end e full-stack. Vamos utilizar e desenvolver o conceito de MVC (Model-View-Controller), algumas particularidades da Programação Orientada a Objetos, Programação Funcional, persistência de dados (MySQL), microframework Flask e gerenciador de pacotes do Python (Astral uv).
</span>

¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨

## _*Alguns passos iniciais para preparar o projeto:*_

¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨

1. Caso não tenha instalado, prepare o uv no seu OS. Você encontra o script de instalação no site <https://docs.astral.sh/uv/#installation>
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.psl | iex"
```

2. Faça a inicialização do projeto com o comando:

```bash
uv init
```

Até então usavamos um Layoout de Pacote (Package Layout) denominado flat-layout. O uv adota uma estruturação mais moderna src-layout, que previne erros de importação comuns chamados `import shadowing`(importações mascaradas).

3. Crie um ambiente virtual no Python:
```bash
uv venv
```

Ative o ambiente virtual se necessário:

```powershell
.venv/Scripts/Activate.ps1 # no Powershell do Windows
source .venv/Scripts/activate # no Git Bash do Windows
source .venv/bin/activaate # no Bash do Linux
```

4. Instale o Flask
```bash
uv add flask # Será criado um arqiovo uv.lock contendo as dependências (requerimentos) e versões dos pacotes do seu projeto.
```

5. Crie um arquivo app.py contendo o código inicial do projeto
```python
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Servidor online!'
```

6. Teste a aplicação iniciando o servidor do Flask

```bash
uv run flask run
```

¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨-.°.-¨

