import pyautogui
import random
from pyautogui import *
FAILSAFE = True

comentarios_tiktok = [
    "Amei essa energia! 🌟",
    "Esse passo é incrível! Preciso aprender! 🕺",
    "Uau, que criatividade! 👏",
    "Esse conteúdo é top! Continuem assim! 🔥",
    "Esse truque é tudo! Vou tentar! ✨",
    "Qual é a sua inspiração para isso? 🤔",
    "Amo como você se expressa! ❤️",
    "Essa edição tá perfeita! 🎬",
    "Você me fez rir! 😂",
    "Essa música combina muito com o seu vídeo! 🎶",
    "Isso é muito original! 👏",
    "A mensagem é poderosa! 💪",
    "Fiquei grudado nesse vídeo! 😍",
    "Quero ver mais conteúdos assim! 👍",
    "Qual é o segredo por trás dessa ideia? 🤫"
]

def interagir(imagem,texto=None):
    posi = locateOnScreen(imagem,confidence=0.9)
    moveTo(posi,duration=3)
    click()
    if texto != None:
        typewrite(texto,interval=0)
        press('enter')
        
def bot():
    #1) Abrir o navegador(no meu caso é o Brave) ,abrir uma aba nova e entrar no tiktok.com
    interagir('imagens/navegador.png')
    interagir('imagens/aba.png','tiktok.com')
    sleep(22)
    #2)manter o loop rodando para ver todos os vídeos
    try:
         while True:
            interagir('like.png')
            sleep(2)
            click(x=874, y=501, interval=1)#essa posição pode mudar dependendo do monitor
            sleep(5)
            comentario_aleatorio = random.choice(comentarios_tiktok)
            interagir('imagens/comentar.png', texto=comentario_aleatorio)
            interagir('imagens/sair.png')
            sleep(5)
            press('down')
    except KeyboardInterrupt:
        print('\n')

if __name__ == '__main__':
    bot()
