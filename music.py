def unmutemusic():
    global currentvol
    root.UnmuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)
    
def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing...')
    
def volumeup():
    vol = mixer.music.get_volume()
    #if(vol>=vol*100):
        #mixer.music.set_volume(vol+0.1)
    #else:
    mixer.music.set_volume(vol+0.05)
    ProgressbarvolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    Progressbarvolume['value'] = mixer.music.get_volume()*100
    
def volumedown():
      vol = mixer.music.get_volume()
      #if(vol<=vol*100):
        #mixer.music.set_volume(vol-0.01)
      #else:
      mixer.music.set_volume(vol-0.05)
      ProgressbarvolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
      Progressbarvolume['value'] = mixer.music.get_volume()*100
      #vol = mixer.music.get_volume()
      #mixer.music.set_volume(vol-0.1)
    
def stopmusic():
    mixer.music.stop()
    ProgressbarMusicLabel.grid_remove()
    ProgressbarLabel.grid_remove()
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid_remove()
    
    #ProgressbarLabel.grid()
    #ProgressbarMusicStartTimeLabel.configure(text='0:00:0')
    AudioStatusLabel.configure(text='Stoped...')
    #ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=))))
    #ProgressbarMusicStartTimeLabel.configure(text='0:00:0')
def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused...')

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.MuteButton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    Progressbarvolume['value'] = 40
    ProgressbarvolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing...')
    
    song = MP3(ad)
    totalsonglength = int(song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength

    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))

    def Progresbarmusictick():
        CurrentsongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrentsongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentsongLength))))
        ProgressbarMusic.after(2,Progresbarmusictick)
    Progresbarmusictick()
    
    
def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='F:/music/New folder',
                                        title='Select Audio File',
                                        filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',
                                        filetype=(('MP3','*.mp3'),('WAV','*.wav')))
                                        
    audiotrack.set(dd)


def createwidthes():
    global implay,impause,imbrowse,imvolumeup,imvolumedown,imstop,imresume,immute,imunmute
    global AudioStatusLabel,ProgressbarvolumeLabel,Progressbarvolume,ProgressbarLabel
    global ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel
    ##################################################################################################################################Images Register
    implay=PhotoImage(file='Play.png')
    impause=PhotoImage(file='Pause.png')
    imbrowse=PhotoImage(file='Browsing.png')
    imvolumeup=PhotoImage(file='VolumeUp.png')
    imvolumedown=PhotoImage(file='VolumeDown.png')
    imstop=PhotoImage(file='Stop.png')
    imresume=PhotoImage(file='Resume.png')
    immute=PhotoImage(file='Mute.png')
    imunmute=PhotoImage(file='Unmute.png')
    
    ###################################################################################################################################change size of image
    implay = implay.subsample(20,20)
    impause = impause.subsample(20,20)
    imbrowse = imbrowse.subsample(20,20)
    imvolumeup = imvolumeup.subsample(20,20)
    imvolumedown = imvolumedown.subsample(20,20)
    imstop = imstop.subsample(20,20)
    imresume = imresume.subsample(20,20)
    immute = immute.subsample(20,20)
    imunmute = imunmute.subsample(20,20)
    
   ########################################################################################## ########################################LABELS
    TrackLabel = Label(root,text='select Audio Track :',background='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root,text='',background='lightskyblue',font=('arial',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)
    
    ###################################################################################################################################Entry Box
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    
    ##################################################################################################################################### Buttons
    BrowseButton = Button(root,text='search',bg='deeppink',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                          image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text='Play',bg='green2',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                          image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)


    root.PauseButton = Button(root,text='Pause',bg='yellow',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                          image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                          image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.MuteButton = Button(root,text='Mute',width=100,bg='yellow',activebackground='purple4',bd=5,image=immute,compound=RIGHT,command=mutemusic)
    root.MuteButton.grid(row=3,column=3)
    root.MuteButton.grid_remove()

    root.UnmuteButton = Button(root,text='Unmute',width=100,bg='yellow',activebackground='purple4',bd=5,image=imunmute,compound=RIGHT,command=unmutemusic)
    root.UnmuteButton.grid(row=3,column=3)
    root.UnmuteButton.grid_remove()


    VolumeUpButton = Button(root,text='VolumeUp',bg='blue',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                          image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)


    StopButton = Button(root,text='Stop',bg='red',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                          image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)


    VolumeDownButton = Button(root,text='VolumeDown',bg='blue',font=('arial',16,'italic bold'),width=200,bd=5,activebackground='purple4',
                              image=imvolumedown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

####################################################################################################################################Progressbar Volume
    ProgressbarLabel=Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    Progressbarvolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
    Progressbarvolume.grid(row=0,column=0,ipadx=5)

    ProgressbarvolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarvolumeLabel.grid(row=0,column=0)

########################################################################################################################################Progressbar Music
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)
    
##################################################################
#import tkinter as tk  
from tkinter import*
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root=Tk()
root.geometry('1100x500+200+50')
root.title('MUSIC PLAYER')
root.iconbitmap(r'E:\project\music.ico')
root.resizable(False,False)
root.configure(bg = 'lightskyblue')
########################################################################################################################################Global Variable
audiotrack = StringVar()
currentvol = 0
totalsonglength = 0
count = 0
text = ''
sk = 0

######################################################################################################################################## Create Slider
mk = 'Developed By Mritunjay & Surya'
SliderLabel = Label(root,text= mk,bg='lightskyblue',font=('arial',40,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabeltick():
    global count,text
    if(count>=len(mk)):
        count=-1
        text=''
        SliderLabel.configure(text=text)
    else:
        text=text+mk[count]
        SliderLabel.configure(text=text)
    count +=1
    SliderLabel.after(200,IntroLabeltick)

    
IntroLabeltick()
mixer.init()
createwidthes()
root.mainloop()
