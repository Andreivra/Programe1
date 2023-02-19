biblioteca = []


def adaugare():
    """ Aceasta functie adauga o carte"""
    cod_isbn = input('Va rugam introduceti codul isbn: ')
    tipul_cartii = input('Va rugam introduceti genul cartii: ')
    autor = input('Va rugam introduceti autorul cartii: ')
    titlu = input('Va rugam introduceti titlul cartii: ')
    det_carte = {
        'cod_isbn': cod_isbn,
        'Tipul cartii': tipul_cartii,
        'Autor': autor,
        'Titlu': titlu}
    biblioteca.append(det_carte)


def sterge():
    """ Aceasta functie sterge o carte"""
    isbn_carte = input('Ce carte dotiti sa stergem? (specificati codul isbn al cartii)')
    for carte in biblioteca:
        if carte['cod_isbn'] == isbn_carte:
            biblioteca.remove(carte)
    # for index, carte in biblioteca:
    #     if carte['cod_isbn'] == isbn_carte:
    #         biblioteca.pop(index)


def detalii():
    """ Aceasta functie aafiseaza detaliile unei carti"""
    isbn_carte = input('Va rugam introduceti cartea pentru care doriti detalii? (specificati cod isbn al cartii)')
    for carte in biblioteca:
        if carte['cod_isbn'] == isbn_carte:
            print(f'Cartea cu codul isbn {carte["cod_isbn"]} are numele {carte["Titlu"]} scrisa de {carte["Autor"]}.')


def lista():
    """ Aceasta functie afiseaza lista cartilor introduse"""
    lista_isbn = []
    for carte in biblioteca:
        isbn = carte["cod_ISBN"]
        lista_isbn.append(isbn)
        print(isbn)

raspuns = input('Putem sa -adaugam- o carte sausa -stergem- sau '
                'vizualizam -detalii- sau -lista- pentru afisarea cartilor sau -q- pentru a iesii: ').lower
if raspuns == "adaugam":
    adaugare()
elif raspuns == "stergem":
    sterge()
elif raspuns == "detalii":
    detalii()
elif raspuns == "lista":
    lista()
elif raspuns == "q":
    quit()
else :
    print("Nu ati introdus o varianta valida de raspuns!")
