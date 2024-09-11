import tkinter as tk

x = 400
y = 600
screensize = f'{x}x{y}'

root = tk.Tk()
root.title('Test')
root.geometry(screensize)

#count = 0

#def on_button1_click():
#    global count
#    count += 1
#    label1.config(text=f'Mi hai clickato {count} volte')

#button1 = tk.Button(root, text='Click Me', command=on_button1_click)
#button1.pack()

#label1 = tk.Label(root, text='Bla bla bla ciao')
#label1.pack()

background = tk.Frame(root, bg='green')
background.pack(side="top", expand=True, fill="both")

dealer_label = tk.Label(background, text='Bla bla bla ciao')
dealer_label.pack(side="top",fill=None, expand=False, pady=50)

hand_label = tk.Label(background, text='Bla bla bla aniafojfoa')
hand_label.pack(side="top",fill=None, expand=False, pady=100)

buttons = tk.Frame(background, bg='grey', width=y, height=200)
buttons.pack(side="bottom", expand=False, fill="both")

buttons2 = tk.Frame(buttons, bg='red', width=150, height=100)
buttons2.pack(side="top", expand=True, fill=None)

button_pesca = tk.Button(buttons2, text='Pesca', width=15)
button_pesca.pack(side="left",fill=None, expand=False, padx=5, pady=5)

button_stai = tk.Button(buttons2, text='Stai', width=15)
button_stai.pack(side="right",fill=None, expand=False, padx=5, pady=5)



#upper_frame = tk.Frame(root, height=x/3, width=y/3, bg='blue')
#upper_frame.grid(row=0, column=1, padx=x/3, pady=y/3)

#lower_frame = tk.Frame(root, height=x/3, width=y/3, bg='purple')
#lower_frame.grid(row=2, column=1, padx=x/3, pady=y/3)


root.mainloop()