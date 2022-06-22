from pygame import *

#oyun penceresi oluşturma
pencere = display.set_mode((600,500))
#pencere arkaplan rengi RGB kodu
pencere.fill((200,180,200))


game = True
FPS = 60
clock = time.Clock()

#oyun döngüsü
while game:
    # eğer çarpı işaretine basılırsa pencereyi kapat
    for e in event.get():
        if e.type == QUIT:
            game = False

    #ekranı güncelle
    display.update()
    clock.tick(FPS)


