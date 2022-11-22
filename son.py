from tkinter import*
import pygame

windows= Tk()
windows.geometry("760x510")
can=Canvas(windows,width=1100, height=700)
img=PhotoImage(file="C:\\Users\\Siham\\Desktop\\L2 MIASHS~S1\\Informatique\\TD\\Projet vacances\\image_de_fond.png")

can.create_image(0,0,anchor=NW,image=img)
#NW=Nord ouest (A NE PAS MODIFIER)
can.place(x=0,y=0)

def boutton():
    pygame.mixer.init()
    pygame.mixer.music.load("ace-combat-121102.mp3")
    pygame.mixer.music.play()
    bouton1 = Button (windows,text = "START", width=18, height=3,font=("Courrier",20), bg="white", fg="#80d0d0",command=StartButton)
    bouton1.place(x=245,y=225)

    print("Bienvenue "+champNom.get()+" tu peux cliquer sur START pour commencer la partie")
    
def StartButton():
    import prototype

ok=Button(windows,text="Valider",command=boutton)
ok.place(x=365,y=315)

lblNom=Label(windows,text="Saisissez votre nom")
champNom=Entry(windows)
champNom.place(x=325,y=275) #le x va nous permettre de le decaler de gauche à droite (x grand ira vers la droite)
lblNom.place(x=335,y=225) #plus le y est petit plus il sera proche du haut de page




windows.mainloop()