from random import randint

class Personagem:
    def __init__(self):
        self.nome="Jess"
        self.hp=1
        self.hpmax=1
    def dano(self,inimigo):
        dano = min(max(randint(0, self.hp) - randint(0, inimigo.hp), 0),inimigo.hp)
        inimigo.hp = inimigo.hp - dano
        if dano == 0:
            print (f"{inimigo.nome} esquivou do ataque de {self.nome}.")
        else: print (f"{self.nome} feriu {inimigo.nome}!")
        return inimigo.hp <= 0

class Monstro(Personagem):
    def __init__(self, jogador):
        Personagem.__init__(self)
        nomes = ["Goblin","Morcego","Zumbi","Bruxa","Afogador","Vampiro"]
        self.nome = nomes[randint(0, 5)]
        self.hp = randint(1, jogador.hp)
        
class jogador (Personagem):
    def __init__(self,nome):
        Personagem.__init__(self)
        self.estado="normal"
        self.hp=10
        self.hp_max=10
        self.nome = nome
    def sair (self):
      print (f"{self.nome} nao pode achar uma saida e morre de fome.\nR.I.P.")
      self.hp = 0
    def ajuda (self): print (Comandos.keys())
    def status (self):print (f" saude de {self.nome} : {self.hp}/{self.hp_max}")
    def cansado (self):
       print (f"{self.nome} se sente cansado")
       self.hp = max(1, self.hp - 1)
    def descansar (self):
        if self.estado != 'normal':
            print (f"{self.nome} nao pode descansar agora!")
            self.ataque_inimigo()
        else:
            print (f"{self.nome} descansa...")
            if randint(0,1):
                self.inimigo = Monstro(self)
                print (f"{self.nome} e rudamente acordado por {self.inimigo.nome}!")
                self.estado = 'luta'
                self.ataque_inimigo()
            else:
                if self.hp < self.hp_max:
                    self.hp = self.hp + 1
                else: print (f"{self.nome}dormiu demais."); self.hp = self.hp - 1
    def explorar (self):
        if self.estado != 'normal':
            print (f"{self.nome} esta muito ocupado agora.")
            self.ataque_inimigo()
        else:
            print (f"{self.nome} explora uma passagem assombrosa.")
            if randint(0,1):
                self.inimigo = Monstro(self)
                print (f"{self.nome} encontra {self.inimigo.nome}!")
                self.estado = 'luta'
            else:
                if randint(0,1): self.cansado()
    def ataque (self):
        if self.estado !='luta':
            print (f"{self.nome} soca o ar, aparentimente sem resultados.")
            self.cansado()
        else:
            if self.dano(self.inimigo):
                print (f"{self.nome} executa {self.inimigo.nome}!")
                self.inimigo = None
                self.estado = 'normal'
                if randint(0, self.hp) < 10:
                    self.hp_max = self.hp_max + 1
                    print (f"{self.nome} se sente mais forte!")
            else: self.ataque_inimigo()
    def ataque_inimigo(self):
        if self.inimigo.dano(self):
            print (f"{self.nome} foi assassino por {self.inimigo.nome} !!!\nR.I.P")

Comandos = {
    "sair": jogador.sair,
    "ajuda": jogador.ajuda,
    "status": jogador.status,
    "descansar": jogador.descansar,
    "explorar": jogador.explorar,
    "atacar": jogador.ataque,
    }
restart = True    
    
while restart :                   
    p = jogador(input("qual sera o nome de seu personagem?  "))
    
    print ("digite ajuda para uma lista de comandos")
    p.ajuda()
    print (f"{p.nome}s entra numa cavena escura procurando por uma aventura") 

    while p.hp > 0 :
        controle = input("> ")
        comandoencontrar = False
        for comando in Comandos.keys():
            if comando == controle:
                Comandos[controle](p)
                comandoencontrar = True
        if not comandoencontrar:
            print ("nao foi possivel executar esse comando, favor digitar outra vez")

    pergunta = input("GAME OVER, se deseja recomesar digite = 1, se nao digite 0 ")
    if pergunta == '0':
        restart = False
    else:
        p.hp = 10
        p.hpmax = 10