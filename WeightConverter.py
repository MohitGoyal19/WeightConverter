from tkinter import *

window = Tk()

def kgToOther():
    text1.delete('1.0', END)
    text1.insert(END, float(entry1Value.get())*1000)
    text2.delete('1.0', END)
    text2.insert(END, float(entry1Value.get())*2.20462)
    text3.delete('1.0', END)
    text3.insert(END, float(entry1Value.get())*35.274)

label1 = Label(window, text = 'Enter weight in Kilograms', width = '50')
label1.grid(row = '0', column = '0', columnspan = '2')

entry1Value = StringVar()
entry1 = Entry(window, width = '50', textvariable = entry1Value)
entry1.grid(row = '0', column = '2', columnspan = '2')

button1 = Button(window, text = 'Convert', command = kgToOther, width = '50')
button1.grid(row = '0', column = '4', columnspan = '2')

label2 = Label(window, text = 'In Grams', width = '25', height = '3')
label2.grid(row = '1', column = '0')

text1 = Text(window, height = '1', width = '25')
text1.grid(row = '1', column = '1')

label3 = Label(window, text = 'In Pounds', width = 25, height = '3')
label3.grid(row = '1', column = '2')

text2 = Text(window, height = '1', width = '25')
text2.grid(row = '1', column = '3')

label4 = Label(window, text = 'In Ounces', width = '25', height = '3')
label4.grid(row = '1', column = '4')

text3 = Text(window, height = '1', width = '25')
text3.grid(row = '1', column = '5')

window.mainloop()
