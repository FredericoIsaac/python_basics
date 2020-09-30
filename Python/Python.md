
# Objetivos:
    
## Geral

Percorrer o livro "Programação em Python" de ***Ernesto Costa***, tirar apontamentos, fazer exercicios com o visual studio, tudo em 30 dias.

[Livro: Programação em Python
Fundamentos e Resolução de Problemas](https://www.wook.pt/livro/programacao-em-python-ernesto-costa/17043335)

### Plano para cumprir objetivo

São 583 paginas, 583 / 30 dias =  19.43, por isso tenho que fazer uma média de 20 paginas por dia, para dia 31/07/2020 acabar o livro.


## 01/07/2020

Pagina atual: 3

Compilador: um programa que traduz a linguagem de programação para linguagem de maquina (binario?) e depois é que executa

Interpretador: executa diretamente as instruções.

>The main difference is that an interpreter directly executes the instructions in the source programming language while a compiler translates those instructions into efficient machine code.
An interpreter will typically generate an efficient intermediate representation and immediately evaluate it. 
[Source](https://medium.com/hackernoon/compilers-and-interpreters-3e354a2e41cf#:~:text=The%20main%20difference%20is%20that,representation%20and%20immediately%20evaluate%20it.)

### Tipos de Linguagens:

#### Linguagens declarativas ou relacionais:

    Algorithm = Logic + Control

>What is Logic Programming?
Logic programming is a programming strategy that uses logic circuits to control how facts and rules are expressed, rather than only mathematical functions. Often used in genetic and evolutionary programming, **this approach generally tells a model what goal to accomplish, rather than how to accomplish it.** Instead of a carefully structured control flow dictating when to execute and how to evaluate function calls or other instructions, the program’s logic rules are written as logical clauses (predicates). [Source](https://deepai.org/machine-learning-glossary-and-terms/logic-programming)

Por exemplo: Prolog

#### Linguagens Funcionais:

    Algorithm = Data + Functions

>Functional programming (often abbreviated FP) is the process of building software by **composing pure functions, avoiding shared state, mutable data, and side-effects.** Functional programming is declarative rather than imperative, and application state flows through pure functions.

(...)

>A **pure function** is a function which:
Given the same inputs, always returns the same output, and
Has no side-effects

(...)

>**Shared state** is any variable, object, or memory space that exists in a shared scope, or as the property of an object being passed between scopes. A shared scope can include global scope or closure scopes. Often, in object oriented programming, objects are shared between scopes by adding properties to other objects.

(...)

>An **immutable object** is an object that can’t be modified after it’s created. Conversely, a mutable object is any object which can be modified after it’s created.
Immutability is a central concept of functional programming because without it, the data flow in your program is lossy. State history is abandoned, and strange bugs can creep into your software. 

(...)

>A **side effect** is any application state change that is observable outside the called function other than its return value. Side effects include:
>* Modifying any external variable or object property (e.g., a global variable, or a variable in the parent function scope chain)
>* Logging to the console
>* Writing to the screen
>* Writing to a file
>* Writing to the network
>* Triggering any external process
>* Calling any other functions with side-effects

 [Source](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0#:~:text=Functional%20programming%20often%20abbreviated%20FP,state%20flows%20through%20pure%20functions.)

Por exemplo: Lisp

#### Linguagens Imperativas ou Procedimentais:

Um programa procedimental é caracterizado por uma sequência de instruções que atuam sobre os dados (variáveis), alterando de forma destrutiva o seu valor, ou sobre a ordem pela qual as instruções são executadas (instruções de controlo)

    Programa = Estrutura de Dados + Algoritmo

Por exemplo: C

#### Linguagens Orientadas aos Objetos (POO):

A comunicação com o exterior das funções é feita unicamente através dos parâmetros que lhe são passados. Divide o estado global por pequenas estruturas fechadas denominadas objetos.

O que distingue a POO da programação imperativa tradicional é o facto de um programa dever agora ser visto como um conjunto de objetos que são manipulados pelas operações às quais estão intimamente ligados.

    Orientação aos Objetos = Objetos + Classes + Herança
    POO = Orientação aos Objetos + Mensagens

Os objetos devem ser vistos como entidades que encapsulam não apenas dados, mas também operações sobre os dados.

**Herança** é um modo de definir a forma como as novas classes herdam propriedades das classes que lhes estão acima na hierarquia. As **mensagens** são o que permite a comunicação entre objetos. 

![exemplo-POO](/Python/images/whatis-object_oriented_programming_half_column_mobile.png)

Por exemplo: Java


Até pagina: 26

## 02/07/2020

Pagina atual: 27

## Modulos

Quando importamos um modulo temos que prefixar todos os comandos pelo nome do modulo.

    >>> import math
    >>> dir(math)
    ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
    >>> help(math.sin)
    Help on built-in function sin in module math:

    sin(x, /)
        Return the sine of x (measured in radians).

No terminal podemos "estudar" o modulo.

import math - para importar modulos

math.pi - para aceder ao pi no modulo math

dir(math) - inpeciona o que o modulo pode fazer apresentando uma lista no terminal com todos metodos 

help(math.sin) - diz nos o que o metodo faz


## Programa Tartaruga

    import turtle
    turtle.forward(x)
    turtle.left(x)
    turtle.right(x)
    turtle.backward(x)
    turtle.position()
    turtle.heading()
    turtle.goto(100,100)
    turtle.setx(200)
    turtle.ycor()
    turtle.xcor()
    turtle.setheading(225)
    turtle.hideturtle()
    turtle.showturtle()
    turtle.penup()
    turtle.pendown()
    turtle.shape("triangle")
    turtle.exitonclick() - permite controlar o fim da execução do programa através do fecho da janela usada para desenhar

Desenhar polígonos regulares:

    def poligono_regular(comp_lado, num_lados):
    ...     """
    ...     Desenha um polígono regular.
    ...     """
    ...     angulo_viragem = 360 / num_lados
    ...     for i in range(num_lados):
    ...         turtle.forward(comp_lado)
    ...         turtle.right(angulo_viragem)
    ...     turtle.hideturtle()


#### Contrutor

Permite criar um objeto. Se a operação não tiver argumento cria um objeto particular, se tiver argumento, tenta criar um objeto do tipo a partir do objeto fornecido.

[Source:](https://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/#:~:text=A%20constructor%20is%20a%20special,will%20need%20when%20it%20starts.)

>A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts. Constructors can also verify that there are enough resources for the object and perform any other start-up task you can think of.

>The name of a constructor is always the same, __init__(). The constructor can accept arguments when necessary to create the object. When you create a class without a constructor, Python automatically creates a default constructor for you that doesn’t do anything. Every class must have a constructor, even if it simply relies on the default constructor. 

[Source:](https://www.geeksforgeeks.org/constructors-in-python/)

Syntax of constructor declaration :

    class GeekforGeeks: 
    
        # default constructor 
        def __init__(self): 
            self.geek = "GeekforGeeks"
    
        # a method for printing data members 
        def print_Geek(self): 
            print(self.geek) 
    
    
    # creating object of the class 
    obj = GeekforGeeks() 
    
    # calling the instance method using the object obj 
    obj.print_Geek() 
_____
    Output :

    GeekforGeeks

#### Objeto
 
 Tres caracteristica são identidade, valor e tipo

 * Identidade - é o que torna o objeto unico, podendo ser consultado mas não modificado, é uma referência ou um pontador para uma zona da memória na qual se encontra a descrição do objeto
 * Valor - Traduz o estado do objeto num dado movimento.
 * Tipo - Determina o conjunto de valroes que o objeto pode assumir e as operações que com ele podemos fazer.

 Em Python o tipo é uma propriedade do objeto, podendo ser consultado mas não alterado, são implementados como classes.

![objetos](/Python\images\objetos.JPG)
 #### Classes

 É um modelo para descrever o que o conjunto dos objetos da classe partilham, em particular seus atributos, que definem o estado do objeto e as operações que com ele podem ser feitas, definidoras do seu comportamento.

#### Metodo: 

    objeto.método(argumentos)

Quando invocamos um metodo são executadas duas ações: primeiro, vai-se obter o método associado ao objeto através do seu nome; segundo, executa-se o método sobre o objeto, passando-lhe os argumentos, ou seja, fazemos:

    método(objeto, argumentos)

Quando usamos função é so este segundo passo.

#### Functions

Functions that can accept other functions as arguments are also called **higher-order functions**

#### Tipos de Objetos

* Inteiros - 733, -15, 0
* Vírgula Flutuante - 2.46, 3.14e-20, 6e100, 4.0e+120
* Números complexos - 4 + 5j, 4.0 + 5.0j, 6J

Não podemos converter um numero complexo num real.

##### Booleanos

* Verdadeiro (True) - é representado por 1
* Falso (False) - é representado por 0

#### Interpretador

Quando se recorre a um interpretador, este funciona com base num ciclo normalmente designado por **lê - avalia - escreve**: uma expressão é lida, o valor que lhe está associado é calculado e o resultado desse calculo é ecoado. Na aparência, é um ciclo com três passos. No entanto, são na realidade, cinco passos, pois, a seguir á leitura, há uma conversão para um formato interno e, antes da impressão, há a escolha do formato de saida.

#### Bitwise Operation - [Source](https://en.wikipedia.org/wiki/Bitwise_operation#:~:text=In%20computer%20programming%2C%20a%20bitwise,values%20for%20comparisons%20and%20calculations.)

|  Symbol | Operator  |
|---|---|
| &  | bitwise AND  |
|  \| | bitwise inclusive OR  |
| ^	  | bitwise XOR (exclusive OR)  |
| <<  | left shift  |
| >>  | right shift  |
| ~  | 	bitwise NOT (one's complement) (unary)  |  

In computer programming, a bitwise operation operates on one or more bit patterns or binary numerals at the level of their individual bits. It is a fast and simple action, directly supported by the processor, and is used to manipulate values for comparisons and calculations.

##### NOT ( ~ )

The bitwise NOT, or complement, is a unary operation that performs logical negation on each bit, forming the ones' complement of the given binary value. Bits that are 0 become 1, and those that are 1 become 0. For example:

    NOT 0111  (decimal 7)  = 1000  (decimal 8)

The bitwise complement is equal to the two's complement of the value minus one. If two's complement arithmetic is used, then NOT x = -x − 1.

A simple but illustrative example use is to invert a grayscale image where each pixel is stored as an unsigned integer.

##### AND ( & )

A bitwise AND is a binary operation that takes two equal-length binary representations and performs the logical AND operation on each pair of the corresponding bits, which is equivalent to multiplying them. Thus, if both bits in the compared position are 1, the bit in the resulting binary representation is 1 (1 × 1 = 1); otherwise, the result is 0 (1 × 0 = 0 and 0 × 0 = 0).

        0101 (decimal 5)  AND 0011 (decimal 3)  = 0001 (decimal 1)

Because of this property, it becomes easy to check the parity of a binary number by checking the value of the lowest valued bit. Using the example above:

        0110 (decimal 6)  AND 0001 (decimal 1) = 0000 (decimal 0)

Because 6 AND 1 is zero, 6 is divisible by two and therefore even.

##### OR ( | )

A bitwise OR is a binary operation that takes two bit patterns of equal length and performs the logical inclusive OR operation on each pair of corresponding bits. The result in each position is 0 if both bits are 0, while otherwise the result is 1. For example:

    0101 (decimal 5) OR 0011 (decimal 3) = 0111 (decimal 7)

##### XOR ( ^ )

A bitwise XOR is a binary operation that takes two bit patterns of equal length and performs the logical exclusive OR operation on each pair of corresponding bits. The result in each position is 1 if only one of the bits is 1, but will be 0 if both are 0 or both are 1.

    0101 (decimal 5) XOR 0011 (decimal 3) = 0110 (decimal 6)
_________________
    def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: Write your solution here
    xor = [ chr ( ord (a) ^ ord (b) ) for a,b in zip (str1, str2) ]
    count = 0
    for distance in xor:
        if distance != '\x00':
            count += 1
    if len(str1) - len(str2) != 0:
        count = None
    return count
    pass

#### Arithmetic Shift ( << >>)

In an arithmetic shift, the bits that are shifted out of either end are discarded. In a left arithmetic shift, zeros are shifted in on the right; in a right arithmetic shift, the sign bit (the MSB in two's complement) is shifted in on the left, thus preserving the sign of the operand.

This example uses an 8-bit register:

    00010111 (decimal +23) LEFT-SHIFT =  00101110 (decimal +46)
    10010111 (decimal −23) RIGHT-SHIFT =  11001011 (decimal −11)
    
In the first case, the leftmost digit was shifted past the end of the register, and a new 0 was shifted into the rightmost position. In the second case, the rightmost 1 was shifted out (perhaps into the carry flag), and a new 1 was copied into the leftmost position, preserving the sign of the number. Multiple shifts are sometimes shortened to a single shift by some number of digits. For example:

    00010111 (decimal +23) LEFT-SHIFT-BY-TWO = 01011100 (decimal +92)

Até pagina: 76

## 03/07/2020

Pagina atual: 77

## Cadeia de Caracteres

| Escape  | Interpretação  |
|---|---|
| \\\  | Armazena uma barra inclinada  |
|  \b |  Espaçamento atrás |
|  \n |  Muda de Linha |
|  \t |  Tabulação horizontal | 
|  \v |  Tabulação vertical | 

##### Operadores

Concatenação de cadeias de caracteres

    "GAATTC" + "GGATCC" = GAATTCGGATCC

Cópias de superficie de uma cadeia

    "GAATTC" * 2 = GAATTCGAATTC

#### Indexação

![index](/Python\images\index.jpg)

##### Fatiamento [inf : sup] e [inf : sup: step]

    >>> cadeia = "Homem Aranha"
    >>> cadeia[1:4]
    'ome'
    >>> cadeia[-6:-2]
    'Aran'
    >>> cadeia[:5]
    'Homem'
    >>> cadeia[6:]
    'Aranha'
    >>> cadeia[:]
    'Homem Aranha'
    >>> cadeia[::2]
    'HmmAah'
    >>> cadeia[1:7:2]
    'oe '

A posição **inf** inclusive e a posição **sup** exclusive.

Caso o indice inferior seja maior do que indice superior, o resultado será uma cadeia vazia

    >>> cadeia[3:2]
    ''

Podemos nao colocar os indices, se nao pusermos o inferior, significa desde o inicio; se nao pusermos o superior, significa até ao fim.

Para obter uma cadeia inversa de uma dada cadeia de caracteres:

    >>> cadeia[::-1]
    'ahnarA memoH'

##### Print

    <frase_com_formato> % <valores>
    >>> mensagem = "A soma de %d com %d da %d" % ( 1 , 3, 1+3)
    >>> print(mensagem)
    A soma de 1 com 3 da 4

Ao usar "%.0f" vamos imprimir um float com duas casas decimais

#### Operações

| Literal  | Interpretação  |
|---|---|
| cad in s  | Determina se cad é subcadeia de s  |
| max(cad)  | Qual o maior elemento da cadeia  |
| min(cad)  | Qual o menor elemento da cadeia  |
| s.index(cad)  | O indice da primeira ocorrência de cad em s  |
| s.count(cad)  | O número de ocorrências de cad em s  |

    >>> cadeia = "Homem Aranha"
    >>> "ma" in cadeia
    False
    >>> max(cadeia)
    'r'
    >>> min(cadeia)
    ' '
    >>> cadeia.index("a")
    8
    >>> cadeia.count("a")
    2

#### Metodos Especificos

| Método   | Significado  | 
|---|---|
| s.find(cad)  | O indice da primeira ocorrrencia ou -1  |
| s.isalpha()  | Verdadeiro se só letras  |
| s.isdigit()  | Verdadeiro se só digitos  |
| s.center(comprimento)  | Center numa cadeia de comprimento  |
| s.lower()  | Converte para letras minusculas  |
| s.upper()  | Converte para letras maiusculas  |
| s.strip()  | Retira brancos á esquerda e á direita  |
| s.replace(velho,novo)  | Substitui ocorrências de velho por novo  |
| s.endswith(cad)  | Verifica se s termina em cad  |

    >>> cadeia = "TACGAUGGGTCAAUGTCGAT"
    >>> cadeia.find("AUG")
    4
    >>> cadeia.find("AUG",6)
    12
    >>> cadeia.find("AUT",6)
    -1
    >>> cadeia.isalpha()
    True
    >>> cadeia.lower()
    'tacgaugggtcaaugtcgat'
    >>> cadeia.replace("T","U")
    'UACGAUGGGUCAAUGUCGAU'
    >>> nome = "Ernesto J. F. Costa"
    >>> nome.center(50)
    '               Ernesto J. F. Costa                '
    >>> titulo = nome.center(30)
    >>> titulo
    '     Ernesto J. F. Costa      '
    >>> titulo.strip()
    'Ernesto J. F. Costa'
    >>> titulo.upper()
    '     ERNESTO J. F. COSTA      '
    >>> "1234".isdigit()
    True
    >>> "12.34".isdigit()
    False

## Range

Range é um iterator que devolve os elementos de uma sequencia á medida que eles são necessarios, evitando, deste modo, que estejam todos em memoria.

    for i in range(4)
    for i in range(1, 4)
    for i in range(1, 4, 2)

## Tuplos

| Literal  | Interpretação  |
|---|---|
| +  | Concatenação de cadeias de caracteres  |
| *  | Cópias de superficie de uma cadeia  |
| len  | Comprimento de um cadeia  |
| in  | Determina se uma cadeia é subcadeia de outra  |
| max  | Qual o maior elemento da cadeia  |
| min  | Qual o menor elemento da cadeia  |
| index  | O indice da primeira ocorrência  |
| count  | O número de ocorência  |
| [i : j : k]  | Fatiamento  |

    >>> t_1 = (1,2,3)
    >>> t_2 = (4,5,6,7,8,9)
    >>> t_1 + t_2
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> t_1 * 2
    (1, 2, 3, 1, 2, 3)
    >>> len(t_2)
    6
    >>> 4 in t_1
    False
    >>> max(t_1)
    3
    >>> min(t_2)
    4
    >>> t_2[2:5]
    (6, 7, 8)
    >>> t_1.count(3)
    1
    >>> t_2.index(5)
    1
    >>> t_1[-1]
    3
    >>> t_2[0:6:2]
    (4, 6, 8)

##### Imutabilidade

Alterando um objeto alteramos indiretamente outro se ambos partilharem o que foi alterado, reside no facto de os tuplos serem objetos **imutaveis**: não é possivel alterar o seu valor sem alterar a sua identidade, criando, assim um novo objeto

Não é possivel alterar cadeias de caracteres:

    >>> cadeia = "Homem Aranha"
    >>> cadeia[6] = "I"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

Mas podemos contornar:

    >>> cadeia = cadeia[:6] + "I" + cadeia[7:]
    >>> cadeia
    'Homem Iranha'

### Empacotamento

É possivel referirmo-nos a tuplos sem usar a sua marca sintática, os parenteses.

    >>> t_3 = 1,2,3,4
    >>> t_3
    (1, 2, 3, 4)

Da para fazer o inverso:

    >>> conta_1 = ("Ernesto Costa", 59, "Coimbra", 123.45)
    >>> nome, idade, morada, saldo = conta_1
    >>> nome
    'Ernesto Costa'

### Embricamento

    >>> t = ("Coimbra", (40.15, 8.27))
    >>> t[1][0]
    40.15

### Collections

    1 >>> import collections
    2 >>> Cidades = collections.namedtuple("Cidades", "Nomes lat long")
    3 >>> cid_1 = Cidades(Nomes="Coimbra", lat=40.15, long=8.27)
    4 >>> cid_1.Nomes
    5 'Coimbra'
    6 >>> cid_2= Cidades("Lisboa", 38.42, 9.10)
    7 >>> cid_2[1]
    8 38.42

A linha 2 mostra a criação do construtor do tipo, sendo que, neste caso, o nome do construtor é o mesmo do tipo. Este modo de proceder, não sendo obrigatorio representa boa pratica.

Fica tambem claro que podemos aceder aos atributos pelo nome ou da forma usual, e que na criação dos objetos não é obrigatorio usar o nome do atributo.

# Algoritmo - descobre o maior valor e return

[Code - maiorValor.py](Python\exercicios\maiorValor.py)

Até pagina: 115

## 04/07/2020

Pagina atual: 115

Observações: Tive de ressaca no sabado dai não ter feito nenhum estudo

## 05/07/2020

Pagina atual: 115

## Generalidades

Um programa é formado por uma sequencia de comandos. Esses comandos dividem-se em **expressôes, instruções** ou ainda **definições**.

De um modo simples podemos dizer que as instruções fazem coisas. Quando executamos um programa, algumas instruções alteram ou criam objetos e associam esses objetos a nomes, enquanto outras apenas servem para definir a proxima instrução a ser executada.

Ás primeiras chamamos instruções destrutivas e ás segundas instruções de controlo.

No conceito de instruções destrutivas, que alteram as caracteristicas dos objetos presentes no programa. Subdividem-se em três categorias:
* Atribuição;
* Leitura;
* Escrita.

A construção dos nomes em Python obedece a regras: um nome válido tem de começar por uma letra ou pleo caracter _, podendo seguir-se depois letras, digitos e o caracter _, por esta ordem em qualquer número.

Palavras reservadas:

* and 
* continue
* execept
* global 
* lambda
* pass
* while 
* as
* def
* False
* if
* None
* raise
* width
* ...

Quando os nomes são muitos extensos, é normal tornar a sua leitura mais simples. Por exemplo, usar ***peso_total*** em vez de ***pesototal.***

#### Atribuição

Uma atribuição nao é mais do que a associação de um nome a um objeto. Os nomes são criados no momento da primeira atribuição (do nome), passando a fazer parte do espaço de nomes.

A associação de um nome a um objeto pode ser feita de modo indireto:

    >>> x = 5.4
    >>> y = 3
    >>> z = x + y
    >>> z
    8.4

#### Atribuição Implicita

Existem algumas atribuições implicitas. Por exemplo, quando importamos um módulo ou quando definimos uma função .

#### Atribuição Aumentada

    >>> x = 4
    >>> x += 1
    >>> y = 10
    >>> y **=2
    >>> x
    5
    >>> y
    100

#### Outras formas de atribuição

Python permite outros modos de efetuar atribuições: em cadeia ou múltiplas

    >>> a = b =3
    >>> a
    3
    >>> b
    3

Aqui temos que o objeto 3 tem agora dois nomes associados.

    >>> x, y = 5, 7
    >>> x
    5
    >>> y
    7

Trocar o valor de duas variaveis!!

    >>> x, y = y, x
    >>> x
    7
    >>> y
    5

Esta situação pode ser ultrapassada se o nome estiver prefixado com um asterisco.

    >>> x, *y = (5,7,9)
    >>> x
    5
    >>> y
    [7, 9]
    >>> *x,y = (5,7,9)
    >>> x
    [5, 7]
    >>> y
    9
    >>> x,*y,z = (3,5,7,9)
    >>> x
    3
    >>> y
    [5, 7]
    >>> z
    9
    >>> x,*y,z = (5,7)
    >>> x
    5
    >>> y
    []
    >>> z
    7

Os valores prefixados com asterisco ficam associados a um objeto do tipo lista.

#### Leitura

Já sabemos que podemos usar o **construtor** dos diferentes tipos de dados para forçar um objeto a ser convertido, quando tal é possivel, para outro tipo de objeto.

    int()
    str()
    float()

Podemos generalizar esta abordagem usando, não o construtor, mas a função **eval**. A função eval tem como argumento uma cadeia de caracteres que é interpretada como sendo uma expressão.

    >>> idade = eval(input("A sua idade por favor: "))
    A sua idade por favor: 27
    >>> idade
    27

#### Escrita

    >>> print(a, ' + ' ,b, ' = ', a+b, sep='--')
    3-- + --3-- = --6

    >>> a = 2
    >>> print(a, end="")
    2>>> print(a, end="**")
    2**>>> 

Por defeito, é usado o caráter de mudança de linha **\n**. Temos assim, uma sintaxe simples para a função **print**.

    print([expressão,...], sep=" ", end = "\n", file=sys.sdout)

Como se pode concluir, também podemos determinar onde vai ser escrito o resultado indicando o canal de saída, que, por defeito, é o monitor (sys.sdout)

#### Metodo de Formatação 

Baseia-se no uso do metodo **format**, que se aplica a um **modelo** de cadeia de carateres que é instanciada por recurso a argumentos por posição ou por nome. 

    >>> modelo_1 = "{0}, {1} e {2}"
    >>> texto_1 = modelo_1.format("cama", "mesa", "roupa lavada")
    >>> print(texto_1)
    cama, mesa e roupa lavada
    >>> modelo_2 = "{dorme}, {come} e {veste}"
    >>> testo_21= modelo_2.format(come="mesa", veste="roupa lavada", dorme="cama")
    >>> print(testo_21)
    cama, mesa e roupa lavada

## Intruções de controlo

* Instruções de controlo:
    * Sequências
    * Condicionais
    * Ciclos

Operadores Relacionais:

* and
* or
* !=
* not
* in - permite responder se um elemento pertence a uma sequência
* is - permite saber se dois nomes estão associados ao mesmo objeto, isto é, se têm a mesma identidade (adress in memory)

##### Representação de Falso

| Objeto  | Descrição  |
|---|---|
| None  | Nada  |
| 0  | Zero  |
| "  | Cadeia de caracteres vazia  |
| ()  | Tuplo vazio  |
| []  | Lista vazia  |
| {}  | Dicionario vazio  |

### Condicionais

* Simples (uma via)

    if ():

* Normal (duas vias)

    if():
    else:

* Geral (várias vias)
    if():
    elif():
    else:

### Loops

Propriedades que são verdadeiras á entrada do ciclo e no final de cada exceução do cilco. São designadas por **invariantes do ciclo.**

Até pagina: 155

## 06/07/2020

Pagina atual: 155

### Instruções de Controlo

Existem muitas situações em programação em que se justifica interromper um ciclo a meio da sua execução. Essa interrupção pode ser definitiva, isto é, o ciclo é abandonado, ou então parcial, levando apenas ao regresso ao inicio do ciclo.

#### Break

Quando não temos mais nada a fazer e queremos abandonar o teste. A instrução **break** permite-nos realizar esse objetivo de modo elegante.

    >>> def factor_max(y):
    ...     x = y // 2
    ...     while x > 1:
    ...         if y % x == 0:
    ...             print("O maior factor de %d é %d" % (y,x))
    ...             break
    ...         x = x - 1


#### Continue

Há situações em que não queremos interromper o ciclo, mas apenas retomá-lo a partir do inicio. Um exemplo simples é quando queremos filtrar certos casos em que nada acontece de outros em que é preciso fazer algo.

Há um aspecto importante sobre a instrução **continue** que deve ser sublinhada, pois é, muitas vezes mal entendido. A instrução faz voltar para o inicio do ciclo, obrigando ao teste da condição de saida antes de retomar a execução do ciclo, o que só acontece se o teste for verdadeiro.

#### Else

Os ciclos **while** e **for** podem ser enriquecidos através da utilização de uma claúsula **else** a seguir ao ciclo. Associadas a essa cláusula estão instruções que serão executadas caso o ciclo **não** tenha sido interrompido por meio de um **break**.

    >>> def factor_max(y):
    ...     x = y // 2
    ...     while x > 1:
    ...         if y % x == 0:
    ...             print("O maior factor de %d é %d" % (y,x))
    ...             break
    ...         x = x - 1
    ...     else:
    ...     print(y, "é um número primo")

#### Pass

Uma instrução que não faz nada.

* No desenvolvimento de programas. Deste modo, podemos testar partes do programa, deixando para mais tarde completar o que está em desenvolvimento. Consegue-se também isolar melhor eventuais erros no código;
* Quando somos obrigados, por razões **sintáticas**, a colocar uma instrução numa zona do código.
* No tratamento de exceções, assunto que será tratado na próxima secção.

#### Exceções

O proprio utilizador pode incorporar no seu programa código que o ajude a controlar possíveis erros. Esse código baseia-se na ideia de **exceção**.

Um caso simples em que isolamos a situação de uma divisão por zero.

    >>> def try_1(x):
    ...     try:
    ...         y= eval(input("\nDenominador: "))
    ...         print( x / y )
    ...     except ZeroDivisionError:
    ...         print("\nCuidado: o denominador não pode ser zero!")

Um exemplo clássico do uso de excecções envolve a abertura de um ficheiro, como se ilustra a seguir:

    >>> def try_4(x):
    ...     try:
    ...         fich = input("Nome do ficheiro: ")
    ...         f_in = open(fich, "r")
    ...         break
    ...     except IOError:
    ...         print("O ficheiro %s não existe. Tente de novo." % fich)

Neste caso, estamos a pedir o nome de um ficheiro até o mesmo ser válido, altura em que se abandona o ciclo **while**.

Associado a um **try** pode existir mais do que uma cláusula **except**, embora só uma seja ativada (a que corresponder à exceção levantada)

    >>> import sys
    >>>
    >>> try:
    ...     f= open("myfile.txt")
    ...     s = f.readline()
    ...     i = int(s.strip())
    ... except IOError as erro:
    ...     print("I/O error: %s" % erro)
    ... except ValueError:
    ...     print("Os dados não puderam ser convertidos para inteiro.")
    ... except:
    ...     print("Erro inesperado:", sys.exc_info()[0])
    ...     raise

No ultimo **except** não existe nenhuma exceção definida associada e é levantada uma geral (**raise**). O uso de sys.exc_info()[0] destina-se a obter informação que o sistema consegue dar sobre o erro.

Para concluir, importa referir que pode também existir uma cláusula opcional, denominada **finally**, no fim da exceção, que será **sempre** executada independentemente do resultado das operações do **try - except**. Normalmente, é usado para atividades de limpeza, como fechar um ficheiro com segurança.

    >>> def divide_1(x,y):
    ...     try:
    ...        result = x/y
    ...     except ZeroDivisionError:
    ...         print("divisão por zero!")
    ...     else:
    ...         print("o resultado é", reuslt)
    ...     finally:
    ...         print("a executar a cláusula finally")

#### Asserções

Acontece, com alguma frequência, queremos interromper um programa se uma dada condição não se verificar (assert).

    >>> def exe_ass(n):
    ...     assert 7 < n < 77, "valores fora dos limites"
    ...     print(n)
    ... # -- resultado da chamada com n = 100
    AssertionError: Valores fora dos limites

[Source](https://www.programiz.com/python-programming/assert-statement)

Assertions are simply boolean expressions that checks if the conditions return true or not. If it is true, the program does nothing and move to the next line of code. However, if it's false, the program stops and throws an error.

It is also a debugging tool as it brings the program on halt as soon as any error is occurred and shows on which point of the program error has occurred.

    def avg(marks):
        assert len(marks) != 0,"List is empty."
        return sum(marks)/len(marks)

    mark2 = [55,88,78,90,79]
    print("Average of mark2:",avg(mark2))

    mark1 = []
    print("Average of mark1:",avg(mark1))

When we run the above program, the output will be:

    Average of mark2: 78.0
    AssertionError: List is empty.

## Listas

As listas são objetos como tudo em python, logo têm identidade, valor e tipo. Os elementos das listas são separador por vírgulas. A marca sintática das listas são os parênteses retos. São mutaveis e heterogenias

    baleias = [5,4,3,4,2,6,8,4,6]

| Nome  | Operador  | Significado  |
|---|---|---|
| Indexação  | [n]  | Acede  |
| Concatenação  | L1 + L2  | Junta   |
| Repetição  | L * n  | Replica  |
| Pertença  | in, not in  | testa  |
| Comprimento  | len  | Quantifica  |
| Fatiamento  | [ : : ]  | Parte  |

    >>> [1,2,3] [1]
    2
    >>> [1,2,3] + [4,5,6]
    [1, 2, 3, 4, 5, 6]
    >>> ["Ai!"]*4
    ['Ai!', 'Ai!', 'Ai!', 'Ai!']
    >>> len([1,2,3])
    3
    >>> 2 in [1,2,3]
    True
    >>> lista = [1,2,3,4,5,6]
    >>> lista[1:4]
    [2, 3, 4]

O **contrutor** é list()

Os nomes são **referências** para o mesmo objeto. Assim, naturalmente, ao usar um deles para mudar o valor do objeto, o acesso pelo outro nome também encontra o objeto alterado. Este acontecimento pode ter efeitos não desejados. Se nãoo quisermos que este efeito lateral aconteça, uma solução é usar uma **cópia**.

    >>> vogais  = ["A", "E", "I", "O", "U"]
    >>> id(vogais)
    2791287099208
    >>> copia = vogais[:]
    >>> copia
    ['A', 'E', 'I', 'O', 'U']
    >>> id(copia)
    2791287111048

Esta solução não é perfeita, pois apenas as referências de primeiro nivel são alteradas. Assim, se o objeto tiver elementos que sejam listas e alterarmos os elementos destas listas, o problema acontece de novo.

    >>> vogais = ["A", "E", ["I","O"],"U","Z"]
    >>> copia = vogais[:]
    >>> id(vogais)
    2791287120840
    >>> id(copia)
    2791287204424
    >>> copia[2][1] = "AI!"
    >>> copia
    ['A', 'E', ['I', 'AI!'], 'U', 'Z']
    >>> vogais
    ['A', 'E', ['I', 'AI!'], 'U', 'Z']

Para termos a certeza de que não temos nenhuma surpresa, devemos fazer uma **cópia profunda** utilizando o método **deepcopy** do módulo **copy**.

    >>> import copy
    >>> vogais = ["A", "E", ["I","O"],"U","Z"]
    >>> copia= copy.deepcopy(vogais)
    >>> id(vogais)
    2791286880456
    >>> id(copia)
    2791286951304
    >>> copia[2][1] = "AI!"
    >>> copia
    ['A', 'E', ['I', 'AI!'], 'U', 'Z']
    >>> vogais
    ['A', 'E', ['I', 'O'], 'U', 'Z']


| Método  | Operação  |
|---|---|
| list.index(obj, i=0, j = len(list))  | Menor indice da ocorrência do objeto  |
| list.count(obj)  | Conta o número de vezes que obj ocorre em list  |
| list.append(obj)  | Adiciona o objeto no fim da lista  |
| list.extend(seq)  | Junta seq á list  |
| list.insert(index, obj)  | Insere o objeto na posição dada pelo indice  |
| list.remove(obj)  | Retira o objeto da lista  |
| list.pop(index)  | Retira o objeto da lista na posição dada pelo indice  |
| list.reverse()  | Inverte a lista ***in situ***  |
| list.sort(key, reverse)  | Ordena ***in situ*** a lista ***list***  |

O método **append** acrescenta um elemento no final da lista e devolve o objeto **None**

Até pagina: 190

## 30/09/2020

### Listas de Compreensão

A forma mais simples de uma lista por compreensão é:

    [ < expressão> for <item> in <iterável>]

    >>> [i ** 2 for i in [1,2,3]]
    [1, 4, 9]

Existe no entanto, situações em que nos interessa ter acesso ao elemento e a sua posição. Quando isso acontece, podemos usar a função predefinida *enumerate*.

    lista = ["a","b","c"]
    for i,v in enumerate(lista):
        print(i,v)

    Output:
        0 a
        1 b
        2 c

### Dicionarios

Um dicionario é uma coleção não ordenada de pares ordenados de objetos, de comprimento variavel, heterogenea e mutável. A primeira componente do par designa-se por chave e a segunda por valor.

O construtor do tipo dicionario chama-se *dict*

    >>> d_1 = dict
    >>> d_1
    <class 'dict'>
    >>> d_2 = dict.fromkeys([1,2,3])
    >>> d_2
    {1: None, 2: None, 3: None}
    >>> d_3 = dict.fromkeys([1,2,3],0)
    >>> d_3
    {1: 0, 2: 0, 3: 0}
    >>> d_4 = dict(nome= "ernesto", idade = 60)
    >>> d_4
    {'nome': 'ernesto', 'idade': 60}
    >>> d_5 = dict(zip([1,2,3],['a','b','c']))
    >>> d_5
    {1: 'a', 2: 'b', 3: 'c'}
    
    >>> d = {'A': 'Adenina', 'T': 'Timina'}
    >>> 'A' in d
    True
    >>> len(d)
    2
    >>> del d["T"]
    >>> d
    {'A': 'Adenina'}

#### Metodos dicionarios

| Método | Operações |
|---|---|
| Não Modificam| |
|dict.copy() | Devolve uma cópia do dict |
|dict.items() | devolve um iteravel de pares (chaves, valor) de dict|
|dict.keys() | Devolve um iteravel de chaves de dict |
|dict.values() |Devolve um iteravel de valores de dict |
|dict.get(keys, default=None) | Devolve o valor caso exista, senao devolve default |
|Modificam | |
|dict.clear() | Retira todos os elementos de dict |
|dict.pop(key, default=None) | Retira e devolve o elemento de key |
|dict.popitem() | Retira aleatoriamente e devolve um par |
|dict.update(dict2) | Adiciona os pares (chave,valor) de dict2 a dict |
| dict.setdefault(key, default=None) | Como get mas atualiza o par com key:default |

### Exemplos

Para obter a chave a partir do valor:

    def progenitor(arg_gen, pessoa):
        for c,v in arv.gen.items():
            if pessoa in v:
                return c
        return []

### Conjuntos set()

Por definição, um conjunto é uma coleção não ordenada de elementos unicos, heterogénea e mutavél. Como se pode ver, a natureza unica dos elementos é um traço distintivo dos conjuntos. Mas existem outros aspetos importantes que importa desde ja realçar.

A implementação dos conjuntos baseia-se em **tabelas de hash**: o nome associado ao objeto determina a sua localização em memória, pois existe uma função(dita função de hash) que efetua esse mapeamento.

Nota-se então que um conjunto é um objeto mutável formado por elementos imutáveis, ou seja, pode se ampliar, eliminar, mas nao pode modificar elementos.

    >>> c_2 = set('123')
    >>> c_2
    {'2', '3', '1'}
    >>> c_3 = {1,2,3}
    >>> c_3
    {1, 2, 3}
    >>> c_4 = { x**2 for x in [1,2,3]}
    >>> c_4
    {1, 4, 9}
    >>> {1,2,3} == {3,2,1}
    True

#### Metodos set

| Método | Operações |
|---|---|
| Não Modificam| |
|set.copy() | faz uma copia de superficia do conjunto |
|set.issubset() | um conjunto é subconjunto de outro|
|set.union(set) | Cria um novo conjunto igual á uniao |
|set.intersection() | Cria um novo conjunto igual á intersecção |
|set.difference(set) | Cria um novo conjunto com a diferença |
|Modificam | |
|set.pop() | Retira um elemento que é devolvido |
|set.clear() | Retira todos os elementos do conjunto |
|set.add(elemt) | Acrescenta o elemento ao conjunto |
| set.discard(elemt) | Retira o elemento |
| set.remove(elem) | Retira o elemento se nao exsitir dá erro |

#### zip method

    >>> list_1 = [1,2,3]
    >>> list_2 = [4,5,6]
    >>> junta = zip(list_1, list_2)
    >>> junta
    <zip object at 0x03663EC8>
    >>> next(junta)
    (1, 4)
    >>> next(junta)
    (2, 5)
    >>> next(junta)
    (3, 6)
    >>> for element in zip(list_1,list_2):
        print(element)

        
    (1, 4)
    (2, 5)
    (3, 6)
    >>> list_3 = [7,8,9]
    >>> list(zip(list_1, list_2, list_3))
    [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    >>> list(zip(list_1))
    [(1,), (2,), (3,)]
    >>> 

Até pagina: 222

## 30/09/2020

Pagina atual: 223

### Ficheiros - Capitulo 7

    meu_ficheiro = open("toto.txt", "r")

No exemplo anterior apenas tivemso de indicar o nome do ficheiro, porque este estava na zona de trabalho corrente. Podemos ter de indicar o caminho absoluto para o ficheiro, caso ele esteja noutro local. Nesta situação o modo de indicar o caminho depende da plataforma que estivermos a usar. 

Windows:

    meu_ficheiro = open(r'c:\caminho\para\ficheiro\toto.txt', 'r')
    meu_ficheiro = open('c:\\caminho\\para\\ficheiro\\toto.txt', 'r')

Nota-se que se prefixarmos a cadeia de carateres que indica o caminho com **r** podemos usar a notação habitual; caso contrário, temos de usar duas barras para trás.

É boa pratica de programação fechar qualquer ficheiro que já não esteja a ser usado. Para tal, usa-se a operação de close, aplicada ao nome associado ao ficheiro:

    meu_ficheiro.close()

#### Leitura

| Operador| Interpretação|
|---|---|
| read()| Lê todo o ficheiro de uma só vez|
| read(N) | Lê N bytes|
|readline()| lê a proxima linha do ficheiro (incluindo\n)|
| readlines()| Lê e guarda como sequencia de linhas (cada linha com \n)|

Quando mandamos ler por exemplo 8 bytes, aseguir quando pedirmos a leitura de uma linha do ficheiro esta é feita a partir do local em que a janela ficou depois de serem lidos os 8 bytes.

#### Escrita

A sintaxe geral do comando de escrita é:

    <ficheiro>.write(<cadeia_de_caracteres>)

| operador | interpretação|
|---|---|
|write(str)| Escreve a cadeia de caracteres num ficheiro|
|writelines(seq) | Escreve seq como sequência de linhas|

Devemos ter em atenção que, quando se abre um ficheiro para escrita (modo 'w'), caso o ficheiro já exista, o mesmo é destruido. Para tal não aconteça, temos de abrir o ficheiro em modo de acrescentar (modo 'a').

#### Navegar

Tratemos agora do problema de querer ler ou escrever em determinadas partes do ficheiro. Tal obriga a ter comandos que controlem o posicionamento da janela sobre o ficheiro. O comando **tell**, que nos indica a posição da janela relativamente ao inicio do ficheiro, e o comando **seek**, que nos permite reposicionar a janela. O funcionamento deste último comando depende do tipo de ficheiro (binário ou de texto)

| Nome| Operador| Interpretação|
|---|---|---|
|seek| fich.seek(pos, como=0)| Movimenta para uma nova posição|
|tell| fich.tell()| Indica a posição relativamente ao inicio|

##### Exemplo

Texto ficheiro:

    um ficheiro pequeno,
    com carateres estranhos.

    para testar a leitura \n de
    ficheiros. 
    e outras coisas \t mais!

Codigo:

    >>> f_ent = open('/data/ficheiro.txt','r')
    >>> bytes = f_ent.read(8)
    >>> bytes
    'um fiche'
    >>> f_ent.seek(6)
    6
    >>> mais_bytes = f_ent.read(10)
    >>> mais_bytes
    'heiro pequ'
    >>> f_ent = seek(0,2)
    111
    >>> novos_bytes = f_ent.read(5)
    >>> novos_bytes
    ''
    >>> f_ent.tell()
    111
    >>> f_ent.seek(0)
    0
    >>> ler_tudo = f_ent.read()
    >>> ler_tudo
    ' um ficheiro pequeno, \ncom carateres estranhos. \n\npara testar a leitura \\n de \nficheiros. \ne outras coisas \\t mais!'


#### Modos de abertura de ficheiros de texto binario

| Modo | Interpretação|
|---|---|
|r| Modo de Leitura|
|w| Modo de escrita|
|a| modo de acrescentar|
|r+| Modo de leitura e escrita sem truncamento|
|w+| Modo de leitura e escrita com truncamento|

#### Ficheiros de texto e unicode

No entanto, a probabilidade de ter de lidar com ficheiro que possuem caracteres não ASCII é muito elevada. A versão 3 de python resovleu o problema maior ao automatizar a codificação e a descodificação dos carateres não ASCII, através da instrução open.

    >>> f_out = open('data/unicode.txt','w', encoding='utf-8')
    >>> f_in = open('data/unicode.txt','r', encoding='utf-8')

#### A Instrução with

Gestores de contexto são objetos que têm associadas duas operações, uma de entrada e outra de saida, operações essas que são executadas quando se entra ou se sai de um contexto, respetivamente. A instrução **with** define um contexto, tendo como sintaxe:

    with expressão as var:
        bloco

    with open(ficheiro, 'r') as meu_fich:
        bloco

Deste modo, temos a garantia de que, mesmo que ocorra um erro durante a execução do bloco, o ficheiro será fechado.

#### Formatação por linhas

    >>> f_ent = open('/data/ficheiro.txt','r')
    >>> for linha in f_ent:
        print(linha)

    um ficheiro pequeno,

    com carateres estranhos.


    para testar a leitura \n de

    ficheiros. 

    e outras coisas \t mais!
    >>> for linha in f_ent:
        print(linha, end=' ')
    # Resolve o problema de dois espaços

#### Modos r+ e w+ 

Já referimos a possibilidade de abrir um ficheiro simultaneamente para leitura e escrita. A diferença entre os modos r+ e w+ é que o primeiro escreve por cima do ficheiro, enquanto o segundo limpa o conteúdo do ficheiro.

#### Sumario capitulo

Neste capitulo estivemos concentrador no conceito de ficheiro e nas operações que com ele podemos fazer: leitura, escrita e navegação. Usamos esta oportunidade para introduzir a instrução *with*, o tipo de dados *byte* e ainda os modulos *csv, urllib e gzip*.

Até pagina: 260

## 30/09/2020

Pagina atual: 261

### Visões - Capitulo 8

#### Abstração

Principio da abstração é baseada na ideia de que só a função é que muda. O objetivo é ter uma unica definição para todos os casos.

#### Sumario Capitulo

Neste capitulo introduzimos alguns conceitos sobre imagens, o modo como podem ser representadas e várias maneiras de as processar. Pusemos em relevo a existencia de um padrão que envolve a travessia das imagens através de dois ciclos for. Discutimos ainda alguns aspetos de abstração procedimental que se traduziu no uso de funções passadas como parametros. Introduzimos o modulo *cImage*, os seus tipos e operações. Introduzimos ainda o formato de imagem PPM e mostrámos algumas manipulações de conversão simples.


Até pagina: 304

## 30/09/2020

Pagina atual: 305

### Recursividade - Capitulo 9

#### Exemplos:

    def fib(n):
        """ Número de Fibonacci recursivo"""
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    def anagrama(cad):
        """ Verifica se a cadeia de caracteres é um anagrama, roma/amor ou lapa/pala"""
        if cad == '':
            return [cad]
        else:
            resp = []
            for perm in anagrama(cad[1:]):
                for pos in range(len(perm) + 1):
                    resp.append(perm[:pos] + cad[0] + perm[pos:])
            return resp

##### Ordenamento por fusão

Baseia-se num principio semelhante ao da procura binaria: dividir a sequencia ao meio, ordenar cada uma das partes recursivamente e depois fundir as duas subsequências.


    from copy import deepcopy

    def ordena_fusao(seq, esquerda, direita):
            """ Dividir a sequencia ao meio. Ordenar cada uma das partes separadamente. Depois fundir as duas partes"""
            if esquerda == direita:
                return [seq[esquerda]]
            else:
                seq = deepcopy(seq)
                meio = (esquerda + direita)// 2
                seq_esq = ordena_fusao(seq, esquerda, meio)
                seq_dir = ordena_fusao(seq, meio + 1 , direita)
                return fusao(seq_esq, seq_dir)

    def fusao(seq1, seq2):
        seq = []
        p_1 = 0
        p_2 = 0
        while (p_1 < len(seq1)) and (p_2 < len(seq2)):
            if seq1[p_1] < seq2[p_2]:
                seq.append(seq1[p_1])
                p_1 = p_1 + 1
            else:
                seq.append(seq2[p_2])
                p_2 = p_2 + 1
        if p_1 == len(seq1):
            seq.extend(seq2[p_2:])
        else:
            seq.extend(seq1[p_1:])
        return seq


##### Ordenamento rapido

Deve o seu nome a ser, em certas circusntancias, o método de ordenamento mais rapido. Escolhe-se um seu elemento para pivô e divide-se a sequencia inciial em duas subsequencias ficando numa, a direita, todos os elementos maiores do que o pivô e na outra, á esquerda, todos os elementos menores do que o pivô.

    def quicksort(seq, inicio, fim):
        """ Quick Sort"""
        if inicio < fim:
            divisor = particao(seq, inicio, fim)
            quicksort(seq, inicio, divisor)
            quicksort(seq, divisor + 1, fim)
        return seq

    def particao(lista, esquerda, direita):
        """ Divide a lista em duas metades em torno de um elemento (pivô).
        A divisão é feita de modo que todos os elementos menores (maiores) ou iguais ao pivô estão à
        esquerda (direita) da lista. Devolve o indice que separa a parte esquerda da direita."""
        pivot = lista[esquerda]
        p_esq = esquerda
        p_dir = direita
        while True:
            while lista[p_dir] > pivot:
                p_dir = p_dir + 1
            while lista[p_esq] < pivot:
                p_esq = p_esq + 1
            if p_esq < p_dir:
                lista[p_esq], lista[p_dir] = lista[p_dir], lista[p_esq]
                p_esq = p_esq + 1
                p_dir = p_dir - 1
            else:
                return p_dir


#### Memorização

O acesso a memoria deve ser eficiente, sob pena de se perder no acesso o que se ganha por nao se ter de (re)fazer os calculos. Para tal, vamos recorrer a um dicionario: a chave será n e o valor fib(n)

    def fibonacci(n, res={}):
        if n == 1 or n == 2:
            return 1
        else:
            if n in res:
                return res[n]
            else:
                fib_n = fibonacci(n-1, res) + fibonacci(n-2, res)
                res[n] = fib_n
                return fib_n

Os mecanismos de memorização pode ser implemntado recorrendo ao modulo *functools*

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    if __name__ == '__main__':
        for i in range(1,11):
            print(fib(i))



Até pagina: 342

## 30/09/2020

Pagina atual: 343

### Complementos - Capitulo 10















# Teste cohecimentos

## 1º Capitulo

Perguntas dadas no final do capitulo e as suas respotas

1. Quais as componentes de base da arquitetura de um computador?
    
R: São as seguintes: Dispositivo de entrada (rato/ teclado), CPU, Memória interna (RAM), Memória externa (disco rigido), Dispositivos de Saida (Monitor)

2. Compiladores e interpretadores: o que são e quais as diferenças entre eles?

R: Compiladores, é um programa que transforma a linguagem de programação como por exemplo c o clang, em linguagem máquina e depois é que executa. E um interpretadore executa diretamente a partir da source do programa

3. Que tipo de paradigmas de programação conhece? o que os distingue?

R: 
* Linguagem Declarativa ou relacionais - as linguagens declarativas têm uma natureza declarativa, significando isto que programar não envolve a indicação do modo como a solução se obtem mas apenas a definição do que é a solução.
* Linguagens Funcionais - é formado por um conjunto de funções relacionadas entre si.
* Linguagens Imperativas - Um programa procedimental é caracterizado por uma sequência de instruções que atuam sobre os dados (variáveis), alterando de forma destrutiva o seu valor, ou sobre a ordem pela qual as instruções são executadas (instruções de controlo)
* Linguagem Orientadas aos objetos - o facto de um programa dever agora ser visto como um conjunto de objetos que são manipulados pelas operações às quais estão intimamente ligados.

4. O que são módulos, expressões, instruções e objetos?

[Site com os conceitos](https://panda.ime.usp.br/pensepy/static/pensepy/02-Conceitos/conceitos.html)

R: 
* Modulos são ficheiros com código que permitem aumentar as capacidades da linguagem de base.
* Expressões é uma combinação de valores, variáveis, operadores e chamadas de funções
* Instruções que o interpretador pode executar
* Objetos, também conhecido como valor. Objetos são elementos fundamentais. Programas são projetados para manipular esses elementos (ou programadores dão ordens para que operações sejam realizadas sobre eles).

5. O que entende por parâmetros formais?

[Site com os conceitos](http://excript.com/python/parametro-de-funcao-python.html)

R: Parâmetro é uma variável declarada no cabeçalho da função e tem uso exclusivo dentro do bloco de instrução da mesma.

6. O que faz a instrução de atribuição (=)

R: Atribui a variavel do lado direito (objeto) o valor do lado direito

7. Que instruções de controlo conhece e para que servem?

R:
* Instruções de atribuição - da ao objeto um valor
* Instruções de controlo - if-then-else, sao instruções que nao alteram o estado dos objetos e se limitam a indicar a parte que deve ser executada

8. O que entende pelo modelo PCAP?

R: Primitivas, Composição, Abstração e Padrões.
* Primitivas - + * < =  (numeros, cadeias, caracteres)
* Composição - if for (Listas, dicionários, conjuntos)
* Abstração - def (classes)
* Padrões - Funções de segunda ordem (funções genericas)

9. O que entende por ciclo lê - avalia - escreve?

[Site com os conceitos](https://www.freecodecamp.org/news/this-is-why-your-read-eval-print-loop-is-so-amazing-cf0362003983/)

[Site com os conceitos](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)

R: Interactive computer programming environment that takes (read) single user inputs (i.e., single expressions), evaluates (executes/ write) them, and returns the result to the user and then go back to the start to read your next input.

## 2º Capitulo

1. O que entende por construtor?

R: It instantiates an object using the definitions found in your class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts.

2. Quais são as operações básicas sobre tartarugas?

R: 
    turtle.forward(x)
    turtle.left(x)
    turtle.right(x)
    turtle.backward(x)

3. De que modo se definem novas formas de tartaruga?

R: turtle.shape("triangle")

4. Quais são as operações básicas sobre caneta?

R:
* turtle.penup()
* turtle.pendown()

5. O que distingue uma função de um método?

R: Num método primeiro, vai-se obter o método associado ao objeto através do seu nome; segundo, executa-se o método sobre o objeto, passando-lhe os argumentos. Numa função so se faz o segundo passo.

6. Como podemos controlar a escala do nosso desenho?

R: setworldcoordinates ( canto inferior esquerdo, canto inferior esquerdo, canto superior direiro, canto superior direiro)

    setworldcoordinates(-math.pi, -2 , math.pi, 2)

7. Qual é a finalidade de exitonclick()?

R: Permite controlar o fim da execução do programa através do fecho da janela usada para desenhar

8. Porque podemos usar funções como argumentos de funções e que consequências existem desse facto?

R: Podemos usar porque em python tudo são objetos, inclusive funções. Functions that can accept other functions as arguments are also called higher-order functions

## 3º Capitulo

1. O que entende por programação descendente?

R: Também chamada de construção do topo para a base: decompôe-se um dado problema em subproblemas, cada um dos quais é resolvido usando a mesma abordagem reducionista, até chegarmos a problemas que se podem resolver de modo direto com as construções da linguagem.

2. O que são objetos imutáveis?

R: São objetos em que nao podemos alterar o valor deles. No momento em que são declarados os valores nao podem voltar a ser alterados.

3. Qual é a diferença entre a função range com um argumento, dois argumentos ou três argumentos?

R: A função range só com um elemento, vai de ate esse elemento (< elemento), com dois argumentos vai do primeiro parametro ate ao segundo parametro (1ºparametro >= && 2ºparametro < ) e com terceiro parametro é igual mas o terceiro parametro é de quanto em quanto vai ser passado (3º parametro = 2, entao vai ser de 2 em 2)

4. O que é uma variável com o papel de contador?

R: Uma variavel com papel de contador serve para conseguirmos manipular as vezes que percorre num loop, podemos começar com o valor que queremos e criar uma condição que faz com que saia do loop graças ao contador

5. O que é uma variavel com o papel de acumulador?

R: Serve para acumular informação dentro de um loop, por exemplo uma variavel do tipo de string é inicializada sem nada e ao longo do loop vai sendo preenchida

6. Como se pode modificar uma cadeia de carateres obtendo uma nova?

R: Uma cadeia de caracteres é imutavel, dai a maneira de alterar é criar um novo valor a variavel, como se pode ver na linha 500.

7. O que significa fatiamento?

R: Fatiamento é dado pelo proprio nome, significa conseguir fatiar a cadeia de caracteres em varias fatias, de acordo como queremos, para podermos manipular os dados como queremos.

8. Qual é o construtor do tipo cadeia de carateres?

R: O construtor é **str** que transforma algo numa cadeia de caracteres.

9. Que diferenças existem entre os métodos find e index?

R: O método find tenta encontrar o que colocamos, caso nao encontre devolve -1, caso encontre apresenta o index onde começa a sequencia de caracteres que queremos. O metodo index caso nao exista na cadeia apresenta um erro. 

## 4º Capitulo

1. Qual o siginificado de estado? E de computação?

R: Num dado instante, os objetos têm um determinado conjunto de caracteristicas (valor, tipo, identidade) e o programa encontra-se a executar uma dada instrução. Afirmamos que o programa se encontra num dado **estado**. A sequência de estados por que vai passando o programa ao longo do tempo constitui uma **computação**. 

2. Que palavras reservadas existem em Python? Qual é a sua função e importância?

R: Algumas delas são:

* False
* True
* def

A sua importancia é dos metodos que elas proprias "chamam" ao serem implementadas no codigo

3. O que significa dizer que Python é uma linguagem não tipada e que o tipo associado a um objeto é determinado dinamicamente?

R: Uma linguagem não tipada significa que nao temos explicitamente indicar que tipo é que se refere o valor (int, float, string, char, ...) e que o  objeto pode alterar de tipo sem que tenha que ser transformado.

4. Que consequencias práticas existem de a tipagem ser dinâmica?

R: Ao longo do programa podemos alterar a variavel sem o problema de alterar o tipo, dando mais flexibilidade ao programador mas tambem mais azo a erro.

5. Como define o conceito de atribuição?

R: Uma atribuição é uma associação de um nome a um objeto

        dna = "GAATC

6. Que formas de atribuição conhece?

R: 
* Atribuição Implicita - quando importamos um mõdulo onde ja estão presentes atribuições
* Atribuição Aumentada - os objetos aparecem á esquerda e á direita do sinal de atribuição (x += 1)
* Atribuição em cadeia ou multiplas (a = b = 3 || x,y = 5, 7)

7. De que maneiras se pode introduzir dados num programa? E de que maneira se pode retirar resultados?

R: Atravez da função input() pode-se introduzir dados e através do return pode se retirar resultados

8. Como funciona a instrução input? Funciona como qualquer tipo de objeto?

R: A intrução input transforma qualquer tipo de input numa cadeia de caracteres.

9. Qual é a diferença entre formar a saída por recurso a uma expressão ou ao método **format**?

R: Ao formar uma saida por recurso a uma expressao teremos que introduzir o texto e as os valores separados por "" e virgulas, com o modo format introduzimos o modelo que queremos introduzir as variaveis entre {} e dando index podemos introduzir varios valores. 

## 4º Capitulo

1. O que entende por bloco e como é que este se relaciona com a indentação do código?

R: Um bloco de codigo é um grupo de instruções que podem ser executadas. Para significar que um conjunto de instruções pertence ao mesmo bloco, usa-se o mecanismo de **indentação**

2. De que maneira pode representar os valores booleanos **True** e **False**?

R: 
* True:
    * 1
* False:
    * 0
    * ""
    * ()
    * None

3. Que tipos de instruções condicionais existem e como se distinguem?

R: 
* Condições Simples (uma via)
* Condições Normais (duas vias, sim ou nao)
* Geral (várias vias, complexidade de sim ou nao)

4. Qual é a diferença fundamental entre um ciclo **for** e um ciclo **while**?

R: Um ciclo for é colocado num sentido de sequência que queremos percorrer, ja sabemos o que queremos percorrer e até onde. O ciclo while é sempre verificado uma condição para repetir, se a condição for satisfeita sai do ciclo.

5. De que modo pode percorrer um ciclo?

R: Pelo seu **conteúdo** que percorre o seu proprio contéudo (for ch in seq:). Ou pelo **índices** (for i in range(len(seq)):)

6. Que formas tem de interromper/quebrar um ciclo?

R: 
* Break
* Pass

7. Em que principio se baseia o método de Monte Carlo?

R: Baseia-se no método **estocástico**, que pode ser usado para calcular o valor aproximado de pi. Consiste em simular o lançamento de dardos na direção que queremos, contar a proporção dos que caem dentro do quadro de circunferência ou curva.

8. Que diferenças existem entre **exceções** e **asserções**?

R: Excecões nao param o programa, apresentam o erro. As asserções terminam o programa apresentando o erro.

# Python Sintax

    >>> altura = eval(input("altura:"))
    altura:1.81
    >>> peso = (72.7 * altura) - 58
    >>> print(peso)
    73.58700000000002

print() - imprime e default é aseguir quebra a linha

input() - solicita a introdução de dados

eval() - permite interpretar o dado introduzido (se nao colocarmos o valor introduzido tera o tipo de string, neste exemplo senao coloca se iria dar erro pois seria um float * string)

for i in range(5): - vai repetir de 0 a 4

import math - para importar modulos

math.pi - para aceder ao pi no modulo math

dir(math) - inpeciona o que o modulo pode fazer apresentando uma lista no terminal com todos metodos 

help(math.sin) - diz nos o que o metodo faz

random.randint(0,100) - numero aleatorio de 0 a 100 (import random)

    >>> 1.0/2
    0.5
    >>> 1.0//2
    0.0

1.0 // 2 - ao usar // dois seguidos vai fazer a divisão e como numero inteiro

None - ausência de valor

pow(x, y) - devolve a potencia do primeiro elevada ao segundo

not x - A negação logica em python

!= - Desigual (valor)

is - Igual identidade (adress memoria)

is not - Desigual identidade (adress memoria)

ord("A") = 65 (ASCII)

chr(65) = "A" (ASCII)

len("A") = 1

str(1) = "1"

max() with iterable arguments

    max(iterable, *iterables, key, default)

    max() Parameters:
    iterable - an iterable such as list, tuple, set, dictionary, etc.
    *iterables (optional) - any number of iterables; can be more than one
    key (optional) - key function where the iterables are passed and comparison is performed based on its return value
    default (optional) - default value if the given iterable is empty

type() - indica o tipo da variavel (int / float/ ...)

"sebastian thrun".title() - ill uppercase the begining of the word

"one fish, two fish".count(fish) - ill count the many times "fish" appear in the string

# Exemplos

### Variaveis

However, the above isn't a great way to assign variables in most cases, because our variable names should be descriptive of the values they hold.

    x, y, z = 2 , 3, 5

Besides writing variable names that are descriptive, there are a few things to watch out for when naming variables in Python.

1. Only use ordinary letters, numbers and underscores (snake_case or camelCase) in your variable names. They can’t have spaces, and need to start with a letter or underscore.

2. You can’t use reserved words or built-in identifiers

### Erros

In general, there are two types of errors to look out for

Exceptions
Syntax
An Exception is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it. 

### Method Strings

[Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)

One important string method: format()
We will be using the format() string method a good bit in our future work in Python, and you will find it very valuable in your coding, especially with your print statements.

We can best illustrate how to use format() by looking at some examples:

Example 1

    print("Mohammed has {} balloons".format(27))

Example 1 Output

    Mohammed has 27 balloons

    Here are some examples for the .split() method.

A basic split method:

    new_str = "The cow jumped over the moon."
    new_str.split()

Output is:

    ['The', 'cow', 'jumped', 'over', 'the', 'moon.']

Here the separator is space, and the maxsplit argument is set to 3.

    new_str.split(' ', 3)

Output is:

    ['The', 'cow', 'jumped', 'over the moon.']

Definition and Usage

The rfind() method finds the last occurrence of the specified value.

## Lists

You can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.

    list_of_random_things = [1, 3.4, 'a string', True]
    >>> list_of_random_things[-1] 
    True
    >>> list_of_random_things[-2] 
    a string

### Useful Functions for Lists I

len() returns how many elements are in a list.

max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.

min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.

sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.

Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

    new_str = "\n".join(["fore", "aft", "starboard", "port"])
    print(new_str)

A helpful method called append adds an element to the end of a list.

    letters = ['a', 'b', 'c', 'd']
    letters.append('z')
    print(letters)

Output:

    ['a', 'b', 'c', 'd', 'z']

## Dictionary

get with a Default Value

Dictionaries have a related method that's also useful, get(). get() looks up values in a dictionary, but unlike looking up values with square brackets, get() returns None (or a default value of your choice) if the key isn't found. If you expect lookups to sometimes fail, get() might be a better tool than normal square bracket lookups.

    >>> elements.get('dilithium')
    None
    >>> elements['dilithium']
    KeyError: 'dilithium'
    >>> elements.get('kryptonite', 'There\'s no such element!')
    "There's no such element!"

### Building Dictionarys

Method 1: Using a for loop to create a set of counters

Let's start with a list containing the words in a series of book titles:

    book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

Step 1: Create an empty dictionary.

    word_counter = {}

Step 2. Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1.

    for word in book_title:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

Another way to loop (with get()):

Step 2. Iterate through each element, get() its value in the dictionary, and add 1.

Recall that the dictionary get method is another way to retrieve the value of a key in a dictionary. Except unlike indexing, this will return a default value if the key is not found. If unspecified, this default value is set to None. We can use get with a default value of 0 to simplify the code from the first method above.

    for word in book_title:
        word_counter[word] = word_counter.get(word, 0) + 1

What's happening here? 

* The for loop iterates through the list as we saw earlier. The for loop feeds 'great' to the next statement in the body of the for loop.
* In this line: word_counter[word] = word_counter.get(word,0) + 1, since the key 'great' doesn't yet exist in the dictionary, get() will return the value 0 and word_counter[word] will be set to 1.
* Once it encounters a word that already exists in word_counter (e.g. the second appearance of 'the'), the value for that key is incremented by 1. On the second appearance of 'the', the key's value would add 1 again, resulting in 2.

Iterating Through Dictionaries with For Loops

    cast = {
            "Jerry Seinfeld": "Jerry Seinfeld",
            "Julia Louis-Dreyfus": "Elaine Benes",
            "Jason Alexander": "George Costanza",
            "Michael Richards": "Cosmo Kramer"
        }

If you wish to iterate through both keys and values, you can use the built-in method items like this:

    for key, value in cast.items():
        print("Actor: {}    Role: {}".format(key, value))

This outputs:

    Actor: Jerry Seinfeld    Role: Jerry Seinfeld
    Actor: Julia Louis-Dreyfus    Role: Elaine Benes
    Actor: Jason Alexander    Role: George Costanza
    Actor: Michael Richards    Role: Cosmo Kramer

## Set

Sets are a mutable collection of distinct (unique) immutable values that are unordered.

You can initialize an empty set by using set().

emptySet = set()
To intialize a set with values, you can pass in a list to set().

dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])

![Data Structures - Python](/Python\images\data_structures.png)

## Boolean

By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

Here are most of the built-in objects that are considered False in Python:

* constants defined to be false: None and False
* zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
* empty sequences and collections: '"", (), [], {}, set(), range(0)

Example:

    errors = 3
    if errors:
        print("You have {} errors to fix!".format(errors))
    else:
        print("No errors to fix!")

In this code, errors has the truth value True because it's a non-zero number, so the error message is printed. This is a nice, succinct way of writing an if statement.

## Break, Continue

Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

break terminates a loop
continue skips one iteration of a loop


## Python Generators

A generator in Python is similar to a function except instead of returning a value and exiting a process, a generator will pause the process, saving its state for next time. The biggest difference between a function and generator from a code perspective is one word: return is changed to yield.

To create the next successive even number simply call next() on the generator object, and it will yield the next iteration. After yield is called, everything in the state of the generator function freezes, and the value is returned. When the generator is called again with next(), it picks back up right where it stopped at yield from before.

    # Definition of the generator to produce even numbers.
    def all_even():
        n = 0
        while True:
            yield n
            n += 2

    my_gen = all_even()

    # Generate the first 5 even numbers.
    for i in range(5):
        print(next(my_gen))

    # Now go and do some other processing.
    do_something = 4
    do_something += 3
    print(do_something)

    # Now go back to generating more even numbers.
    for i in range(100):
        print(next(my_gen))

## Zip and Enumerate

#### Zip

zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

You could unpack each tuple in a for loop like this (it can be more that two values).

    letters = ['a', 'b', 'c']
    nums = [1, 2, 3]

    for letter, num in zip(letters, nums):
        print("{}: {}".format(letter, num))

In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

    some_list = [('a', 1), ('b', 2), ('c', 3)]
    letters, nums = zip(*some_list)

#### Enumerate

enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

    letters = ['a', 'b', 'c', 'd', 'e']
    for i, letter in enumerate(letters):
        print(i, letter)

This code would output:

    0 a
    1 b
    2 c
    3 d
    4 e

#### List Comprehensions

Opção demorada:

    cities = ["new york city", "mountain view", "chicago", "los angeles"]

    capitalized_cities = []
    for city in cities:
        capitalized_cities.append(city.title())

    print(capitalized_cities)

Opção list comprehensions:

    cities = ["new york city", "mountain view", "chicago", "los angeles"]

    capitalized_cities = [city.title() for city in cities]

Outro exemplo com conditionals:

So com o if:

    square = [x**2 for x in range(9) if x % 2 == 0]

Com if e else:

    square = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]


## Functions

#### Default Arguments

We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
In the example above, radius is set to 5 if that parameter is omitted in a function call. If we call cylinder_volume(10), the function will use 10 as the height and 5 as the radius. However, if we call cylinder_volume(10, 7) the 7 will simply overwrite the default value of 5.

#### Scope

Variables defined outside functions, as in the example below, can still be accessed within a function. Here, word is said to have a global scope.

    # This works fine
    word = "hello"

    def some_function():
        print(word)

    some_function()

Notice that we can still access the value of the global variable word within this function. However, the value of a global variable can not be modified inside the function. If you want to modify that variable's value inside this function, it should be passed in as an argument. You'll see more on this in the next quiz.

#### DocString

    """
    This is an example of Google style.

    Args:
        param1: This is the first param.
        param2: This is a second param.

    Returns:
        This is a description of what is returned.

    Raises:
        KeyError: Raises an exception.
    """
_____________
    def readable_timedelta(days):
        """
        Return a string of the number of weeks and days included in days.

        Parameters:
        days -- number of days to convert (int)

        Returns:
        string of the number of weeks and days included in days
        """
        weeks = days // 7
        remainder = days % 7
        return "{} week(s) and {} day(s)".format(weeks, remainder)


#### Lambda Expressions

Function that doesnt have name.

    # Funtion:
    def double(x):
        return x * 2
    
    # Lambda:
    double = lambda x: x * 2

Exemplo:

    numbers = [
                [34, 63, 88, 71, 29],
                [90, 78, 51, 27, 45],
                [63, 37, 85, 46, 22],
                [51, 22, 34, 11, 18]
            ]

    def mean(num_list):
        return sum(num_list) / len(num_list)

    averages = list(map(mean, numbers))
    print(averages)

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().

    averages = list(map(lambda x : sum(x)/ len(x), numbers))

## Error and Exceptions

[Exceptions in Python](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

There are two kinds of errors in Python - syntax errors and exceptions. Syntax errors occur when you don't use correct syntax and Python doesn't know how to run your code. Exceptions occur when Python runs into unexpected situations while executing your code and can happen even if you used correct syntax.

### Try Statement

We can use try statements to handle exceptions. There are four clauses you can use.

* try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
* except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
* else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
* finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

        while True:
            try:
                x = int(input("Enter a number: "))
                # Breaks out of the loop if right input
                break
            # If a ValueError is called (input = "dasdsads" )
            except ValueError:
                print("That\'s not a valid number!")
            # if ctrl + c for example or enter
            except KeyboardInterrupt:
                print("\nNo input taken")
                break
            # It ill always run this part of the code:
            finally:
                print("\nAttempted Input\n")

If we want this handler to address more than one type of exception, we can include a parenthesized tuple after the except with the exceptions.

    try:
        # some code
    except (ValueError, KeyboardInterrupt):
        # some code

Example:

    def party_planner(cookies, people):
        leftovers = None
        num_each = None

        try:
            num_each = cookies // people
            leftovers = cookies % people
        except ZeroDivisionError:
            print("Oops, you entered 0 people will be attending.")
            print("Please enter a good number of people for a party.")

        return(num_each, leftovers)

##### Accessing Error Messages

When you handle an exception, you can still access its error message like this:

    try:
        # some code
    except ZeroDivisionError as e:
    # some code
    print("ZeroDivisionError occurred: {}".format(e))

This would print something like this:

    ZeroDivisionError occurred: integer division or modulo by zero

## Files

Reading a File

    f = open('my_path/my_file.txt', 'r')
    file_data = f.read()
    f.close()

1. First open the file using the built-in function, open. This requires a string that shows the path to the file. The open function returns a file object, which is a Python object through which Python interacts with the file itself. Here, we assign this object to the variable f.
2. There are optional parameters you can specify in the open function. One is the mode in which we open the file. Here, we use r or read only. This is actually the default value for the mode argument.
3. Use the read method to access the contents from the file object. This read method takes the text contained in a file and puts it into a string. Here, we assign the string returned from this method into the variable file_data.
4. When finished with the file, use the close method to free up any system resources taken up by the file.


Writing to a File

    f = open('my_path/my_file.txt', 'w')
    f.write("Hello there!")
    f.close()

**With**

Python provides a special syntax that auto-closes a file for you once you're finished using it.

    with open('my_path/my_file.txt', 'r') as f:
        file_data = f.read()
        
This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file. Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.

    with open("camelot.txt") as song:
        print(song.read(2))
        print(song.read(8))

Each time we called read on the file with an integer argument, it read up to that number of characters, outputted them, and kept the 'window' at that position for the next call to read. This makes moving around in the open file a little tricky, as there aren't many landmarks to navigate by.

Conveniently, Python will loop over the lines of a file using the syntax for line in file. I can use this to create a list of lines in the file. Because each line still has its newline character attached, I remove this using .strip().

    camelot_lines = []
    with open("camelot.txt") as f:
        for line in f:
            camelot_lines.append(line.strip())

    print(camelot_lines)

Outputs:

    ["We're the knights of the round table", "We dance whenever we're able"]

## Import Python files

If the python files are in the same directory:

    import other_script

To use functions and variables of other scripts (modules)

    print(other_script.num)

To simplify we can give other name to the module

    import other_script as uf
    print(uf.num)

To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if __name__ == "__main__" block. Or alternatively, include them in a function called main() and call this in the if main block.

    # useful_functions.py

    def mean(num_list):
        return sum(num_list) / len(num_list)

    def add_five(num_list):
        return [n + 5 for n in num_list]

    def main():
        print("Testing mean function")
        n_list = [34, 44, 23, 46, 12, 24]
        correct_mean = 30.5
        assert(mean(n_list) == correct_mean)

        print("Testing add_five function")
        correct_list = [39, 49, 28, 51, 17, 29]
        assert(add_five(n_list) == correct_list)

        print("All tests passed!")

    if __name__ == '__main__':
        main()
________        
    # demo.py

    import useful_functions as uf

    scores = [88, 92, 79, 93, 85]

    mean = uf.mean(scores)
    curved = uf.add_five(scores)

    mean_c = uf.mean(curved)

    print("Scores:", scores)
    print("Original Mean:", mean, " New Mean:", mean_c)

    print(__name__)
    print(uf.__name__)

## Import Library's

[Python Standard Library](https://docs.python.org/3.6/library/index.html)

    import math

    print(math.exp(3))

#### Our favourite modules

The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

* csv: very convenient for reading and writing csv files
* collections: useful extensions of the usual data types including    OrderedDict, defaultdict and namedtuple
* random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
* string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
* re: pattern-matching in strings via regular expressions
* math: some standard mathematical functions
* os: interacting with operating systems
* os.path: submodule of os for manipulating path names
* sys: work directly with the Python interpreter
* json: good for reading and writing json files (good for web work)

To import just a method of a library

    from collections import defaultdict
    # or:
    from collections import defaultdict, namedtuple
    # giving name to modules:
    from csv import reader as csvreader


This ill import the method ***defaultdict*** from collections and nothing more

In order to manage the code better, modules in the Python Standard Library are split down into sub-modules that are contained within a package. A package is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.

    import package_name.submodule_name
_____
    import random
    random.radint(0,10)

    from random import randint
    randint(0,10)

### Third lybrary party

terminal (gitbash):
    
    pip install pytz

editor:

    import pytz

    ist_now = now.astimezone(ist)

Is common practice to indicate in a file named "requirements.txt" the third party librarys that we use, so that anyone can use our code

    # requirements.txt

    name_package == version

    beaitifulsoup4==4.5.1
    bs4==0.0.1

You can install all dependencys in the requerements.txt using pip:

terminal / git bash :

    pip install -r requitements.txt

#### Useful Third-Party Packages

* IPython - A better interactive Python interpreter
* requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
* Flask - a lightweight framework for making web applications and APIs.
* Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
* Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
* pytest - extends Python's builtin assertions and unittest module.
* PyYAML - For reading and writing YAML files.
* NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
* pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
* matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
* ggplot - Another 2D plotting library, based on R's ggplot2 library.
* Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
* pyglet - A cross-platform application framework intended for game development.
* Pygame - A set of Python modules designed for writing games.
* pytz - World Timezone Definitions for Python


### Hierarchy of Online Resources

While there are many online resources about programming, not all of the them are created equal. This list of resources is in approximate order of reliability.

1. The Python Tutorial - This section of the official documentation surveys Python's syntax and standard library. It uses examples, and is written using less technical language than the main documentation. Make sure you're reading the Python 3 version of the docs!
2. The Python Language and Library References - The Language Reference and Library Reference are more technical than the tutorial, but they are the definitive sources of truth. As you become increasingly acquainted with Python you should use these resources more and more.
3. Third-Party Library Documentation - Third-party libraries publish their documentation on their own websites, and often times at https://readthedocs.org/. You can judge the quality of a third-party library by the quality of its documentation. If the developers haven't found time to write good docs, they probably haven't found the time to polish their library either.
4. The websites and blogs of prominent experts - The previous resources are primary sources, meaning that they are documentation from the same people who wrote the code being documented. Primary sources are the most reliable. Secondary sources are also extremely valuable. The difficulty with secondary sources is determining the credibility of the source. The websites of authors like Doug Hellmann and developers like Eli Bendersky are excellent. The blog of an unknown author might be excellent, or it might be rubbish.
5. StackOverflow - This question and answer site has a good amount of traffic, so it's likely that someone has asked (and someone has answered) a related question before! However, answers are provided by volunteers and vary in quality. Always understand solutions before putting them into your program. One line answers without any explanation are dubious. This is a good place to find out more about your question or discover alternative search terms.
6. Bug Trackers - Sometimes you'll encounter a problem so rare, or so new, that no one has addressed it on StackOverflow. You might find a reference to your error in a bug report on GitHub for instance. These bug reports can be helpful, but you'll probably have to do some original engineering work to solve the problem.
7. Random Web Forums - Sometimes your search yields references to forums that haven't been active since 2004, or some similarly ancient time. If these are the only resources that address your problem, you should rethink how you're approaching your solution.

