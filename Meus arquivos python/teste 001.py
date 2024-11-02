Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
print('estou aprendendo python')
estou aprendendo python
print('Olá, mundo!')
Olá, mundo!
print(7+4)
11
print('7'+'4')
74
nome
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nome
NameError: name 'nome' is not defined. Did you mean: 'None'?
nome=Melissa
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    nome=Melissa
NameError: name 'Melissa' is not defined
>>> nome='Melissa'
>>> idade='5'
>>> peso'8.5'
SyntaxError: invalid syntax
>>> peso8.5
SyntaxError: invalid syntax
>>> peso=8.5
>>> print(nome,idade,peso)
Melissa 5 8.5
>>> print(nome + idade+ peso)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(nome + idade+ peso)
TypeError: can only concatenate str (not "float") to str
>>> TypeError: can only concatenate str (not "float") to st
SyntaxError: invalid syntax
>>> nome=input('Qual o seu nome?')
Qual o seu nome? Paula ket 
>>> idade=input(' Quantos anos você tem?')
 Quantos anos você tem? 33
>>> peso=input('Qual o seu peso?')
Qual o seu peso?90
>>> print(nome, peso, idade)
 Paula ket  90  33
>>> 
================== RESTART: C:/Users/polya/OneDrive/Área de Trabalho/teste 01.py =================
Qual é o seu nome? Polyana
Quantos anos você tem ? 78
Qual o seu peso? 99
 Polyana  78  99
>>> 
