class cdjcalc():
    jvCalc=0.0
    def __init__(self, param1=0.0):
        self.param1=param1
    
    def fjcalc(self):
        self.jvCalc+=self.param1
        print(self.jvCalc)