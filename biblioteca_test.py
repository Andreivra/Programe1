biblioteca = []
intrare = True

while intrare:
    directie = input("Ce doriti sa facem? Putem sa -adaugam- o carte sau "
                     "sa -stergem- sau vizualizam -detalii- sau -q- pentru a iesii: ").lower
    if directie == 'q':
        intrare = False
    elif directie == 'adaugam':
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
    elif directie == 'stergem':
        isbn_carte = input('Ce carte dotiti sa stergem? (specificati codul isbn al cartii)')
        for carte in biblioteca:
            if carte['cod_isbn'] == isbn_carte:
                biblioteca.remove(carte)
        # for index, carte in biblioteca:
        #     if carte['cod_isbn'] == isbn_carte:
        #         biblioteca.pop(index)

    elif directie == 'detalii':
        isbn_carte = input('Va rugam introduceti cartea pentru care doriti detalii? (specificati cod isbn al cartii)')
        for carte in biblioteca:
            if carte['cod_isbn'] == isbn_carte:
                print(f'Cartea cu codul isbn {carte["cod_isbn"]} are '
                      f'numele {carte["Titlu"]} scrisa de {carte["Autor"]}.')
