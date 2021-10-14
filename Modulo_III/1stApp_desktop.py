import PySimpleGUI as sg

button_size = (6,3)

PLAYER_ONE = "O"
PLAYER_TWO = "X"

current_player = PLAYER_ONE



layout = [[
            sg.Button("", key="Primero", size=button_size),
            sg.Button("", key="Segundo", size=button_size),
            sg.Button("", key="Tercero", size=button_size)
          ],
          [
            sg.Button("", key="Cuarto", size=button_size),
            sg.Button("", key="Quinto", size=button_size),
            sg.Button("", key="Sexto", size=button_size)
          ],
          [
            sg.Button("", key="Septimo", size=button_size),
            sg.Button("", key="Octavo", size=button_size),
            sg.Button("", key="Noveno", size=button_size)
          ],
          [
            sg.Button("Terminar", key="Terminar")
          ]
        ]


window = sg.Window("Gato y raton",layout, margins=(100,100))


#AQUÍ SE ENCUENTRA EL BUCLE
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Terminar":
        break

    print(window.Element(event).ButtonText)

    if window.Element(event).ButtonText == "": #Solo si la propiedad ButtonText  esta vacia vamos a poder marcarla
        window.Element(event).Update(text=current_player)
        #Y cambia de jugador
        if current_player == PLAYER_ONE: #Si llegamos aqui y es el jugador uno deberiamos cambiar
            current_player = PLAYER_TWO
        else: #Si llegamos aqui y es el jugador dos uno deberiamos cambiar
            current_player = PLAYER_ONE



    print(values)

window.Close()

    

