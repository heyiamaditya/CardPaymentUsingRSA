import PySimpleGUI as pg
pg.theme('TealMono')
font=('Britannic Bold',15)


layout = [
    [pg.Text("Enter Account Number",size=(25,1))],
    [pg.In(size=(25,1),enable_events=True,key="acc")],
    [pg.Text("Enter Phone Number")],
    [pg.In(size=(25,1),enable_events=True,key="phn")],
    [pg.Text("Enter Card Number")],
    [pg.In(size=(25,1),enable_events=True,key="card")],
    [pg.Text("Enter CVV")],
     [pg.In(size=(25,1),enable_events=True,key="cvv")],
    [pg.Image('card.png', size=(0,250))],
    [pg.Button("OK")]
]
window= pg.Window("Card Payment Details", layout,size=(700,600),font=font)

while True:
    event , values =window.read()

    if event =="OK" or event == pg.WIN_CLOSED:
        print(values)
        break


window.close()