import random

cards = ['asso', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'donna', 're']

mano_banco = []
punti_banco = 0
mano_giocatore = []
punti_giocatore = 0

def draw():
    return random.choice(cards)

def game_init():
    for i in range(2):
        mano_banco.append(draw())
        mano_giocatore.append(draw())
    print(f'\nMano del Banco: [{mano_banco[0]}, x]\n')
    print(f'La tua mano: {mano_giocatore}')
    print(f'I tuoi punti: {calcola_punti(mano_giocatore, punti_giocatore)}\n')

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
    tf = True
    if punti_giocatore == 21:
        print('21! Hai vinto!')
    while punti_giocatore < 21 and tf == True:
        yn = input('Peschi o stai? p/s')
        if yn == 'p':
            mano_giocatore.append(draw())
            print(f'La tua mano: {mano_giocatore}')
            print(f'I tuoi punti: {calcola_punti(mano_giocatore, punti_giocatore)}\n')
        elif yn == 's':
            print('Turno del banco!')
            tf = False


game_init()
turno_giocatore()


