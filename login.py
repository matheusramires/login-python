import psycopg2

db_host = 'IP'
db_port = '5432'
db_user = 'postgres'
db_password = 'senha'
db_name = 'nome_do_db'

connect = psycopg2.connect(host=db_host, dbname=db_name, port=db_port, user=db_user, password=db_password)
cur = connect.cursor()

#insere novo usuario
'''def new_user(nome, login, senha):
    sql = f'insert into login_user.login ({nome}, {login}, {senha}) values (\'admin\',\'admin\', \'admin\')'
    cur.execute(sql)
    connect.commit()'''


#login
def login():

    users = []
    login = str(input('Login: '))
    senha = str(input('Senha: '))

    sql = 'SELECT id, nome, login,senha from login_user.login order by nome'
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        users.append(row)

    #print(users)
    #qtd_user = len(users)
    #print('qtd de usuarios: ' + str(qtd_user))

    for user in users:
        if ((login == user[2]) and (senha == user[3])):
            acesso = bool('true')
            print('acesso permitido!!')
    return acesso


login()



cur.close()
connect.close()
connect.close()
