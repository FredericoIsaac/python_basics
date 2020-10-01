# python_basics
Fundamentals of programming with python

# Why?

Porque sinto que apesar de perceber os conceitos sinto que ainda nao sei nada, que os fundamentos nao estão sedimentados.

Isto deve se muito a minha pressa para aprender, tenho que ter tempo, paciencia e fazer exercicios. Pratica los a medida que vão sendo apresentados nos livros.

Com este mês a estudar os fundamentos espero poder chegar ao final e sentir que aprendi o basico da linguagem python e que estou pronto para fazer os projetos mais basicos.

## Goal

* Tirar apontamentos do livro "Programação em Python" de ***Ernesto Costa***, no prazo de duas semanas.
* Tirar apontamentos do livro "Automate the Boring Stuff With Python" de ***Ai Sweigart***, no prazo de duas semanas ate dia 19-09-2020.

## Plano

* Estudar todos os dias:
    * Das 05:00 até as 07:00
    * Na hora de almoço das 13H15 ás 14:00
    * E das 18:00 ás 20:00

* A primeira hora da manhã será escrever os apontamentos e fazer os exercicios
* Na hora de almoço ler e sublinhar
* A tarde ler e sublinhar, pesquisar mais informação para sedimentar informação.

# Bibliografia

https://automatetheboringstuff.com/

https://www.fca.pt/pt/catalogo/informatica/programacao/programacao-em-python/

# Youtube

https://www.youtube.com/watch?v=DhdOKh5Issw&list=PLWKjhJtqVAbkmRvnFmOd4KhDdlK1oIq23&index=3&ab_channel=freeCodeCamp.org


# Youtube lições

Para imprimir com espaço personalizado entre colunas e lidar com try e except 

    def time_table():
        try:
            x = int(input("Introduz um numero: "))
            for row in range(x):
                for column in range(x):
                    print(f"{row*col:2}", end = " ")
                print()
        except ValueError:
            print("Oops, Please enter a number: ")
        q = input("Do you want another table? y/n").lower()
        if q[0] == "n":
            break

    time_table()


Conditions with while loop and else:

    while x > 10:
        print("x é maior que 10")
        x = int(input("introduz um numero: "))
    else:
        print("Boa introduziste um numero menor que 10")

Enumerate que começa onde quiseres

    names = ["joao","andre","sara"]
    for x in enumerate(names, start=1):
        print(x)

    # Se quisermos imprimir isto sem ser num tuple
    for num, name in enumerate(names, start=1):
        print(num, name)

Strip() method

Elimina os espaços em branco numa string

