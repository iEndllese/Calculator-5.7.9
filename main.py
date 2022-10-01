import config
from color import G, C, W, B, Y
from os import system as os

utils = config
TG = G + utils.TegsScript
VB = B + utils.Ver_By
print(TG + VB)

while True:
	calculate = eval(input(C + "\nВызначение: " + W))
	os("cls||clear") ; 
	print(TG + VB) ; 
	print(Y + utils.line)
	print(C + f"Итого: {W}{calculate}\n" + Y + utils.line)