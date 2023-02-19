def capitale():
    score = 0
    raspuns = input('Care este capitala Romaniei?\n').lower()
    if raspuns == 'bucuresti':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala Germaniei?\n').lower()
    if raspuns == 'berlin':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala tarii Lichtenstein?\n').lower()
    if raspuns == 'vaduz':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala Suediei?\n').lower()
    if raspuns == 'stockholm':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala Spaniei?\n').lower()
    if raspuns == 'madrid':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala Frantei?\n').lower()
    if raspuns == 'paris':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala tarii Madagascar?\n').lower()
    if raspuns == 'antananarivo':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala tarii Kosovo?\n').lower()
    if raspuns == 'pristina':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala tarii Azerbaijian?\n').lower()
    if raspuns == 'baku':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este capitala Kazahstanului?\n').lower()
    if raspuns == 'astana':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    print('Ai raspuns la ' + str(score) + ' intrebari corect!')
    print('Ai avut o rata de raspuns de ' + str((score / 10) * 100) + '%')
    print('Iti multumesc ca ai avut timp sa joci acest joc de cultura generala!!!!')


def castele():
    score = 0
    raspuns = input('In care oras se afla castelul lui Matei Corvin?\n').lower()
    if raspuns == 'hunedoara':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('In ce judet se afla cetatea Dacica "Valea Zanelor"?\n').lower()
    if raspuns == 'covasna':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Cum se numeste actualmente localitatea unde a fost cetatea Porolissum?\n').lower()
    if raspuns == 'cluj napoca':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('In ce localitate se afla castelul lui Dracula?\n').lower()
    if raspuns == 'bran':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    print('Ai raspuns la ' + str(score) + ' intrebari corect!')
    print('Ai avut o rata de raspuns de ' + str((score / 4) * 100) + '%')
    print('Iti multumesc ca ai avut timp sa joci acest joc de cultura generala!!!!')


def istorie():
    score = 0
    raspuns = input('Cand a avut loc unirea Romaniei ?\n').lower()
    if raspuns == '1918':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('In ce an a cazut cortina de fier?\n').lower()
    if raspuns == '1990':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Cat a durat razboiul de 100 de ani?\n').lower()
    if raspuns == '106':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    print('Ai raspuns la ' + str(score) + ' intrebari corect!')
    print('Ai avut o rata de raspuns de ' + str((score / 3) * 100) + '%')
    print('Iti multumesc ca ai avut timp sa joci acest joc de cultura generala!!!!')


def geografie():
    score = 0
    raspuns = input('Unde se varsa Dunarea ?\n').lower()
    if raspuns == 'marea neagra':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Care este continentul care nu incepe cu litera "A"?\n').lower()
    if raspuns == 'europa':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    raspuns = input('Pe ce continent se afla lacul Tonle Sap?\n').lower()
    if raspuns == 'vaduz':
        print('Corect!\n')
        score += 1
    else:
        print('Incorect!\n')

    print('Ai raspuns la ' + str(score) + ' intrebari corect!')
    print('Ai avut o rata de raspuns de ' + str((score / 3) * 100) + '%')
    print('Iti multumesc ca ai avut timp sa joci acest joc de cultura generala!!!!')


print('Bine ai venit la jocul intrebarilor!')

joc = input('Vrei sa jucam acest joc?\n').lower()
if joc != 'da':
    print("La revedere!")
    quit()
else:
    print('Hai sa incepem!')
print('Capitale, Castele, Istorie, Geografie')
cat = input('Te rog sa alegi o categorie din cele enumerate mai sus: \n').lower()
if cat == 'capitale':
    capitale()
else:
    if cat == 'castele':
        castele()
    else:
        if cat == 'istorie':
            istorie()
        else:
            if cat == "geografie":
                geografie()
            else:
                print('aceasta categorie nu se regaseste in plaja admisa!')
