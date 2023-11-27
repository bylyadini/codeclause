from tkinter import *
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title("Music App")
root.geometry("640x360")
root.iconbitmap("icon.ico")

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]  # Fixed typo, changed 'song' to 'songs'

def play_music():
    global current_song, paused

    if not paused:
        file_path = os.path.join(root.directory, current_song)
        normalized_path = os.path.normpath(file_path)
        pygame.mixer.music.load(normalized_path)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
        
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True

def next_music():
    global current_song , paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
        
def previous_music():
    global current_song , paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

    
    

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

organise_menu = Menu(menubar,tearoff=False)
organise_menu.add_command(label="Select Folder",command=load_music)
menubar.add_cascade(label="Organise",menu=organise_menu)

songlist = Listbox(root,bg="black",fg="white",width=100,height=18)
songlist.pack()

play_button_img = PhotoImage(file="play.png")
pause_button_img = PhotoImage(file="pause.png")
next_button_img = PhotoImage(file="next.png")
prev_button_img = PhotoImage(file="previous.png")

controls_frame = Frame(root)
controls_frame.pack()

play_btn = Button(controls_frame,image=play_button_img,borderwidth=0,command=play_music)
pause_btn = Button(controls_frame,image=pause_button_img,borderwidth=0,command=pause_music)
next_btn = Button(controls_frame,image=next_button_img,borderwidth=0,command=next_music)
previous_btn = Button(controls_frame,image=prev_button_img,borderwidth=0,command=previous_music)

play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
next_btn.grid(row=0,column=3,padx=7,pady=10)
previous_btn.grid(row=0,column=0,padx=7,pady=10)

root.mainloop()
