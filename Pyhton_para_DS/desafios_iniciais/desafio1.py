distancia, diametro1, diametro2 = list(map(int, input().split(" ")))

def icm():
    return distancia / (diametro1 + diametro2 )

print(f"{icm():.2f}")

print(input())

