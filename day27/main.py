import tkinter

window = tkinter.Tk()
window.title("My First Tkinter Application")
window.minsize(width=500,height=250)


#Labels
mylabel = tkinter.Label(text="Convert from Miles to KM", font=("Arial", 10,'bold' ))
mylabel.place(x=0,y=0)
mylabel2 = tkinter.Label(text="Miles", font=("Arial", 10, ))
mylabel2.place(x=320,y=70)
mylabel3 = tkinter.Label(text="Enter the distance in MILES that you want to convert to KM", font=("Arial", 10 ))
mylabel3.place(x=90,y=40)
mylabel4 = tkinter.Label(font=("Arial", 10 ))
mylabel4.place(x=230,y=135)


#Inputs
m_input = tkinter.Entry(width=20)
m_input.place(x=190,y=70)

def clicked_button():
    miles = float(m_input.get())
    km = miles * 1.609344
    mylabel4.config(text=f"{km:.2f} KM")
    
#Buttons
    
calculate_btn = tkinter.Button(text="Convert to KM", command=clicked_button)
calculate_btn.place(x=210,y=100)



window.mainloop()