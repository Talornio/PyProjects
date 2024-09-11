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
    set_screen()
    for i in range(2):
        mano_banco.append(draw())
        mano_giocatore.append(draw())
    punti_giocatore = calcola_punti(mano_giocatore)
    dealer_label.config(text=f'\nMano del Banco: [{mano_banco[0]}, x]')
    hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}')

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
    global punti_giocatore
    global punti_banco
    global mano_giocatore
    global punti_banco
    punti_banco = calcola_punti(mano_banco)
    while punti_banco < 17:
        mano_banco.append(draw())
        punti_banco = calcola_punti(mano_banco)
    dealer_label.config(text=f'Mano del Banco: {mano_banco}\nI punti del Banco: {punti_banco}')
    end()

def on_click_pesca():
    global punti_giocatore
    global punti_banco
    global mano_giocatore
    global mano_banco
    if punti_giocatore == 21:
        hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}')
        if blackjack(mano_banco):
            punti_giocatore = 22
            hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}\nBlackJack!')
        turno_banco()
    if punti_giocatore < 21:
        mano_giocatore.append(draw())
        punti_giocatore = calcola_punti(mano_giocatore)
        hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}\n')
    if punti_giocatore > 21:
        hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}\nHai sballato!')

def on_click_stai():
    hand_label.config(text='Turno del banco!')
    turno_banco()

def screen_clean():
    for widget in background.winfo_children():
        widget.destroy()

def set_screen():
    screen_clean()
    global dealer_label
    global hand_label
    global buttons
    global buttons2
    global button_pesca
    global button_stai

    dealer_label = tk.Label(background, text=' ')
    hand_label = tk.Label(background, text=' ')
    buttons = tk.Frame(background, bg='grey', width=y, height=200)
    buttons2 = tk.Frame(buttons, bg='red', width=150, height=100)
    button_pesca = tk.Button(buttons2, text='Pesca', command=on_click_pesca, width=15)
    button_stai = tk.Button(buttons2, text='Stai', command=on_click_stai, width=15) 
    dealer_label.pack(side="top",fill=None, expand=False, pady=50)
    hand_label.pack(side="top",fill=None, expand=False, pady=100)
    buttons.pack(side="bottom", expand=False, fill="both")
    buttons2.pack(side="top", expand=True, fill=None)
    button_pesca.pack(side="left",fill=None, expand=False, padx=5, pady=5)    
    button_stai.pack(side="right",fill=None, expand=False, padx=5, pady=5)

def end():
    global punti_giocatore
    global punti_banco
    global mano_giocatore
    global punti_banco
    #global ending_label
    #screen_clean()
    #ending_label = tk.Label(background, text=' ')
    #ending_label.pack(side='top', fill=None, expand=True)
    while True:
        if punti_banco > 21:
            dealer_label.config(text=f'Mano del Banco: {mano_banco}\nI punti del Banco: {punti_banco}\nIl banco ha sballato!')
            break
        elif blackjack(mano_banco):
            punti_banco = 22
        if punti_banco > punti_giocatore:
            dealer_label.config(text=f'Mano del Banco: {mano_banco}\nI punti del Banco: {punti_banco}\nHa vinto il banco!')
            if blackjack(mano_banco):
                dealer_label.config(text=f'Mano del Banco: {mano_banco}\nBlackJack!')
            break
        if punti_banco < punti_giocatore:
            hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}\nHai vinto!')
            if blackjack(mano_giocatore):
                hand_label.config(text=f'La tua mano: {mano_giocatore}\nBlackJack!')
            break
        if punti_banco == punti_giocatore:
            hand_label.config(text=f'La tua mano: {mano_giocatore}\nI tuoi punti: {punti_giocatore}\nPareggio!')
            break

ng_btn = tk.Button(background, text='Nuova partita!', command=game_init,width=20, height=10)
ng_btn.pack(side='top', fill=None, expand=True)

root.mainloop()