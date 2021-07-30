#Д/З: Entry. Вводим город. Погоду ввыводить как тот раз( мы делали
#Вводим алматы
#Input    button
#City:   Almaty
#Temp:    38


import requests
import json
with open('datatemp.json') as f:
    data = json.load(f) #json (str)-> dict
for city in data['region']:
    print(city['name'], temp['temp'])



data = requests.get(URL, params=parameters)


from tkinter import *
window = Tk()
window.geometry("600x600")
window.resizable(False, False)

def print_city():
    city = inputx.get()

inputx = Entry(window, bg = 'pink')
inputx.pack()

btnx = Button(window, text="Show", bg="white", command=print_city)
btnx.pack()



window.mainloop()#ВЫВОДИМ ОКОШКУ










