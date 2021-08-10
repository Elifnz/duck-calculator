import tkinter as tk
from PIL import Image, ImageTk

# Updated expression box
expression = ""


def update(number_entered):
    global expression
    expression = expression + str(number_entered)
    equation.set(expression)


# equal button
def equal_button():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("type")
        expression = ""


# clear button
def clear_button():
    global expression
    expression = ""
    equation.set("")


root = tk.Tk()
backg = "#fef6da"
canvas = tk.Canvas(root, width=400, height=600, bg=backg)
canvas.grid(columnspan=5, rowspan=8)
equation = tk.StringVar()
# Duck Calculator Title
FONT = 'impact'
duck_calculator_sign = tk.Label(root, text="Duck Calculator", font=(FONT, 25), fg="darksalmon", bd=0, bg=backg)
duck_calculator_sign.grid(columnspan=5, row=0)

# Duck Logo
image = Image.open('duck.png')
new_image = Image.new("RGBA", image.size, backg)  # Create a white rgba background
new_image.paste(image, (0, 0), image)  # Paste the image on the background. Go to the links given below for details.
new_image.convert('RGB').save('duck.jpg', "JPEG")  # Save as JPEG
duck_photo = Image.open('duck.jpg').resize((80, 80))
duck_photo = ImageTk.PhotoImage(duck_photo)
logo_label = tk.Label(image=duck_photo, bd=0)
logo_label.image = duck_photo
logo_label.grid(columnspan=4, row=0, sticky="w")
# EXPRESSİON BOX WHERE CALCULATİONS ARE DİSPLAYED
expression_field = tk.Entry(root, width=45, textvariable=equation)
expression_field.grid(columnspan=4, row=3)
# 0,1,2,3,4,5,6,7,8,9 Buttons will be written
button0 = tk.Button(root, text="0", bg="#eedc9a", fg="white", command=lambda: update(0), height="3", width="8",
                    font=FONT)
button0.grid(row=7, column=1, sticky='nsew')
button1 = tk.Button(root, text="1", bg="#eedc9a", fg="white", command=lambda: update(1), height="3", width="8",
                    font=FONT)
button1.grid(row=6, column=1, sticky='nsew')
button2 = tk.Button(root, text="2", bg="#eedc9a", fg="white", command=lambda: update(2), height="3", width="8",
                    font=FONT)
button2.grid(row=6, column=2, sticky='nsew')
button3 = tk.Button(root, text="3", bg="#eedc9a", fg="white", command=lambda: update(3), height="3", width="8",
                    font=FONT)
button3.grid(row=6, column=3, sticky='nsew')
button4 = tk.Button(root, text="4", bg="#eedc9a", fg="white", command=lambda: update(4), height="3", width="8",
                    font=FONT)
button4.grid(row=5, column=1, sticky='nsew')
button5 = tk.Button(root, text="5", bg="#eedc9a", fg="white", command=lambda: update(5), height="3", width="8",
                    font=FONT)
button5.grid(row=5, column=2, sticky='nsew')
button6 = tk.Button(root, text="6", bg="#eedc9a", fg="white", command=lambda: update(6), height="3", width="8",
                    font=FONT)
button6.grid(row=5, column=3, sticky='nsew')
button7 = tk.Button(root, text="7", bg="#eedc9a", fg="white", command=lambda: update(7), height="3", width="8",
                    font=FONT)
button7.grid(row=4, column=1, sticky='nsew')
button8 = tk.Button(root, text="8", bg="#eedc9a", fg="white", command=lambda: update(8), height="3", width="8",
                    font=FONT)
button8.grid(row=4, column=2, sticky='nsew')
button9 = tk.Button(root, text="9", bg="#eedc9a", fg="white", command=lambda: update(9), height="3", width="8",
                    font=FONT)
button9.grid(row=4, column=3, sticky='nsew')

# =,/,*,+,- buttons
buttonequal = tk.Button(root, text=" = ", bg="#eedc9a", fg="white", command=equal_button(), height="3", width="8",
                        font=FONT)
buttonequal.grid(row=7, column=3, sticky='nsew')
buttondivide = tk.Button(root, text=" / ", bg="#eedc9a", fg="white", command=lambda: update("/"), height="3", width="8",
                         font=FONT)
buttondivide.grid(row=4, column=4, sticky='nsew')
buttonmultiply = tk.Button(root, text=" x ", bg="#eedc9a", fg="white", command=lambda: update("*"), height="3",
                           width="8",
                           font=FONT)
buttonmultiply.grid(row=5, column=4, sticky='nsew')
buttonsubtract = tk.Button(root, text=" - ", bg="#eedc9a", fg="white", command=lambda: update("-"), height="3",
                           width="8",
                           font=FONT)
buttonsubtract.grid(row=6, column=4, sticky='nsew')
buttonadd = tk.Button(root, text=" + ", bg="#eedc9a", fg="white", command=lambda: update("+"), height="3", width="8",
                      font=FONT)
buttonadd.grid(row=7, column=4, sticky='nsew')
buttondecimal = tk.Button(root, text=" . ", bg="#eedc9a", fg="white", command=lambda: update("."), height="3",
                          width="8",
                          font=FONT)
buttondecimal.grid(row=7, column=2, sticky='nsew')
buttonclear = tk.Button(root, text="Clear ", bg="#eedc9a", fg="white", command=clear_button, height="3", width="8",
                        font=FONT)
buttonclear.grid(row=3, column=4, sticky='nsew')

root.mainloop()
