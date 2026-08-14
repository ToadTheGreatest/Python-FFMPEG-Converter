import ffmpeg
import tkinter
import math

def log(text):
    print(text)

def convertTo(inputpath, outputpath):
    try:
        ffmpeg.input(inputpath).output(outputpath, vcodec="libx264", acodec="aac").overwriteOutput().run(capture_stdout=True, capture_stderr=True)
        log(f"Success! File saved at {outputpath}")
    except Exception as e:
        log(f"ERROR: {e}")

window = tkinter.Tk()
window.title("Convert Video")

widgets = [
    tkinter.Label(window, text="Input path"),
    tkinter.Entry(window),
    tkinter.Button(window, text="Browse..."),
    tkinter.Label(window, text="Output path"),
    tkinter.Entry(window),
    tkinter.Button(window, text="Browse..."),
]

index = 0
for x in widgets:
    x.grid(row=math.floor(index / 3), column=index % 3)
    index += 1

goButton = tkinter.Button(window, text="Convert")
goButton.grid(row=math.floor(index / 3),column=0, columnspan=3)

window.mainloop()