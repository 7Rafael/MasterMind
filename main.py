import random
import tkinter
from tkinter import *
from tkinter import messagebox

run = True

while run:

    colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Violet"]
    chances = 8
    attempts = 0
    random.shuffle(colors)
    posColors = colors[0:4]
    answer = []
    firstRun = True
    correctPos = 0
    correctColor = 0

    print(posColors)
    print(len(posColors))
    app = Tk()
    app.title('Mastermind')
    app.config(bg='#CCC')
    app.geometry('430x560')
    color = ["#CCC" , "#FFF" , "#000"]
    squarey = 60
    def exit():
        global run
        run=False
        app.destroy()
        app.quit()

    exit = Button(app, text="exit", background="Red", command=exit)
    exit.place(x=0, y=10)

    def standartLayout():
        global firstRun
        i=0
        y = 60
        if firstRun == True:
            while i < chances:
                square = Label(app, text="    ", background=color[0], borderwidth=2, relief="raised")
                square.place(x=30, y=y)
                square1 = Label(app, text="    ", background=color[0], borderwidth=2, relief="raised")
                square1.place(x=60, y=y)
                square2 = Label(app, text="    ", background=color[0], borderwidth=2, relief="raised")
                square2.place(x=90, y=y)
                square3 = Label(app, text="    ", background=color[0], borderwidth=2, relief="raised")
                square3.place(x=120, y=y)
                y += 30
                i+=1

            firstRun = False


    standartLayout()
    def layout():
        global color, squarey, correctColor, correctPos
        squarex = 30
        square = Label(app, text="    ", background=color[0], borderwidth=2, relief="raised")
        square.place(x=30, y=squarey)
        square1 = Label(app, text="    ", background=color[0],borderwidth=2, relief="raised")
        square1.place(x=60, y=squarey)
        square2 = Label(app, text="    ", background=color[0],borderwidth=2, relief="raised" )
        square2.place(x=90, y=squarey)
        square3 = Label(app, text="    ", background=color[0],borderwidth=2, relief="raised")
        square3.place(x=120, y=squarey)

        while correctPos > 0:
            square = Label(app, text="    ", background=color[2], borderwidth=2, relief="raised")
            square.place(x=squarex, y=squarey)
            correctPos -= 1
            squarex += 30
        while correctColor > 0:
            square = Label(app, text="    ", background=color[1], borderwidth=2, relief="raised")
            square.place(x=squarex, y=squarey)
            correctColor -= 1
            squarex += 30
        squarey += 30



    redAlreadyChosen = False
    blueAlreadyChosen = False
    yellowAlreadyChosen = False
    orangeAlreadyChosen = False
    violetAlreadyChosen = False
    greenAlreadyChosen = False
    i = 0
    x = 175
    y = 60
    def selected_button():
        global answer, i,x, y,red,blue,yellow,violet,green,orange

        try:
            if i < 4:
                colorPos1 = Label(app, text="    ", background=answer[i], borderwidth=2, relief="raised")
                colorPos1.place(x=x, y=y)
                i += 1
                x += 25
            if i == 4:
                red.config(state="disable")
                blue.config(state="disable")
                yellow.config(state="disable")
                violet.config(state="disable")
                green.config(state="disable")
                orange.config(state="disable")
                x = 175
                i = 0
        except:
            x = 175
            i=0


    def red_button():
        global answer, posAnswer, redAlreadyChosen
        if redAlreadyChosen == False:
            answer.append("Red")
            redAlreadyChosen = True
            selected_button()



    def blue_button():
        global answer, posAnswer,blueAlreadyChosen
        if blueAlreadyChosen == False:
            answer.append("Blue")
            blueAlreadyChosen = True
            selected_button()

    def yellow_button():
        global answer, posAnswer,yellowAlreadyChosen
        if yellowAlreadyChosen == False:
            answer.append("Yellow")
            yellowAlreadyChosen= True
            selected_button()

    def orange_button():
        global answer, posAnswer,orangeAlreadyChosen
        if orangeAlreadyChosen == False:
            answer.append("Orange")
            orangeAlreadyChosen= True
            selected_button()
    def violet_button():
        global answer, posAnswer,violetAlreadyChosen
        if violetAlreadyChosen == False:
            answer.append("Violet")
            violetAlreadyChosen= True
            selected_button()

    def green_button():
        global answer, posAnswer,greenAlreadyChosen
        if greenAlreadyChosen == False:
            answer.append("Green")
            greenAlreadyChosen= True
            selected_button()


    def checkPlace():
        global answer,posColors, redAlreadyChosen, blueAlreadyChosen, yellowAlreadyChosen, orangeAlreadyChosen, violetAlreadyChosen, greenAlreadyChosen, y,correctColor,correctPos, errorText, run
        i = 0
        while i < len(posColors):# nessa linha ele verifica conta o tamanho do código
            if answer[i] in posColors[i]:#aqui ele vai verificar se a cor está na posição correta
                #tem cor na posição correta
                correctPos+= 1
                if correctPos == 4:
                    tkinter.messagebox.showinfo(title="Parabéns", message="Você ganhou!!!")
                    result = tkinter.messagebox.askquestion(title="Jogar novamente", message="Deseja jogar novamente?")
                    if result == 'yes':
                        run = True
                        app.destroy()
                    else:
                        run = False
                        app.destroy()
                        app.quit()

            if answer[i] in posColors:#aqui ele vereifica se existe a cor
                #tem cor na tabela
                correctColor += 1
                if answer[i]in posColors[i]:
                    correctColor -=1
            i+=1

        y+= 30
        answer = []
        redAlreadyChosen = False
        blueAlreadyChosen = False
        yellowAlreadyChosen = False
        orangeAlreadyChosen = False
        violetAlreadyChosen = False
        greenAlreadyChosen = False



    def confirm_button():
        global answer,posColors,chances,attempts,red,blue,yellow,violet,green,orange, run

        red.config(state="normal")
        blue.config(state="normal")
        yellow.config(state="normal")
        violet.config(state="normal")
        green.config(state="normal")
        orange.config(state="normal")
        if attempts < chances and len(answer) == 4:
            answer = answer[0:4]
            checkPlace()
            layout()
            attempts +=1
        if attempts == chances:
            tkinter.messagebox.showinfo(title="Perdeu", message="Você perdeu!")
            result = tkinter.messagebox.askquestion(title="Jogar novamente", message="Deseja jogar novamente?")
            if result == 'yes':
                run = True
                app.destroy()
            else:
                run = False
                app.destroy()
                app.quit()


    red = Button(app, text='    ', background="Red", command=red_button)
    blue = Button(app, text='    ', background="Blue",command=blue_button)
    yellow = Button(app, text='    ', background="Yellow",command=yellow_button)
    orange = Button(app, text='    ', background="Orange", command=orange_button)
    violet = Button(app, text='    ', background="Violet", command=violet_button)
    green = Button(app, text='    ', background="Green", command=green_button)

    confirmButton = Button(app, text ='Confirm', background="White",command=confirm_button)
    confirmButton.place(x=350, y=20)
    red.place(x=175, y=20)
    green.place(x=300, y=20)
    blue.place(x=200, y=20)
    yellow.place(x=225, y=20)
    orange.place(x=250, y=20)
    violet.place(x=275, y=20)


    app.mainloop()
