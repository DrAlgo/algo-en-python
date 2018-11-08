

def recherche_dichotomique(tab,x):
    """tab tableau croissant ; si x est dans tab renvoie 
    un indice i correspondant, sinon renvoie None"""

    fini = False       #indique si la recherche est finie
    position = None    #indice de x si trouve, None sinon
    debut = 0          #debut intervalle de recherche
    fin = len(tab)-1   #fin intervalle de recherche

    #on peut rejecter directement si tab vide
    #ou si est en dehors des bornes du tableau
    if not tab or x < tab[0] or x > tab[fin]:
        return None

    while not fini:
        milieu = (debut + fin)/2
        if x < tab[milieu]:
            fin = milieu - 1
        elif x > tab[milieu]:
            debut = milieu + 1
        elif x == tab[milieu]:   #gagne
            position = milieu
            fini = True
        if debut > fin:  #element non trouve
            fini = True
    return position



print 'test de la recherche dichotomique'
t = [-3,0,1,2,2,3,3,3,4,5,6,6]
print t
for x in t + [-5, 8, 2.5]: 
    print x,'est a l\'indice', recherche_dichotomique(t,x)
