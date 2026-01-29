from pathlib import Path
import os 
def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1}: {item}")
    


def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name:")
        p  = Path(name)
        if not p.exists() :
            with open(p,'w')  as f:
                data = input("what do you want to write in this file:")
                f.write(data)
            print('file created succesfully')
        else:
            print("this file already exist")    
    except Exception as err:
        print(f"An error occured as {err}")    
        
def readfile():
    try:
        readfileandfolder()
        name  = input("which file you want to read:")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as f :
                data = f.read()
                print(data)
            print("readed successfully ")
        else:
            print("the file does not exists")
    except Exception as err:
        print(f"An error occured as {err}")   
def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to update:")
        p = Path(name)
        if p.exists and p.is_file():
            print("press 1 for changing the name of your file:")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content  in your life ")
            
            response = int(input("tell your response:"))
            if response == 1 :
                name2 = input("enter your  new file name :")
                p2 = Path(name2)
                p.rename(p2)
            if response == 2   :
                with open (p,'w') as f :
                    data = input("what  do you want to  overwrite the data:")
                    f.write(data)
            if response == 3 :
                with open (p,'a') as f :
                    data = input("what  do you want to  append the data:")
                    f.write(" "+data)                        
    except Exception as err :
        print(f"An error occured as {err}")                
def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete:")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file deleted sucessfully")
        else :
            print("no such file exist")    
    except Exception as err:
        print(f"an error occures as {err}")              
    

print("print 1 for creating a file")
print("print 2 for reading a file")
print("print 3 for uodating a file")
print("print 4 for delection a file")

check = int(input('enter your response(1\2\3\4):'))
if check == 1 :
    createfile()
if check == 2 :
    readfile()    
if check == 3 :
    updatefile()    
if check == 4:
    deletefile()    
    