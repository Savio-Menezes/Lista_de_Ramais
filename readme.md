README.md
📞 Projeto de Ramais - Flask com MySQL
Este projeto utiliza Flask para rodar um servidor web simples e MySQL Connector para realizar a conexão com o banco de dados MySQL. Ele lista ramais e telefones de colaboradores organizados por setor, usuário ou ramal.

🚀 Configuração do Ambiente
1. Requisitos
Certifique-se de ter instalado:
Python (3.8 ou superior)
pip (gerenciador de pacotes do Python)
MySQL (banco de dados configurado)

2. Clonar o Projeto
git clone <URL_DO_REPOSITORIO>
cd tela_ramais


3. Criar Ambiente Virtual (Opcional, mas Recomendado)
python -m venv venv

Ative o ambiente virtual:
venv\Scripts\activate

4. Instalar Dependências
pip install Flask==3.1.0 mysql-connector==2.2.9

Se necessário, você pode instalar diretamente a partir de um arquivo requirements.txt:
pip install -r requirements.txt


5. Configurar o Banco de Dados
Antes de rodar o projeto, configure o banco de dados:
Acesse o arquivo Python principal.
Insira as credenciais do MySQL em:
python

connection = mysql.connector.connect(
    host='SEU_HOST',
    user='SEU_USUARIO',
    password='SUA_SENHA',
    database='SEU_BANCO'
)



6. Executar o Servidor Flask
Com tudo configurado, rode o servidor:
python app.py

O servidor será iniciado em http://127.0.0.1:5000.

