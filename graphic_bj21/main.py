import random
import tkinter as tk

x = 400
y = 600
screensize = f'{x}x{y}'

root = tk.Tk()
root.title('Test')
root.geometry(screensize)
root.resizable(False, False)
timer = tk.IntVar()

cards = ['asso', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'donna', 're']

mano_banco = []
punti_banco = 0
mano_giocatore = []
punti_giocatore = 0

background = tk.Frame(root, bg='green')
background.pack(side="top", expand=True, fill="both")

dealer_label = tk.Label(background, text='Bla bla bla ciao')
dealer_label.pack(side="top",fill=None, expand=False, pady=50)

hand_label = tk.Label(background)
hand_label.pack(side="top",fill=None, expand=False, pady=100)

buttons = tk.Frame(background, bg='grey', width=y, height=200)
buttons.pack(side="bottom", expand=False, fill="both")

buttons2 = tk.Frame(buttons, bg='red', width=150, height=100)
buttons2.pack(side="top", expand=True, fill=None)



def draw():
    return random.choice(cards)

def game_init():
    global punti_banco
    punti_banco = 0
    global punti_giocatore
    punti_giocatore = 0
    global mano_banco
    mano_banco.clear()
    global mano_giocatore
    mano_giocatore.clear()
    for i in range(2):
        mano_banco.append(draw())
        mano_giocatore.append(draw())
    print(f'\nMano del Banco: [{mano_banco[0]}, x]\n')
    hand_label.config(text=f'La tua mano: {mano_giocatore}')
    punti_giocatore = calcola_punti(mano_giocatore)
    hand_label.config(text=f'I tuoi punti: {punti_giocatore}')

def calcola_punti(mano):
    punti = 0
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
            hand_label.config(text='Peschi o stai?')
        else: tf = False

def blackjack(mano):
    punti = 0
    for card in mano:
        if card in ('re', 'donna', 'jack'):
            punti += 10
        elif card == 'asso':
            punti += 11
    if punti == 21:
        print('Black Jack!\n')
        return True
    return False

def turno_banco():
    global punti_banco
    global punti_giocatore
    print(f'Mano del Banco: {mano_banco}')
    punti_banco = calcola_punti(mano_banco)
    print(f'I punti del Banco: {punti_banco}\n')
    print
    while punti_banco < 17 or punti_banco < punti_giocatore:
        print('Il Banco pesca!')
        mano_banco.append(draw())
        punti_banco = calcola_punti(mano_banco)
        print(f'Mano del Banco: {mano_banco}')
        print(f'I punti del Banco: {punti_banco}\n')

def on_click_pesca():
    mano_giocatore.append(draw())
    hand_label.config(text=f'La tua mano: {mano_giocatore}')
    punti_giocatore = calcola_punti(mano_giocatore)
    hand_label.config(text=f'I tuoi punti: {punti_giocatore}\n')

def on_click_stai():
    hand_label.config(text='Turno del banco!')
    turno_banco()
    if punti_banco > 21:
        print('Il banco ha sballato!')
    elif blackjack(mano_banco):
        punti_banco = 22
    if punti_banco > punti_giocatore:
        print('Ha vinto il banco!')
    if punti_banco < punti_giocatore:
        print('Hai vinto!')
    if punti_banco == punti_giocatore:
        print('Pareggio!')



button_pesca = tk.Button(buttons2, text='Pesca', command=on_click_pesca, width=15)
button_pesca.pack(side="left",fill=None, expand=False, padx=5, pady=5)

button_stai = tk.Button(buttons2, text='Stai', command=on_click_stai, width=15)
button_stai.pack(side="right",fill=None, expand=False, padx=5, pady=5)




def game_loop():
    while True:
        game_init()
        turno_giocatore()
        if punti_giocatore > 21:
            print('Hai sballato!')
            break
        elif blackjack(mano_giocatore):
            punti_giocatore = 22
        


root.mainloop()