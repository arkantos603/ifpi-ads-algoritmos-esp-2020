#Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, do_twice é uma função que
#  toma um objeto de função como argumento e o chama duas vezes:

def do_twice(func, arg):
 
    func(arg)
    func(arg)


def print_twice(arg):

    print(arg)
    print(arg)


def do_four(func, arg):

    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print, 'spam')
print('')

do_four(print, 'spam')