import random

cards = ['asso', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'donna', 're']

mano_banco = []
punti_banco = 0
mano_giocatore = []
punti_giocatore = 0
vittoria_giocatore = False
vittoria_banco = False

global_flag = True

def draw():
    return random.choice(cards)

def game_init():
    global punti_giocatore
    global punti_banco
    for i in range(2):
        mano_banco.append(draw())
        mano_giocatore.append(draw())
    print(f'\nMano del Banco: [{mano_banco[0]}, x]\n')
    print(f'La tua mano: {mano_giocatore}')
    punti_giocatore = calcola_punti(mano_giocatore, punti_giocatore)
    print(f'I tuoi punti: {punti_giocatore}\n')

def calcola_punti(mano, punti):
    for card in mano:
        if card in ('re', 'donna', 'jack'):
            punti += 10
        elif card == 'asso':
            if punti + 11 > 21:
                punti += 1
            else: punti += 11
        else: punti += card
    return punti

def turno_giocatore():
    global punti_giocatore
    tf = True
    while tf:
        if punti_giocatore == 21:
            print('21!')
            tf = False
        if punti_giocatore < 21:
            yn = input('Peschi o stai? p/s\n')
            if yn == 'p':
                mano_giocatore.append(draw())
                print(f'La tua mano: {mano_giocatore}')
                punti_giocatore = calcola_punti(mano_giocatore, punti_giocatore)
                print(f'I tuoi punti: {punti_giocatore}\n')
            elif yn == 's':
                print('Turno del banco!')
                tf = False

def blackjack(mano):
    punti = 0
    for card in mano:
        if card in ('re', 'donna', 'jack'):
            punti += 10
        elif card == 'asso':
            punti += 11
    if punti == 21:
        print('Black Jack!')
        return True
    return False

def turno_banco():
    global punti_banco
    print(f'Mano del Banco: {mano_banco}')
    punti_banco = calcola_punti(mano_banco, punti_banco)
    print(f'I punti del Banco: {punti_banco}\n')
    print
    while punti_banco < 17:
        print('Il Banco pesca!')
        mano_banco.append(draw())
        punti_banco = calcola_punti(mano_banco, punti_banco)
        print(f'Mano del Banco: {mano_banco}')
        print(f'I punti del Banco: {punti_banco}\n')

while True:
    game_init()
    turno_giocatore()
    if punti_giocatore > 21:
        print('Hai sballato!')
        break
    elif blackjack(mano_giocatore):
        punti_giocatore = 22
    turno_banco()
    if punti_banco > 21:
        print('Il banco ha sballato!')
        break
    elif blackjack(mano_banco):
        punti_banco = 22
    if punti_banco > punti_giocatore:
        print('Ha vinto il banco!')
        break
    if punti_banco < punti_giocatore:
        print('Hai vinto!')
        break
    if punti_banco == punti_giocatore:
        print('Pareggio!')
        break


