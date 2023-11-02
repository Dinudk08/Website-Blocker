from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("WEBSITE BLOCKER")
Label(root,text ='website blocker',font ='arial 20 bold').pack()
Host_path='C:\Windows\System32\drivers\etc\hosts'
IP_address='127.0.0.1'
Label(root,text='Enter Website :' , font='arial 13 bold').place(x=5 ,y=60)
Websites=Text(root,font='arial 10',height='2' ,width='40').place(x=140,y=50)


def Blocker():
    website_lists = Websites.get(1.0,END)
    website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in website:
            if website in file_content:
                Label(root,text='Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(IP_address + "" + website + '\n')
                Label(root,text = "Blocked",font = 'arial 12 bold').place(x=230,y=200)
block=Button(root,text='block',font='arial 12 bold',pady=5,command=Blocker ,width='6',bg='royal blue',activebackground='sky blue')
block.place(x=230,y=150)
root.mainloop()
