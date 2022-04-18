import random
from tkinter import*

root = Tk()
root.geometry("700x1000")
text=Text(root)
user_input =Entry(root,width=42,font=("arial",20,"bold"),bg="blue")
user_input.place(x=1,y=960)

greetings = ['Hollo !','hi',"hii",'hello', 'hi,how can i help you !', 'Hi', 'hey!', 'hey']
question = ['how are you', 'How are you doing?',"how are you feel","whats up"]
responses = ['Okay', "I'm fine","I,m good","Happy !"]
menu=["i want to buy something","what is on the menu","what do you reccommend?"]
menuresponse=["we sell pizza !","pizzas and Burggers are in the menu","coffie and tea are in the menu"]
name=["whats your name","what is your name","do you have any name","what should i call you"]
nameresponse=["you can call me zoomato servise","you can call me swiggy serviese"]
bye=["cya","see you letter","bye","byy","good bye","i am leaving","have a good day"]
byeresponse=["bye !","Goodbye !","talk to you letter","Have a nice day","see you soon"]
h= ["I did not understand what you said","Sorry! what "]

def fun():
    send=user_input.get()
    text.insert(END,"\n"+send)
    user_text = user_input.get()
    if user_text in greetings:
        l=Label(root,text=user_text,font=("arial",20,"bold"))
        l.pack(anchor=SE)
        bot_text = random.choice(greetings)
    elif user_text in question:
        l=Label(root,text=user_text,font=("arial",20,"bold"))
        l.pack(anchor=SE)
        bot_text = random.choice(responses)
    elif user_text in menu:
        l=Label(root,text=user_text,font=("arial",20,"bold"))
        l.pack(anchor=SE)
        bot_text = random.choice(menuresponse)
    elif user_text in name:
        l=Label(root,text=user_text,font=("arial",20,"bold"))
        l.pack(anchor=SE)
        bot_text = random.choice(nameresponse)
    elif user_text in bye:
        l=Label(root,text=user_text,font=("arial",20,"bold"))
        l.pack(anchor=SE)
        bot_text = random.choice(byeresponse)
    else:
        l=Label(root,text=user_text,font=("arial",20,"bold"))
        l.pack(anchor=SE)
        bot_text = random.choice(h)
    a=Label(root,text=bot_text+"\n",font=("arial",20,"bold"),anchor=NW)
    a.pack(anchor=NW)
    user_input.delete(0,END)
button = Button(root, text="SEND", command=fun,bg="sky blue")
button.place(x=636,y=965) 
root.mainloop()