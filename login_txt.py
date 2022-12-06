

dict = {}
dane3 = []

def rejestracja():
    with open('loginy.txt') as f:
        dane = f.read()

    dane = dane.split('\n')

    for i in dane:
        dane2 = i.split(':')
        dane3.append(dane2)

    for i in dane3:
        dict[i[0]] = i[1]

    User = input('Podaj nazwe tworzonego urzytkownika: ')
    Password = input('Podaj haslo: ')
    Password2 = input('Powtorz haslo: ')

    if (len(User) or len(Password)) < 1:
        print("\nNie mozna zostawic pustych pol!\n")
        return rejestracja()

    elif User in dict:
        print('\nTaki uzytkownik juz istnieje, wybierz inna nazwe!\n')
        return rejestracja()

    elif Password != Password2:
        print('\nPodane hasla sa rozne, sprobuj jeszcze raz\n')
        return rejestracja()

    with open('loginy.txt', 'a') as f:
        f.write(f'\n{User}:{Password}')
        print('\nUrzytkownik dodany pomyslnie\n')

def logowanie():
    with open('loginy.txt') as f:
        dane = f.read()

    dane = dane.split('\n')

    for i in dane:
        dane2 = i.split(':')
        dane3.append(dane2)

    for i in dane3:
        dict[i[0]] = i[1]

    User = input('Podaj nazwe urzytkownika: ')
    Password = input('Podaj haslo: ')
    
    if User in dict and Password == dict[User]:
        print('\nLogowanie pomyslne\n')
    else:
        print('\nNieprawidlowy login lub haslo\n')

def home(option=None):
    option = input('Rejestracja | Logowanie: ')
    if option == 'Rejestracja' or option == 'rejestracja':
        return rejestracja()

    elif option == 'Logowanie' or option == 'logowanie':
        return logowanie()

    else:
        print('\nWpisz: Rejestracja albo Logowanie\n')
        return home()

home()