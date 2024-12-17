from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    connection = mysql.connector.connect(
        host='',
        user='',
        password='',
        database=''
    )
    return connection

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    ordenar = request.form.get('ordenar', 'S')  # Valor padrão 'S' (Setor)
    
    # Conectar ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
   # Consulta SQL dependendo do parâmetro 'ordenar'
    if ordenar == 'S':  # Ordenar por setor
        sql = '''
            SELECT us_nome, us_ramal, us_depto, st_ds, us_tel, us_divulga_ramal, us_divulga_tel
            FROM usuario
            LEFT JOIN setores ON setores.st_id = usuario.st_id
            WHERE us_ativo = 'S'  -- Verifica se o colaborador está ativo
              AND (us_ramal IS NOT NULL AND us_ramal != '' OR us_tel IS NOT NULL AND us_tel != '')  -- Ramal ou celular deve ser válido
            ORDER BY st_ds, us_nome, us_ramal
        '''
    elif ordenar == 'U':  # Ordenar por usuário
        sql = '''
            SELECT us_nome, us_ramal, us_depto, st_ds, us_tel, us_divulga_ramal, us_divulga_tel
            FROM usuario
            LEFT JOIN setores ON setores.st_id = usuario.st_id
            WHERE us_ativo = 'S'  -- Verifica se o colaborador está ativo
              AND (us_ramal IS NOT NULL AND us_ramal != '' OR us_tel IS NOT NULL AND us_tel != '')  -- Ramal ou celular deve ser válido
            ORDER BY us_nome
        '''
    else:  # Ordenar por ramal
        sql = '''
            SELECT us_nome, us_ramal, us_depto, st_ds, us_tel, us_divulga_ramal, us_divulga_tel
            FROM usuario
            LEFT JOIN setores ON setores.st_id = usuario.st_id
            WHERE us_ativo = 'S'  -- Verifica se o colaborador está ativo
              AND (us_ramal IS NOT NULL AND us_ramal != '' OR us_tel IS NOT NULL AND us_tel != '')  -- Ramal ou celular deve ser válido
            ORDER BY us_ramal, us_nome
        '''
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    # Fechar conexão
    cursor.close()
    conn.close()
    
    return render_template('index.html', rows=rows, ordenar=ordenar)

if __name__ == '__main__':
    app.run(debug=True)