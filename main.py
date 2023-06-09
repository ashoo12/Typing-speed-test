
from tkinter import *
from tkinter import messagebox
user_text=[]
corrected_user_text=[]

def get_value():
    global cpm,wpm
    user_text.append(user_input.get(1.0,END))

    for alph in user_text:
        for n in range(len(alph)):
            print(alph[n])
            if alph[n]==quote[n]:
               corrected_user_text.append(alph[n])
               cpm=(len(corrected_user_text))
               wpm=round(cpm / 5)
               cpm_label.config(text=f"Corrected CPM={cpm}")
               wpm_label.config(text=f"Corrected WPM={wpm}")
    speed()
def speed():
    global wpm
    if wpm >= 40:
        messagebox.showinfo(message="YOUR TYPING SPEED IS AVERAGE.")
    elif wpm >=100:
        messagebox.showinfo(message="YOUR TYPING SPEED IS EXCELLENT.")
    else:
        messagebox.showinfo(message="YOUR TYPING SPEED IS LIKE A TURTLE!.")

def timer(count):
      if count>0:
            win.after(1000,timer,count-1)
            timeleft_label.config(text=f"Time Left={count}")
      else:
            user_input.config(state=DISABLED)
            timeleft_label.config(text=f"Time Left=0")
            get_value()

def restart():
    user_input.config(state=NORMAL)
    user_input.delete(1.0,END)



win=Tk()
win.minsize(width=500,height=500)
win.title("Typing Speed Test")
quote="scolding is something common in student life being a naughty boy" \
      " I am always scolded by my parents but one day I was severely scolded" \
      " by my English teacher She infect teaches well but that day i could not" \
      " resist the temptation that an adventure of nancy drew offered while " \
      "she was teaching i was completely engrossed in reading that book"\
     " nancy drew was caught in the trap laid by some smugglers"\
     " and it was then when i felt a light tap on my bent head"\
     " the teacher had caught me red handed she scolded me then and there"\
     " and insulted me in front of the whole class i was embarrassed"\
     " my cheeks burned being guilty conscious when the class was over"\
     " i went to the teacher to apologize when she saw"\
     " that i had realized my mistake she cooled down and"\
     " then told me in a very kind manner how disheartening"\
     " it was when she found any student not paying attention"\
     " i was genuinely sorry and promised to myself never to commit"\
     " such a mistake again."\

cpm_label=Label(text="Corrected CPM=?")
cpm_label.grid(row=0,column=0)
wpm_label=Label(text="Corrected WPM=?")
wpm_label.grid(row=1,column=0)
timeleft_label=Label(text="Time Left=60")
timeleft_label.grid(row=2,column=0)
restart_button=Button(text="Restart",command=restart).grid(row=3,column=0)
typing_text=Text(win,width=60,height=10,padx=10,pady=10,font=('Arial 15'))
typing_text.grid(row=4,column=0)
typing_text.insert(END,quote)
user_input=Text(win,width=60,height=10,padx=10,pady=10,font=('Arial 15'))
user_input.grid(row=5,column=0)
timer(60)





win.mainloop()
