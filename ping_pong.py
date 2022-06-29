from pygame import *

class Karakter(sprite.Sprite):
    def __init__(self, krk_image, krk_x, krk_y, krk_hiz, genislik, yukseklik):
        super().__init__()
        self.image = transform.scale(image.load(krk_image),(genislik,yukseklik))
        self.hiz = krk_hiz

        self.rect = self.image.get_rect()
        self.rect.x = krk_x
        self.rect.y = krk_y

    def ciz(self):
        pencere.blit(self.image,(self.rect.x,self.rect.y))


#raketlerin oluşturulması
class Oyuncu(Karakter):
    def update_r(self):
        basilan_tuslar = key.get_pressed()
        if basilan_tuslar[K_UP] and self.rect.y >5:
            self.rect.y -= self.hiz
        if basilan_tuslar[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.hiz 

    def update_l(self):
        basilan_tuslar = key.get_pressed()
        if basilan_tuslar[K_w] and self.rect.y >5:
            self.rect.y -= self.hiz
        if basilan_tuslar[K_s] and self.rect.y < 420:
            self.rect.y += self.hiz 


raket_sol = Oyuncu("racket.png",30,200,4,50,150)
raket_sag = Oyuncu("racket.png",520,200,4,50,150)

top = Karakter("tenis_ball.png",200,200,4,50,50)




#oyun penceresi oluşturma
pencere = display.set_mode((600,500))
#pencere arkaplan rengi RGB kodu
pencere.fill((200,180,200))


game = True
FPS = 60
clock = time.Clock()

yatat_hiz = 3
dikey_hiz = 3

#yazı taslakları
font.init()
yazi_taslagı = font.Font(None ,40)
lose1= yazi_taslagı.render("1. OYUNCU KAYBETTİ",True,(0,0,0))
lose2= yazi_taslagı.render("2. OYUNCU KAYBETTİ",True,(0,0,0))

#oyun döngüsü
while game:
    # eğer çarpı işaretine basılırsa pencereyi kapat
    for e in event.get():
        if e.type == QUIT:
            game = False

    pencere.fill((200,180,200))
    raket_sag.ciz()
    raket_sol.ciz()
    top.ciz()

    raket_sol.update_l()
    raket_sag.update_r()


    #topun hareketi
    top.rect.x = top.rect.x + yatat_hiz
    top.rect.y = top.rect.y + dikey_hiz

    #topun alt üst duvara sekmesi
    if top.rect.y > 450 or top.rect.y < 0:
        dikey_hiz = dikey_hiz* (-1)

    #raketlerden sekme
    if sprite.collide_rect(raket_sol,top) or  sprite.collide_rect(raket_sag,top):
        yatat_hiz = yatat_hiz * (-1)

    #kaybetme kontrölü
    if top.rect.x < 0:
        pencere.blit(lose1,(200,200))
    
    if top.rect.x > 600:
        pencere.blit(lose2,(200,200))
    

    #ekranı güncelle
    display.update()
    clock.tick(FPS)


