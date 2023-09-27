from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageDraw



window=Tk()
window.title('Watermaker')
window.minsize(width=500,height=400)
window.configure(bg='pink')

def apply_watermark(text):
    image=open_dialog()
    w,h=image.size
    x,y=int(w/2),int(h/2)
    # this is to ensure that we place our text at the midle of the image , you can adjust this
    draw=ImageDraw.Draw(image)
    draw.text((x, y), text, fill=(255, 255, 255))
    image.show()
    # cv2.imshow('Watermarker', image)
    # cv2.waitKey(0)
    # cv2.destroyAllwindows()

def open_dialog():
    file=filedialog.askopenfilename()
    image=Image.open(file)
    # image=image.resize(image,(400,400))
    return image



# LABELS
top_label=Label(text='Image Watermark💧',font=('Arial',24,'bold'))
top_label.place(x=100,y=20)
main_label=Label(text='Text:',font=('Arial',12))
main_label.place(x=50,y=100)

# TEXTBOX
textbox=Entry(font=('Arial',12))
textbox.place(x=120,y=100)

# # BUTTON
# choose_button=Button(text='choosefile',command=open_dialog)
# choose_button.pack()

# BUTTON
apply_button=Button(text='apply watermark',command=lambda: apply_watermark(textbox.get()))
apply_button.place(x=160,y=180)


window.mainloop()



