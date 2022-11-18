from tkinter import*

windows= Tk()
windows.geometry("760x510")
can=Canvas(windows,width=1100, height=700)
img=PhotoImage(file="C:\\Users\\nawel\\OneDrive\\Documents\\MIASHS\\Semestre 3\\informatique\\PROJET\\image_de_fond.png")

can.create_image(0,0,anchor=NW,image=img)
#NW=Nord ouest
can.place(x=0,y=0)

def boutton():
    bouton1 = Button (windows,text = "START", font=("Courrier",20), bg="white", fg="#80d0d0",command=StartButton)
    bouton1.pack(expand=True)
    print("Bienvenue "+champNom.get()+" tu peux cliquer sur START pour commencer la partie")

def StartButton():
    #print("BBBBB")
    import myfile


ok=Button(windows,text="valider",command=boutton)

lblNom=Label(windows,text="siasissez votre nom")
champNom=Entry(windows)

lblNom.pack(expand=YES)
champNom.pack(expand=YES)

ok.pack(expand=YES)


windows.mainloop()

print("AAAA")
