from tkinter import filedialog
from tkinter.filedialog import askdirectory
import tkinter as tk
import os
import shutil
import hashlib
import mimetypes
from PIL import Image
import webbrowser

def create_file():
    frame.pack_forget()

    textbox = tk.Text(wn,width=20,height=10,font=('Comic sans',20))
    textbox.pack()

    


    def save():
        text = textbox.get('0.0',tk.END)
        file_saving = filedialog.asksaveasfile(defaultextension='.txt',
                                        filetypes= [('Text file', '*.txt'),
                                                    ('HTML file,','*.html'),
                                                    ('Word file','*.docx'),
                                                    ('XML file','*.xml'),
                                                    ('ODT file','*.odt'),
                                                    ('DOC file','*.doc'),
                                                    ('All files','*.*')],
                                        initialdir='/Users/uptri/Desktop/test',
                                        mode='w',
                                        title= 'Save as ' )
        file_saving.write(text)
        

    button_save = tk.Button(wn,text='Save as',command = save,font=('Comic sans',20))
    button_save.place(x=0,y=0)


def read_file():
    path = filedialog.askopenfilename(title='select af folder',filetypes=[('Text file','*.txt'),('All files','*.*')])
    if path:
        with open(path,'r') as file:
            fileText = file.read()
            textbox1 = tk.Text(wn,width=40,height=20)
            textbox1.pack()

            textbox1.insert(tk.END,fileText)

def remove_file():
    # using the os module
    path = filedialog.askopenfilename(title='Select a file')
    os.remove(path)
    print(f'{path} has been removed.')

def remove_dir():
    path = filedialog.askdirectory(title='Select a folder')
    shutil.rmtree(path)
    print(f'{path} has been removed.')

def add_file_to_dir():
    folder_path = filedialog.askdirectory(title=('select a directory to move the file to'))
    file_path = filedialog.askopenfilename(title='Select a file')
    filename = os.path.basename(file_path)
    destination_path = os.path.join(folder_path,filename)
    shutil.move(file_path,destination_path)

def make_directory_and_subfolder():
    def make():
        folder = os.path.join(entry1.get(),entry2.get())
        os.makedirs(folder,exist_ok=True)
        print(f'{entry2.get()} folder has been created in {entry1.get()}')

    
    entry1 = tk.Entry(width=40,font=('Arial',20))
    entry1.pack()
    entry2 = tk.Entry(width=40,font=('Arial',20))
    entry2.pack()
    entry1.insert(True,'Path to Folder')
    entry2.insert(True,'Name of Folder')
    submit_but1 = tk.Button(wn,text='Submit',font=('Consolas',20),command=make)
    submit_but1.pack()

