import ffmpeg
import tkinter
from tkinter import filedialog
import math

def log(text):
    print(text)

def convertTo(inputpath, outputpath):
    try:
        (
            ffmpeg
            .input(inputpath)
            .output(outputpath, vcodec="libx264", acodec="aac")
            .run(capture_stdout=True, capture_stderr=True, overwrite_output=True)
        )
        log(f"Success! File saved at {outputpath}")
    except Exception as e:
        log(f"ERROR: {e}")

def browseInput():
    path = filedialog.askopenfilename(
        title="Select Input Video",
        filetypes=[
            ("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv *.webm *.m4v"),
            ("MP4 Video", "*.mp4"),
            ("MKV Video", "*.mkv"),
            ("AVI Video", "*.avi"),
            ("QuickTime Video", "*.mov")
        ]
    )
    widgets[1].delete(0, tkinter.END)
    widgets[1].insert(0, path)

def browseOutput():
    path = filedialog.asksaveasfilename(
        title="Save Output Video",
        filetypes=[
            ("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv *.webm *.m4v"),
            ("MP4 Video", "*.mp4"),
            ("MKV Video", "*.mkv"),
            ("AVI Video", "*.avi"),
            ("QuickTime Video", "*.mov")
        ]
    )
    widgets[4].delete(0, tkinter.END)
    widgets[4].insert(0, path)

def startConvert():
    inputf = widgets[1].get()
    output = widgets[4].get()
    convertTo(inputf, output)

window = tkinter.Tk()
window.title("Convert Video")

widgets = [
    tkinter.Label(window, text="Input path"),
    tkinter.Entry(window),
    tkinter.Button(window, text="Browse...", command=browseInput),
    tkinter.Label(window, text="Output path"),
    tkinter.Entry(window),
    tkinter.Button(window, text="Browse...", command=browseOutput),
]

index = 0
for x in widgets:
    x.grid(row=math.floor(index / 3), column=index % 3)
    index += 1

goButton = tkinter.Button(window, text="Convert", command=startConvert)
goButton.grid(row=math.floor(index / 3),column=0, columnspan=3)

window.mainloop()