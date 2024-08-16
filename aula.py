import mysql.connector
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bdyoutube"
)
cursor = conexao.cursor()

nome_produto = "Todynho"
comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #usado quando o "comando" edita o banco de dados

cursor.close()
conexao.close()


#CREATE

#nome_produto = "chocolate"
#valor = 16
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() #usado quando o "comando" edita o banco de dados

#READ

#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall() #usado para ler o banco de dados
#print(resultado)

#UPDATE

#nome_produto = "Todynho"
#valor = 6
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #usado quando o "comando" edita o banco de dados

#DELETE

#nome_produto = "Todynho"
#comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() 