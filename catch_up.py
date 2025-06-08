from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)
sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)
x1 = 100
y1 = 300
x2= 50
y2 = 400
#обработай событие «клик по кнопке "Закрыть окно"»
clock = time.Clock()
FPS = 60
game = True
while game:

    clock.tick(FPS)

    
    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()
    speed = 10
    
    
    x1 = 100
    y1 = 300
    x2= 50
    y2 = 400   

      
    display.update()