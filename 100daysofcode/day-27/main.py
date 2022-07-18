import tkinter

def miles_to_km():
    miles = float(mile_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f'{km}')

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

mile_input = tkinter.Entry(width=7)
mile_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_buttom = tkinter.Button(text="Calculator", command=miles_to_km)
calculate_buttom.grid(column=1, row=2)




window.mainloop()



# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(500, 300)
#
# # Label
#
# my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
# my_label.pack()
#
# my_label['text'] = "New Text"
# my_label.config(text="New Text")
#
#
# # Button
#
# def button_clicked():
#     new_text = input.get()
#     my_label['text'] = new_text
#
#
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
#
# # Entry
#
# input = tkinter.Entry(width=10)
# input.pack()
# print(input.get())
#
# window.mainloop()