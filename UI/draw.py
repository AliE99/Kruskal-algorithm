from tkinter import *


class Graphic:
    def draw(self, result):
        canvas_width = 1280
        canvas_height = 760
        python_green = "#476042"

        master = Tk()

        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        w.pack()
        points = []
        w.create_text(canvas_width / 2,
                      20,
                      text="Kruskal Graph", fill="#476042")

        for i in range(0, len(result)):
            w.create_line(self[result[i][0]].x * 20, self[result[i][0]].y * 20, self[result[i][1]].x * 20,
                          self[result[i][1]].y * 20)

        for i in range(0, len(self)):
            w.create_oval(self[i].x * 20 - 25, self[i].y * 20 - 25, self[i].x * 20 + 25, self[i].y * 20 + 25,
                              outline="#000000",
                          fill="#B3B3B3", width=2)

        for i in range(0, len(self)):
            w.create_text(self[i].x * 20, self[i].y * 20, anchor=W, font="Purisa",
                          text=i)

        mainloop()
