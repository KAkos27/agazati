def elso():
    etel_nev:str = str(input("Étel neve: "))
    nev:str = str(input("Étel rendelőjének neve: "))

    ertekeles:int = int(input("Értékelés (1-5): "))
    while ertekeles < 1 or ertekeles > 5:
        if ertekeles < 1:
            print("Az értékelés nem lehet negatív!")
            ertekeles:int = int(input("Értékelés (1-5): "))
        elif ertekeles > 5:
            print("5 pont feletti értékelés nem elfogadható!")
            ertekeles:int = int(input("Értékelés (1-5): "))
    
    print("Köszönjük az értékelést!")