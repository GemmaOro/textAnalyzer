texto = input("Introduce una cita de tu agrado:  ").lower()

letra1 = input("Dime 1 letra de tu elección al azar: ").lower()
letra2 = input("Dime una 2a letra de tu elección al azar: ").lower()
letra3 = input("Dime una 3a letra de tu elección al azar: ").lower()

solucion1 = texto.count(letra1)
solucion2= texto.count(letra2)
solucion3= texto.count(letra3)

print(f"La letra '{letra1}' aparece {solucion1} veces en tu texto. ")
print(f"La letra '{letra2}' aparece {solucion2} veces en tu texto. ")
print(f"La letra '{letra3}' aparece {solucion3} veces en tu texto. ")

palabras = texto.split()
print(f"Tu texto tiene un total de {len(palabras)} palabras! ¿Qué te parece? ")
letra_inicial= texto[0]

print(f"La primera letra que aparece en el texto es la : '{letra_inicial}' ")

letra_final = texto[-1]
print(f"La última letra de tu texto es la: '{letra_final}' ")

texto_al_reves = texto[::-1]
texto_unido = " ".join(texto_al_reves)
print(f"Tu texto al reves se vería así: '{texto_unido}' ")

buscar_python = "Python" in texto
dic= {True: 'si', False: 'no'}
print(f"La palabra 'Python' {dic[buscar_python]} aparece en tu texto. ")



















