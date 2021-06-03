"""

                                                                  DATA MANIPULATION

It's basically the manipulation of information, that is, it shows demonstrations of the manipulation of values using a built-in Python function, the 'print' function.

1 - Some variables will be declared;

2 - Values will be assigned to the names, and these names will receive instances of the type of the values being passed;

Note: It is not necessary to declare the variable's type, as Python is a dynamically typed programming language.

3 - A string is passed and it will be concatenated with the value of each variable inside the 'print' function.

                                                ----------------------------------------

É basicamente a manipulação de informações, ou seja, é exibido demostrações da manipulação de valores utilizando uma função interna do Python, a função 'print'.

1 - Será declarado algumas variáveis;

2 - Serão atribuídos valores aos nomes, e esses nomes receberão instâncias do tipo do valores que estão sendo passados;

Obsservação: Não é necessário declarar o tipo da variável, temos que o Python é uma linguagem de programação de tipagem dinâmica.

3 - É passado uma string e a mesma será concatenada com o valor de cada variável dentro da função 'print'.

"""

num_int = 5

num_dec = 7.3

val_str = "text"

print("The value is:", num_int)
print("The value is: %i" % num_int)
print("The value is: " + str(num_int))
print("The value is: {}".format(num_int))

print("The value is:", num_dec)
print("The value is: %.2f" % num_dec)
print("The value is: " + str(num_dec))
print("The value is: {}".format(num_dec))

print("The value is:", val_str)
print("The value is: %s" % val_str)
print("The value is: " + val_str)
print("The value is: {}".format(val_str))
