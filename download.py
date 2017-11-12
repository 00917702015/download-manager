import requests
import os
import time
def download():
        CHUNK_SIZE = 8192
        bytes_read = 0
        checkdir()
        url = input("Enter the download link ")
        r = requests.get(url,allow_redirects=True,stream=True)
        filename = os.path.basename(url)
        url = r.url
        total_bytes =len(r.content)
        file_name,extension=os.path.splitext(filename)
        path = setpath(extension,filename)
        if os.path.exists(path):
                print("File already exists")
        else:
                with open(path,"ab") as file:
                        itr_count = 1
                        for chunk in r.iter_content(CHUNK_SIZE):
                                itr_count = itr_count+1
                                file.write(chunk)
                                bytes_read += len(chunk)
                                progress = 100* float(bytes_read)/float(total_bytes)
                                print("progress: %d"% (progress))

                r.close()
def setpath(extension,file_name):
        if extension == ".png" or extension == ".jpg" or extension == ".bmp" or extension == ".gif":
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Images",file_name)
                return path
        elif extension == ".zip" or extension == ".rar" or extension == ".7z":
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Compressed",file_name)
                return path
        elif extension == ".mp4" or extension == ".webm" or extension == ".avi" or extension == ".mkv" or extension == ".flv":
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Videos",file_name)
                return path
        elif extension == ".doc" or extension ==".docx" or extension == ".pdf" or extension == ".epub" or extension == ".djvu" or extension == ".txt" or extension == ".log" or extension == ".ini":
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Documents",file_name)
                return path
        elif extension == ".mp3" or extension == ".wav" or extension == ".aac" or extension == ".flac":
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Music",file_name)
                return path
        elif extension == ".exe":
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Programs",file_name)
                return path
        else:
                path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Others",file_name)
                return path
def checkdir():
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Programs")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Programs"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Images")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Images"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Music")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Music"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Compressed")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Compressed"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Others")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Others"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Videos")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Videos"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Documents")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Documents"))

download()
