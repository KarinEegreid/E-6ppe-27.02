# Karl Paju IS22

from tkinter import * # importime Tkinteri raamistiku
raam = Tk() # Loome Tkinteri akna
raam.title("Tühi Tahvel") # Määrame akna pealkirja
tahvel = Canvas(raam, width=600) # Loome ekraani, mille laius on 600 ning mis võimaldab joonistada erinevaid objekte

tahvel.create_rectangle(50,70,100,100, width=2, outline="blue") # Loome tahvli peal ristküliku (50,70) - (100,100) ja määrame selle joonelaiuse 2 pikslit ja ääre värviks sinine
tahvel.create_text(50,50, text="Tere!") # Loome tahvli peal teksti objekti (50,50) ja määrame selle sisuks "Tere!"

tahvel.create_polygon(100,100,150,150,200,100, fill="red",outline="black") # Loome tahvli peal polügooni, mille nurkade koordinaadid on (100,100), (150,150), (200,100) ja määrame selle täitevärviks "red" ja ääre värviks "black"

tahvel.pack() # Paneb tahvli akna sisse
raam.mainloop() # käivitab akna peal töötavat tsüklit, mis võimaldab akent muuta ja interakteeruda kasutajaga