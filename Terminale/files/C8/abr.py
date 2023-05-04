import graphviz as gv

GREY = '#e0e0e0'
BLEU = 'lightblue'
ROUGE = 'salmon'

NODE_OPTS = {
    'fixedsize': 'true',
    'width': '0.25',
    'height': '0.25',
    'style': 'filled',
    'fontsize': '10',
    'fillcolor': GREY
}

class ABR:

    arbre_id = 0
    
    def __init__(self, valeur=None):
        self.valeur = valeur
        self.id = ABR.arbre_id
        ABR.arbre_id += 1
        if valeur is not None:
            self.gauche = ABR()
            self.droit = ABR()

    def est_vide(self):
        return self.valeur is None

    def insere_une_valeur(self, v):
        if self.est_vide():
            self.valeur = v
            self.gauche = ABR()
            self.droit = ABR()
        elif v > self.valeur:
                self.droit.insere_une_valeur(v)
        elif v < self.valeur:
                self.gauche.insere_une_valeur(v)

    def insere_valeurs(self, values):
        for v in values:
            self.insere_une_valeur(v)

    def show(self, show_vide=True, colored=False):
        
        def representation(dot, arbre, aretes, color):
            dot_node_id = str(arbre.id) 
            if arbre.est_vide() and show_vide:
                dot.node(dot_node_id, 'ø', {'shape': 'plaintext', 'style': ''})
            elif not arbre.est_vide():
                dot.node(dot_node_id, str(arbre.valeur), {'fillcolor':color if colored else GREY})
                representation(dot, arbre.gauche, aretes, BLEU)
                if not arbre.gauche.est_vide() or show_vide:
                    aretes.append((dot_node_id, str(arbre.gauche.id)))
                representation(dot, arbre.droit, aretes, ROUGE)
                if not arbre.droit.est_vide() or show_vide:
                    aretes.append((dot_node_id, str(arbre.droit.id)))

        dot = gv.Graph(format='svg', node_attr=NODE_OPTS)
        aretes = []
        representation(dot, self, aretes, GREY)
        dot.edges(aretes)
        return dot


EX9 = ABR()
EX9.insere_valeurs([12, 10, 15, 5, 20, 4, 8])
img = EX9.show(True,True)
img.render(view=True)
