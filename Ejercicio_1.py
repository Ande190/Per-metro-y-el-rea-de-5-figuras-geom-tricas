import math
#Algoritmo No 1
#Elabore un algoritmo que halle el perímetro y el área de 5 figuras geométricas (diferentes a las hechas en clase).
#Entradas
#basemayor_trapecio, basemenor_trapecio, lado1_trapecio, lado2_trapecio, altura_trapecio
# lado_rombo, diagonalmayor_rombo, diagonalmenor_rombo
#diagonalmayor, diagonalmenor, lado_hexagono, apotema_hexagono
#radiomenor_elipse, radiomayor_elipse
#lado_heptagono, apotema_heptagono
#Lectura de Datos por teclado
basemayor_trapecio=float(input("Digite el valor de la base mayor para hallar área y perímetro del Trapecio:"));
basemenor_trapecio=float(input("Digite el valor de la base menor para hallar área y perímetro del Trapecio:"));
lado1_trapecio=float(input("Digite el valor del lado uno para hallar área y perímetro del Trapecio:"));
lado2_trapecio=float(input("Digite el valor del lado dos para hallar área y perímetro del Trapecio:"));
altura_trapecio=float(input("Digite el valor de la altura para hallar área del Trapecio:"));
lado_rombo = float(input("Digite el valor del lado del rombo para hallar perímetro del rombo:"));
diagonalmayor = float(input("Digite el valor de la diagonal mayor para hallar área del rombo:"));
diagonalmenor = float(input("Digite el valor de la diagonal menor para hallar área del rombo:"));
lado_hexagono = float(input("Digite el valor del lado del Hexagono para hallar área y perímetro del Hexagono:"));
apotema_hexagono =float(input("Digite el valor del apotema del Hexagono para hallar el área del Hexagono:"));
radiomenor_elipse =float(input("Digite el valor del radio menor para hallar área y perímetro de una Elipse:"));
radiomayor_elipse=float(input("Digite el valor del radio mayor para hallar área y perímetro de una Elipse:"));
lado_heptagono=float(input("Digite el valor del lado del heptágono para hallar perímetro del Heptágono:"));
apotema_heptagono=float(input("Digite el valor de la apotema para hallar el área del Heptágono:"));
#Procesos
perimetro_trapecio = basemayor_trapecio + basemenor_trapecio + lado1_trapecio + lado2_trapecio;
area_trapecio = (basemayor_trapecio + basemenor_trapecio) * altura_trapecio / 2;
perimetro_rombo = 4 + lado_rombo;
area_rombo = diagonalmayor * diagonalmenor / 2;
perimetro_hexagono = 6 * lado_hexagono;
area_hexagono = perimetro_hexagono * lado_hexagono / 2;
perimetro_elipse = math.pi * (radiomenor_elipse + radiomayor_elipse);
area_elipse = math.pi * radiomenor_elipse + radiomayor_elipse;
perimetro_heptagono = 7 * lado_heptagono;
area_heptagono = perimetro_heptagono * apotema_heptagono / 2;
#Salidas
print("Perimetro del Trapecio=",perimetro_trapecio);
print("Area del Trapecio=",area_trapecio);
print("Perimetro del Rombo=",perimetro_rombo);
print("Area del Rombo=",area_rombo);
print("Perimetro del Hexágono=",perimetro_hexagono);
print("Area del Hexágono=",area_hexagono);
print("Perimetro de la Elipse=",perimetro_elipse);
print("Area de la Elipse=",area_elipse);
print("Perimetro del Heptagono=",perimetro_heptagono);
print("Area del Heptagono=",area_heptagono);





