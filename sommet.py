class Sommet:
    
    def __init__(self, etiquette, rentrant, sortant):
        self.etiquette = etiquette
        self.rentrant = rentrant
        self.sortant = sortant
        
    def getPredecessor(self):
        return self.rentrant
    
    def getSuccessor(self):
        return self.sortant
    
    def __str__(self):
        return str(self.etiquette) + " "