import PySimpleGUI as sg

button_size = (6,3)

PLAYER_ONE = "O"
PLAYER_TWO = "X"

current_player = PLAYER_ONE

deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0,]

winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

layout = [[
            sg.Button("", key="-0-", size=button_size),
            sg.Button("", key="-1-", size=button_size),
            sg.Button("", key="-2-", size=button_size)
          ],
          [
            sg.Button("", key="-3-", size=button_size),
            sg.Button("", key="-4-", size=button_size),
            sg.Button("", key="-5-", size=button_size)
          ],
          [
            sg.Button("", key="-6-", size=button_size),
            sg.Button("", key="-7-", size=button_size),
            sg.Button("", key="-8-", size=button_size)
          ],
          [
            sg.Button("Terminar", key="Terminar")
          ]
        ]


window = sg.Window("Gato y raton",layout, margins=(100,100))


game_end = False

#AQUÍ SE ENCUENTRA EL BUCLE
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Terminar":
        break

    
    if window.Element(event).ButtonText == "" and not game_end: #Solo si la propiedad ButtonText  esta vacia vamos a poder marcarla
        index = int(event.replace("-", "")) 
        deck[index] = current_player #Actualizamos el tablero virtual
        window.Element(event).Update(text=current_player)

        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] !=0:
                if deck[winner_play[0]] == PLAYER_ONE:
                    print("El jugador 1 ha ganado")
                    game_end = True
                else: 
                    print("El jugador 2 ha ganado")
                    game_end = True


        if 0 not in deck:
            game_end = True

        #Y cambia de jugador
        if current_player == PLAYER_ONE: #Si llegamos aqui y es el jugador uno deberiamos cambiar
            current_player = PLAYER_TWO
        else: #Si llegamos aqui y es el jugador dos uno deberiamos cambiar
            current_player = PLAYER_ONE



    print(values)

window.Close()

    

############################################################################### AQUÍ ME QUEDE #################################################################################################