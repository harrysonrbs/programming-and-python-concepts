"""
                                                                          DATA INPUT
                                                          
Data sent into application.

A very common task in a program or script is simply capturing data typed by the keyboard by a user, this data will then be processed for a particular task.

In Python, to capture data typed on the keyboard by a user, we can employ the function input() which will activate the typing mode in the console, this way the 
input() function will store a typed data type to a variable, for example. It is important to remember that we can pass a text (string) as a parameter to the input() 
function, requesting more specific data from the user.

                                      ------------------------------------------------------------------------------------
                                      
Dados enviado para dentro da aplicação.

Uma tarefa bastante comum em um programa ou script é simplesmente a caputura de dados digitados pelo teclado por um usuário, dessa forma, esse dados serão processados 
para uma determina tarefa.

No Python, para capturar dados digitados pelo teclado por um usuário, podemos empregar a função input() que ativará o modo de digitação no console, dessa forma a função 
input() armazenará um tipo de dado digitado a  uma variável, por exemplo. É importante lembrar que podemos passar como parâmetro da função input() um texto (string),
solicitando dados mais específicos ao usuário. 
   
"""

# coding: utf-8

login = input("Login: ")
password = input("Password: ")

print(login)
print(password)
