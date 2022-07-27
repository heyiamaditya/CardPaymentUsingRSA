from Prime import p ,q
from Interface import values
import PySimpleGUI as pg



pg.theme('TealMono')
font=('Britannic Bold',15)

e=1

n=p*q

def check_gcd(i, Φn):
    if i == 0:
        #print(Φn, "\n")
        return Φn + i
    else:

        return (check_gcd(Φn % i, i))




def select_e(Φn):
    for i in range(2,Φn):
        if check_gcd(i,Φn)==1:
            return i
        else :
            i+=1


Φn=(p-1)*(q-1)
e=select_e(Φn)

print("e=",e,"\n")
print("Φn=",Φn,"\n")
print("p=",p,"\n")
print("q=",q,"\n")
print(values['acc'])


def calucate_d(e):
    j = 0
    i = 1
    while j < 1:
        d = ((Φn * i) + 1) / e
        if (d % 1) == 0:
            j = 1
        else:
            i += 1
    return d


def encryption(plain):
    return(pow(plain,e,n))

e1=int(values['acc'])
e2=int(values['cvv'])
e3=int(values['card'])
e4=int(values['phn'])

c1=encryption(e1)
c2=encryption(e2)
c3=encryption(e3)
c4=encryption(e4)
print("e1",e1)

def em_show():

    return(c1,c2,c3,c4)

d=int(calucate_d(e))

def decryption(cipher):
    print("cipher",cipher)
    return(pow(cipher,d)%n)


print ('d=',d)

def d_show():
    return (decryption(c1), decryption(c2),
            decryption(c3), decryption(c4))


layout2=[[pg.Text("Do you want to view encrypted text")],
         [pg.Button("YES") , pg.Button("NO")],
         [pg.Image('image.png', size=(0,250))],
         [pg.Text("For Decryption enter Key")],
         [pg.In(size=(25,1),enable_events=True,key="decrypt")],
         [pg.Button("OK")]
        ]

encrypt= pg.Window("Encryption / Decryption",layout2,size=(700,600),font=font)

while True:
    new_event ,new_values =encrypt.read()

    if new_event =="YES":
        pg.popup('Encrypted details',em_show(),font=font)
    if new_event =="OK" or new_event == pg.WIN_CLOSED:
        print("new" ,new_event)
        val=int(new_values['decrypt'])
        if(val==d):
            print('Yes')
            pg.popup('Decrypted details', d_show(), font=font)

        break


encrypt.close()
print (d)