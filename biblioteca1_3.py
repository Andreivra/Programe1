biblioteca = []
continua = True


def adaugare():
    """ Aceasta functie adauga o carte"""
    cod_isbn = input("Introduceti codul ISBN: ")
    tip_carte = input("Introduceti tipul cartii: ")
    autor = input("Introduceti autorul: ")
    titlu = input("introduceti titlul: ")
    detalii_carte = {
        "cod_ISBN": cod_isbn,
        "tip carte": tip_carte,
        "autor": autor,
        "titlu": titlu}
    biblioteca.append(detalii_carte)


def sterge():
    """ Aceasta functie sterge o carte"""
    isbn_carte = input("Ce carte doriti sa stergem? (introduceti codul ISBN al acesteia)")
    for carte in biblioteca:
        if carte["cod_ISBN"] == isbn_carte:
            biblioteca.remove(carte)


def detalii():
    """ Aceasta functie aafiseaza detaliile unei carti"""
    isbn_carte = input("Va rugam introduceti cartea pentru care doriti detalii (specificati codul ISBN): ")
    for carte in biblioteca:
        if carte["cod_ISBN"] == isbn_carte:
            print(f"Carte cu codul ISBN {carte['cod_ISBN']} are numele {carte['titlu']} si a fost "
                  f"scrisa de {carte['autor']} avnd titlul {carte['titlu']}")


def lista():
    """ Aceasta functie afiseaza lista cartilor introduse"""
    lista_isbn = []
    for carte in biblioteca:
        isbn = carte["cod_ISBN"]
        lista_isbn.append(isbn)
        print(isbn)


while continua:
    raspuns = input("Putem sa -adaugam- o carte sausa -stergem- sau vizualizam -detalii- "
                    "sau -lista- pentru afisarea cartilor sau -q- pentru a iesii: ")
    if raspuns == "adaugam":
        adaugare()
    elif raspuns == "stergem":
        sterge()
    elif raspuns == "detalii":
        detalii()
    elif raspuns == "lista":
        lista()
    elif raspuns == "q":
        continua = False
    else:
        print("Nu ati introdus o varianta valida de raspuns!")
