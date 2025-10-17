from guizero import App, Picture, Box, Text
cuaso = App("man hinh dien thoai", width = 1300, height = 350)
text = Text(cuaso ,text = "Day la thoi khoa bieu cua minh", size = 20)
picture1 = Picture(cuaso, "thoikhoabieu.png")
cuaso.display()
