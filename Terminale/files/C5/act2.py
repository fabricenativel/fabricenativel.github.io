class Duree:

    def __init__(self,heures,minutes,secondes):
        self.heures=heures
        self.minutes=minutes
        self.secondes=secondes

    def __strt__(self):
        return f"{self.heures}h {self.minutes}m {self.secondes}s"
    
    
