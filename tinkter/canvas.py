from tkinter import *
root = Tk()
canvasWidth = 800
canvasheight = 400
root.geometry(f"{canvasWidth}x{canvasheight}")
canvas_widget = Canvas(root, width=canvasWidth, height=canvasheight)
canvas_widget.pack()

# line for
canvas_widget.create_line(00, 0, 800, 200)
canvas_widget.create_rectangle(100, 200, 200, 400, fill="red")
canvas_widget.create_text(200, 200, text="Saksham")
root.mainloop()
