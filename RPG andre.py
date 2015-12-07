from ramdom import randint

class Personagem:
    def __init__(self):
        self.nome="Jess"
        self.hp=1
        self.hpmax=1
    def dar_dano(self,inimigo):
        pass

class Monstro(Personagem):
    def __init__(self, jogador):
        Personagem.__init__(self)
        self.nome = "Goblin"
        self.hp = randint(1, jogador.hp)
        
class jogador (Personagem):
    def __init__(self):
        Personagem._init(self)
        self.estado="normal"
        self.hp=10
        self.hp_max=10
    def sair (self):
      print "%s nao pode achar uma saida e morre de fome.\nR.I.P." % self.nome
      self.hp = 0
    def ajuda (self): print Comandos.Keys()
    def status (self):print " saude de %s : %d/%d" % (self.nome, self.hp, self.hp_max)
    def cansado (self):
       print "%s se sente cansado" % self.nome
       self.hp = max(1, self.hp - 1)
    def descansar (self):
        if self.estado != 'normal':
            print "%s nao pode descansar agora!" % self.nome
            self.ataque_inimigo()
        else:
            print "%s descansa..." % self.nome
            if randint(0,1):
                self.inimigo = Monstro(self)
                print "%s e rudamente acordado por %s!" % (self.nome, self.inimigo.nome)
                self.estado - 'luta'
                self.ataque_inimigo()
            else:
                if self.hp < self.hp_max:
                    self.hp = self.hp + 1
                else: print "%s dormiu demais." % self.nome; self.hp = self.hp - 1
    def explorar (self):
        if self.estado != 'normal':
            print "%s esta muito ocupado agora." % self.nome
            self.ataque_inimigo()
        else:
            print "%s explora uma passagem assombrosa." % self.nome
            if randint(0,1):
                self.inimigo = Monstro(self)
                print "%s encontra %s!" % (self.nome, self.inimigo.nome)
                self.estado = 'luta'
            else:
                if randint(0,1): self.cansado()
    def ataque (self):
        if self.estado !='luta':
            print "%s soca o ar, aparentimente sem resultados." %self.nome
            self.cansado()
        else:
            if self.dano(self.inimigo):
                print "%s executa %s!" % (self.nome, self.inimigo.nome)
                self.inimigo = None
                self.estado = 'normal'
                if randint(0, self.hp) < 10:
                    self.hp = self.hp + 1
                    self.hp_max = self.hp_max + 1
                    print "%s se sente mais forte!" %self.nome
            else: self.ataque_inimigo()
    def ataque_inimigo(self):
        if self.inimigo.dano(self):
            print "%s foi assassino por %s !!!\nR.I.P" %(self.nome, self.inimigo.nome)
                        
            
           
Comandos = {
    "sair": jogador.sair,
    "ajuda": jogador.ajuda,
    "estado": jogador.estado,
    "cansado": jogador.cansado,
    "descansar": jogador.descansar,
    "explorar": jogador.explorar,
    "atacar": jogador.atacar,
    }
                    
p = jogador()
p.nome = raw_input ("qual sera o nome de seu personagem?")        
          