import os

class Manipolazione():
    def contafile(self):
        # ottengo directory corrente
        cwd = os.getcwd()
        print(cwd)

        #ottengo lista dei file nella directory corrente
        f = os.listdir(cwd)
        # calcolo il numero dei file
        c = 0
        for i in f:
            c += 1
        print(c)
        return c
    

    #creo un file ricevuto in input
    def CreaFile(self, nomefile):
        cwd = os.getcwd()
        cwd = cwd + "/" + nomefile
        print (cwd)
        open(cwd, "w")
    #modifico nome file ricevuto in input
    def modficaNomeFile(self, nomefile, nuovonome):
        os.rename(nomefile, nuovonome)
        
    #cancello file ricevuto in input
    def rimuoviFile(self, nuovonome):
        os.remove(nuovonome)



cl = Manipolazione()
print(cl.contafile())
print("Inserisci il nome del file da creare")
nome = input()
cl.CreaFile(nome)
print("inserisci il nome da moficare")
nuovonome = input()
cl.modficaNomeFile(nome, nuovonome)
print ("premi invio per cancellare il file appena modificato")
pp = input()
cl.rimuoviFile(nuovonome)