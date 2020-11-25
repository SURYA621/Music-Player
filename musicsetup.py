from CX_Freeze import*
includefiles = ["music.ico",'Mute.png','Play.png','Pause.png','Browsing.png','VolumeUp.png','VolumeDown.png','Stop.png','Resume.png','Unmute.png']
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base="Win32GUI"
    
shortcut_table = [
    ("DesktopShortCut",# Shortcut
     "DesktopFolder", # Directory_
     "Music Player", #Name
     "TARGETDIR", #Component_
     "[TARGETDIR]\music.exe", # Target
     None, # Arguments
     None, # Description
     None, # Hotkey
     None, #Icon
     None, # IconIndex
     None, # ShowCmd
     "TARGETDIR", #WkDir
     )
]

msi_data = {"Shortcut":shortcut_table}

bdist_msi_options = {'data':msi_data}
setup(

    version="0.1",
    description="Simple Music Player Developed By Mritunjay & Surya",
    author="Pandey",
    name="Music Player",
    options={'build_exe':{'include_file':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="music.py",
            base=base,
            icon='music.ico',
        )
    ]
)
    
    
