#Práctica 1: Gráficas de tortuga
# Fecha: 24-Ago-2016
# Autor:   A01379896 Erick Bautista Pérez
#           A01378568 Leonardo Valencia Benitez
#-------------------------------------------------------------------------------



from turtle import fd, lt, done, rt


def estrella(lado):
    for i in range(5):    
        lt(72)
        fd(lado)
        rt(144)
        fd(lado)
    
    
estrella(100)
done()