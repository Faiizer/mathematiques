from tkinter import *
"""
Création de la fenêtre 'root'
"""
root = Tk()
root.update()
root.title('Dérivées')

"""
Ici nous avons la création des barres du Menu
"""
menuBar = Menu(root)
root['menu'] = menuBar

sousMenu = Menu(menuBar)
menuBar.add_cascade(label='Fichier', menu=sousMenu)
sousMenu.add_command(label='Quitter', command=root.quit())
sousMenu2 = Menu(menuBar)
menuBar.add_cascade(label='A venir', menu=sousMenu2)
sousMenu2.add_command(label='A venir')
sousMenu2.add_command(label='A venir')
sousMenu2.add_command(label='A venir')
sousMenu2.add_command(label='A venir')
sousMenu2.add_command(label='A venir')

"""
Ce calcul permet de créer des points et des lignes correspondants aux points et à la courbe de la fonction
"""
def calculs(event):
    calcul = entree.get()
    intervalle = [-100, 100]
    for x in range(intervalle[0], intervalle[1] + 1):
        y = eval(calcul)
        can.create_oval(xb + x * 10, yb + y * 10, xb + x * 10, yb + y * 10, fill='white', outline='white')
        calculPlusUn = calcul.replace('x', '(x+1)')
        can.create_line(xb + x * 10, yb + y * 10, xb + (x+1) * 10, yb + eval(calculPlusUn) * 10, fill='white')
        root.update()



"""
Ici nous entrons la fonction, qui sera calculée et mise sur le graphique
"""
value = StringVar(root)
value.set("Utilisez ' x ' si vous possédez un inconnu :)")

entree = Entry(root, textvariable=value, width=50)
entree.pack()

# On lie la fonction à l'Entry
# La fonction sera exécutée à chaque fois que l'utilisateur appuie sur "Entrée"
entree.bind("<Return>", calculs)




"""
Ici, nous définissons l'endroit auquel se trouve le pointeur de la souris et l'écrivons en bas
"""
def motion(event):
    chaine.configure(text = "X =" + str((int(event.x) - xb) / 10) + ", Y =" + str(-(int(event.y) - yb) / 10))

can = Canvas(root, cursor='crosshair', bg='black', height=800, width=800)
can.bind("<Motion>", motion)
can.pack()
chaine = Label(root)
chaine.pack()


"""
Ici, nous avons la création des axes (ordonnées & abscisses)
"""
can.create_line(0, 400, 800, 400, fill='white')
can.create_line(400, 0, 400, 800, fill='white')

"""
Ici, nous définissons le point (0; 0) qui correspond donc au point (400; 400) car nous avons une fenêtre 800*800
"""
xb = 400
yb = 400

root.mainloop()
