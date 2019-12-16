from tkinter import *

root=Tk()
root.title("Cryptograph o'Mine")
root.iconbitmap("desktop/alphabet/signature.ico")
photo_a = PhotoImage(file="desktop/alphabet/a.png")
photo_b = PhotoImage(file="desktop/alphabet/b.png")
photo_c = PhotoImage(file="desktop/alphabet/c.png")
photo_ç = PhotoImage(file="desktop/alphabet/ç.png")
photo_d = PhotoImage(file="desktop/alphabet/d.png")
photo_e = PhotoImage(file="desktop/alphabet/e.png")
photo_f = PhotoImage(file="desktop/alphabet/f.png")
photo_g = PhotoImage(file="desktop/alphabet/g.png")
photo_ğ = PhotoImage(file="desktop/alphabet/ğ.png")
photo_h = PhotoImage(file="desktop/alphabet/h.png")
photo_ı = PhotoImage(file="desktop/alphabet/ı.png")
photo_i = PhotoImage(file="desktop/alphabet/i.png")
photo_j = PhotoImage(file="desktop/alphabet/j.png")
photo_k = PhotoImage(file="desktop/alphabet/k.png")
photo_l = PhotoImage(file="desktop/alphabet/l.png")
photo_m = PhotoImage(file="desktop/alphabet/m.png")
photo_n = PhotoImage(file="desktop/alphabet/n.png")
photo_o = PhotoImage(file="desktop/alphabet/o.png")
photo_ö = PhotoImage(file="desktop/alphabet/ö.png")
photo_p = PhotoImage(file="desktop/alphabet/p.png")
photo_r = PhotoImage(file="desktop/alphabet/r.png")
photo_s = PhotoImage(file="desktop/alphabet/s.png")
photo_ş = PhotoImage(file="desktop/alphabet/ş.png")
photo_t = PhotoImage(file="desktop/alphabet/t.png")
photo_u = PhotoImage(file="desktop/alphabet/u.png")
photo_ü = PhotoImage(file="desktop/alphabet/ü.png")
photo_v = PhotoImage(file="desktop/alphabet/v.png")
photo_y = PhotoImage(file="desktop/alphabet/y.png")
photo_z = PhotoImage(file="desktop/alphabet/z.png")
photo_dot = PhotoImage(file="desktop/alphabet/dot.png")
photo_semi = PhotoImage(file="desktop/alphabet/semi.png")
photo_warn = PhotoImage(file="desktop/alphabet/warn.png")
photo_question = PhotoImage(file="desktop/alphabet/question.png")
photo_semidot = PhotoImage(file="desktop/alphabet/semi_dot.png")
photo_dotdot = PhotoImage(file="desktop/alphabet/dot_dot.png")
sizex = 600
sizey = 400
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
col_l=0
row_l=0
labels = []
element=0
myframe=Frame(root,width=400,height=300,bd=2,relief=GROOVE)
myframe.place(x=10,y=10)
try:
    f = open("desktop/filler.txt",mode = 'r',encoding = 'utf-8')
    lines = f.read()
finally:
    f.close
    
    for line in lines:
        for i in line:
            if i =='a':
                labels.append(Label(root, image=photo_a))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='b':
                labels.append(Label(root, image=photo_b))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='c':
                labels.append(Label(root, image=photo_c))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='ç':
                labels.append(Label(root, image=photo_ç))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='d':
                labels.append(Label(root, image=photo_d))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='e':
                labels.append(Label(root, image=photo_e))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='f':
                labels.append(Label(root, image=photo_f))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='g':
                labels.append(Label(root, image=photo_g))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='ğ':
                labels.append(Label(root, image=photo_ğ))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='h':
                labels.append(Label(root, image=photo_h))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='ı':
                labels.append(Label(root, image=photo_ı))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='i':
                labels.append(Label(root, image=photo_i))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='j':
                labels.append(Label(root, image=photo_j))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='k':
                labels.append(Label(root, image=photo_k))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='l':
                labels.append(Label(root, image=photo_l))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='m':
                labels.append(Label(root, image=photo_m))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='n':
                labels.append(Label(root, image=photo_n))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='o':
                labels.append(Label(root, image=photo_o))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='ö':
                labels.append(Label(root, image=photo_ö))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='p':
                labels.append(Label(root, image=photo_p))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='r':
                labels.append(Label(root, image=photo_r))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='s':
                labels.append(Label(root, image=photo_s))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='ş':
                labels.append(Label(root, image=photo_ş))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='t':
                labels.append(Label(root, image=photo_t))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='u':
                labels.append(Label(root, image=photo_u))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='ü':
                labels.append(Label(root, image=photo_ü))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='v':
                labels.append(Label(root, image=photo_v))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='y':
                labels.append(Label(root, image=photo_y))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='z':
                labels.append(Label(root, image=photo_z))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='.':
                labels.append(Label(root, image=photo_dot))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i ==',':
                labels.append(Label(root, image=photo_semi))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i ==':':
                labels.append(Label(root, image=photo_dotdot))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i ==';':
                labels.append(Label(root, image=photo_semidot))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='?':
                labels.append(Label(root, image=photo_question))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='!':
                labels.append(Label(root, image=photo_warn))
                labels[element].place(x=10+(25*col_l),y=10+(30*row_l))
                element+=1
            elif i =='\n':
                row_l+=1
                col_l=-1
            col_l+=1
        


root.mainloop()