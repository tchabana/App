import tkinter as tk 
from tkinter import *
from tkinter import PhotoImage

#Dictionaire de couleure
couleur = {
    "nero":"#252726",
    "purpule":"#800080",
    "white":"#FFFFFF"
}

app = tk.Tk()
app.title("G-stock")
app.config(bg="gray30")
app.geometry("400x600")
#app.iconbitmap("logo_.ico")

btnEtat = False

def switch():
    global btnEtat
    if btnEtat == True:
        for x in range(300):
            navLateral.place(x=-x,y=0)
            topFrame.update()
        bannerText.config(fg=couleur["purpule"])
        acceilText.config(bg=couleur["purpule"])
        topFrame.config(bg=couleur["purpule"])
        app.config(bg="gray30")
        btnEtat = False
    else:
        for x in range(-300,0):
            navLateral.place(x=x,y=0)
            topFrame.update()
            btnEtat = True
# chargement images de la bare de menue
navIcon = PhotoImage(file='menu.png')
closeIcon = PhotoImage(file='close.png')
imgFont = PhotoImage(file='back_image3.png')

# top bare

topFrame = tk .Frame(app,bg=couleur["purpule"])
topFrame.pack(side='top',fill=tk.X)

acceilText = tk.Label(topFrame,text='GRAFIMAK',font="ExtraCondensed 15",bg=couleur["purpule"],fg="white",height=2,padx=20)
acceilText.pack(side='right')

# Image de font 
can = Canvas(app,width=400,height=600)
can.create_image( 0,0, anchor=NW ,image=imgFont)
can.pack()
bannerText = tk.Label(app,text="GRAFIMAK",font="ExtraCondensed 20",fg='purple')
bannerText.place(x=120,y=400)



# bouton de nav

navbarBtn = tk.Button(topFrame,image=navIcon,bg=couleur["purpule"],padx=20,bd=0, activebackground=couleur["purpule"],command=switch)
navbarBtn.place(x=10,y=5)
# nav bar laterale
navLateral = Frame(app,bg='gray30',width=300,height=600)
navLateral.place(x=-300,y=0)
tk.Label(navLateral,font="ExtraCondensed 15",bg=couleur["purpule"],fg="black",width=300,height=2,padx=20).place(x=0,y=0)

# les option de la navbar

option = ['ACCUEIL','PAGES','PROFILE','PARAMETRE','AIDE']
y = 80
for i in range(5):
    tk.Button(navLateral,text=option[i],font="ExtraCondensed 15",bg="gray30",fg=couleur["white"],activebackground="gray30",bd=0).place(x=25,y=y)
    y += 40
# bouton de fermeture

fermrBtn = tk.Button(navLateral,image=closeIcon,bg=couleur["purpule"],activebackground=couleur["purpule"],command=switch,bd=0).place(x=250,y=10)

app.mainloop()
