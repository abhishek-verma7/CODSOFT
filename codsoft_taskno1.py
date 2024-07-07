#CALCULATOR

from tkinter import*

first_number=second_number=operator=None
def get_digit(digit):
    current=result_label["text"]
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global  first_number , operator
    first_number=int(result_label["text"])
    operator=op
    result_label.config(text='')
def get_result():
    global first_number,second_number,operator
    second_number= int(result_label["text"])
    if operator == "+":
        result_label.config(text=str(first_number+second_number))
    elif operator == "-":
        result_label.config(text=str(first_number-second_number))
    elif operator == "*":
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(first_number/second_number))
        

root = Tk()
root.title("Calculator")
root.geometry("258x370")
root.resizable(0,0)
root.config(bg="black")


result_label=Label(root,text='',bg="black",fg='white')
result_label.grid(row=0,column=0,columnspan=500,pady=(50,25),sticky="w")
result_label.config(font=("Arial ",30,"bold"))


b7=Button(root,text=7,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(7))
b7.grid(row=1,column=0)
b7.config(font=("Arial ",14))

b8=Button(root,text=8,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(8))
b8.grid(row=1,column=1)  
b8.config(font=("Arial ",14))

b9=Button(root,text=9,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(9))
b9.grid(row=1,column=2)
b9.config(font=("Arial ",14))

b_add=Button(root,text='+',bg='#FF4136',fg="white",width=5,height=2,command=lambda :get_operator("+"))
b_add.grid(row=1,column=3)
b_add.config(font=("Arial ",14))


b4=Button(root,text=4,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(4))
b4.grid(row=2,column=0)
b4.config(font=("Arial ",14))

b5=Button(root,text=5,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(5))
b5.grid(row=2,column=1)
b5.config(font=("Arial ",14))

b6=Button(root,text=6,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(6))
b6.grid(row=2,column=2)
b6.config(font=("Arial ",14))

b_sub=Button(root,text='-',bg='#FF4136',fg="white",width=5,height=2,command=lambda :get_operator("-"))
b_sub.grid(row=2,column=3)
b_sub.config(font=("Arial ",14))


b1=Button(root,text=1,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(1))
b1.grid(row=3,column=0)
b1.config(font=("Arial ",14))

b2=Button(root,text=2,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(2))
b2.grid(row=3,column=1)
b2.config(font=("Arial ",14))

b3=Button(root,text=3,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(3))
b3.grid(row=3,column=2)
b3.config(font=("Arial ",14))

b_mult=Button(root,text='*',bg='#FF4136',fg="white",width=5,height=2,command=lambda :get_operator("*"))
b_mult.grid(row=3,column=3)
b_mult.config(font=("Arial ",14))



b_c=Button(root,text="C",bg='#FF4136',fg="white",width=5,height=2,command=lambda :clear())
b_c.grid(row=4,column=0)
b_c.config(font=("Arial ",14))

b_z=Button(root,text=0,bg='#0074D9',fg="white",width=5,height=2,command=lambda:get_digit(0))
b_z.grid(row=4,column=1)
b_z.config(font=("Arial ",14))

b_equal=Button(root,text="=",bg='#FF4136',fg="white",width=5,height=2,command=get_result)
b_equal.grid(row=4,column=2)
b_equal.config(font=("Arial ",14))

b_div=Button(root,text='/',bg='#FF4136',fg="white",width=5,height=2,command=lambda :get_operator("/"))
b_div.grid(row=4,column=3)
b_div.config(font=("Arial ",14))

root.mainloop()