def actions():
    def deleteDuplicate_files():
        duplicatefiles = 0
        path = filedialog.askdirectory()
        walker = os.walk(path)
        uniqueFiles = {}
        for folders,subfolders,files in walker:
            for file in files:
                 filepath = os.path.join(folders,file)
                 filehash = hashlib.md5((open(filepath, 'rb')).read()).hexdigest()
                 if filehash in uniqueFiles:
                     os.remove(filepath)
                     print(f'{filepath} has been removed.')
                 else:
                     uniqueFiles[filehash] = path

    def sortThem():
        path = filedialog.askdirectory()
        
        png_dir = os.path.join(path,'png files')
        jpg_dir = os.path.join(path,'jpg files')
        other = os.path.join(path,'other files')
        pythondir = os.path.join(path,'python files')
        jpeg = os.path.join(path,'jpeg files')
        exedir = os.path.join(path,'exe files')
        zipdir = os.path.join(path,'zip files')
        avifdir = os.path.join(path,'avif files')
        txtdir = os.path.join(path,'txt files')
        htmldir = os.path.join(path, 'HTML files')
        
        os.mkdir(png_dir)
        os.mkdir(jpg_dir)
        os.mkdir(other)
        os.mkdir(pythondir)
        os.mkdir(jpeg)
        os.mkdir(exedir)
        os.mkdir(zipdir)
        os.mkdir(avifdir)
        os.mkdir(txtdir)
        os.mkdir(htmldir)
        
        for folder,subfolder,files in os.walk(path):
            for file in files:
                ImgPath = os.path.abspath(os.path.join(path,file))
                i,extension = os.path.splitext(ImgPath)
                lowerExtension = extension.lower()

                if lowerExtension == '.png':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(png_dir,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.jpg':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(jpg_dir,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.jpeg':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(jpeg,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.py':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(pythondir,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.exe':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(exedir,file)
                    shutil.move(ImgPath,destination_path)


                elif lowerExtension == '.zip':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(zipdir,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.avif':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(avifdir,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.html':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(htmldir,file)
                    shutil.move(ImgPath,destination_path)

                elif lowerExtension == '.txt':
                    # shutil.move('what',''where')
                    # shutil.copy('what',''where') # Duplicate
                    destination_path = os.path.join(txtdir,file)
                    shutil.move(ImgPath,destination_path)

                else:
                    destination_path = os.path.join(other,file)
                    shutil.move(ImgPath,destination_path)

    def renameDir():

        def submit():
            nameofcurrentdir = os.path.dirname(path)
            newname = entry12.get()
            finalname = os.path.join(nameofcurrentdir,newname)
            os.rename(path,finalname)


        path = askdirectory()
        entry12 = tk.Entry(width=40,font=('Arial',20))
        entry12.pack()
        entry12.insert(True,'# New name of directory')
        subbut = tk.Button(wn,text='SUBMIT',font=('Consolas',20),command=submit)
        subbut.pack()

    def renameFile():
        def submit():
            nameofcurrentfile = os.path.dirname(path)
            newname = entry12.get()
            finalname = os.path.join(nameofcurrentfile,newname)
            os.rename(path,finalname)


        path = filedialog.askopenfilename()
        entry12 = tk.Entry(width=40,font=('Arial',20))
        entry12.pack()
        entry12.insert(True,'# New name of file')
        subbut = tk.Button(wn,text='SUBMIT',font=('Consolas',20),command=submit)
        subbut.pack()

    frame.pack_forget()
    deleteDuplicatesfiles_but = tk.Button(wn,text='Delete duplicate files',font=('Consolas',20),command=deleteDuplicate_files)
    deleteDuplicatesfiles_but.pack()
    sortingbut = tk.Button(wn,text='sort images in a folder',font=('Consolas',20),command=sortThem)
    sortingbut.pack()
    renamebut = tk.Button(wn,text='rename folder',font=('Consolas',20),command=renameDir)
    renamebut.pack()
    renamebut1 = tk.Button(wn,text='rename file',font=('Consolas',20),command=renameFile)
    renamebut1.pack()

    


def move_file():
    filepath = filedialog.askopenfilename(title='select a file')
    folderpath = filedialog.askdirectory(title='select a file')
    destination_path = os.path.join(filepath,folderpath)
    print(destination_path)
    shutil.move(filepath,destination_path)
    print(f'{filepath} has been moved to directory {destination_path}')

def move_dir():
    folderpath = filedialog.askdirectory(title='select a folder to be moved')
    newFolderpath = filedialog.askdirectory(title='Select the destination folder')
    destination_path = os.path.join(folderpath,newFolderpath)
    shutil.move(folderpath,destination_path)    

def getpath():

    def dirpath():
        path = askdirectory()
        label = tk.Label(f2,text=path,font=15)
        label.grid(columnspan=1)

    def filepath():
        path = filedialog.askopenfilename()
        label = tk.Label(f2,text=path,font=15)
        label.grid(columnspan=1)

    frame.pack_forget()
    f2 = tk.Frame(wn)
    f2.pack()
    buttondir = tk.Button(f2,text='get dir path',font=('Arial',20),command=dirpath)     
    buttondir.grid(row=0,column=0)
    buttonfile = tk.Button(f2,text='get file path',font=('Arial',20),command=filepath)     
    buttonfile.grid(row=0,column=1)

    



wn = tk.Tk()

frame = tk.Frame(wn)
frame.pack()


create_file_button = tk.Button(frame,text='create file',font=('Consolas',20),command=create_file)
create_file_button.grid(row=0,column=0)

read_file_button = tk.Button(frame,text='read file',font=('Consolas',20),command=read_file)
read_file_button.grid(row=0,column=1)

remove_dir_but = tk.Button(frame,text='remove directory',font=('Consolas',20),command=remove_dir)
remove_dir_but.grid(row=0,column=2)

remove_file_button = tk.Button(frame,text='remove file',font=('Consolas',20),command=remove_file)
remove_file_button.grid(row=1,column=0)

add_file_to_dir_button = tk.Button(frame,text='add file to directory',font=('Consolas',20),command=add_file_to_dir)
add_file_to_dir_button.grid(row=1,column=1)

make_directory_and_subfolderbutton = tk.Button(frame,text='make directory',font=('Consolas',20),command=make_directory_and_subfolder)
make_directory_and_subfolderbutton.grid(row=1,column=2)

movefile = tk.Button(frame,text='move file',font=('Consolas',20),command=move_file)
movefile.grid(row=2,column=0)

movedir = tk.Button(frame,text='move directory',font=('Consolas',20),command=move_dir)
movedir.grid(row=2,column=1)

getpath = tk.Button(frame,text='get path',font=('Consolas',20),command=getpath)
getpath.grid(row=2,column=2)

actonbut = tk.Button(frame,text='More',font=('Consolas',25),command=actions)
actonbut.grid(columnspan=3)



wn.mainloop()