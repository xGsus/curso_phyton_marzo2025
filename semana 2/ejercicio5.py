nota = int(input("Ingrese la calificacion entre 0 y 100:"))

if nota>=90 and nota<=100:
    print("La calificacion es A")
elif nota>=80 and nota<=89:
    print("La calificacion es B")
elif nota>=70 and nota<=79:
    print("La calificacion es C")
elif nota>=60 and nota<=69:
    print("La calificacion es D")
else:
    print("La calificacion es F")