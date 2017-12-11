import requests
import os
import time
import argparse
def download(url):
        CHUNK_SIZE = 8192
        bytes_read = 0
        checkdir()
        #url = input("Enter the download link: ")
        r = requests.get(url,allow_redirects=True,stream=True)
        filename = os.path.basename(url)
        path,r = setpath(r,filename,url)
        url = r.url
        total_bytes = len(r.content)
        print(total_bytes)
        with open(path,"ab") as file:
                for chunk in r.iter_content(CHUNK_SIZE):
                        file.write(chunk)
                        bytes_read += len(chunk)
                        progress = 100* float(bytes_read)/float(total_bytes)
                        #print("progress: %d"% (progress),end="")
        r.close()
def setpath(r,filename,url):
        file_name,extension = os.path.splitext(filename)
        extension = extension.split("?")[0]
        extension = extension[1:]
        file_name = file_name[:100].split("?")[0]
        content_type = r.headers['content-type']
        file_type,file_extension=content_type.split("/")
        file_type = file_type.title()
        if content_type == "application/octet-stream" or not content_type :
                file_extension = extension
                file_type = "Others"
        if file_extension[0] == "x":
                file_type = file_extension.split("-")[2].title()
                file_extension = file_extension.split("-")[1]
        if file_type == "Program" :
                file_type = "Application"
                file_extension = extension
        file_extension = "." + file_extension
        file_name = file_name + file_extension
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),file_type,file_name)
        if os.path.exists(path):
                resume_check,r = resume_download(r,path,url)
                if resume_check == False:
                        initial_path = path
                        file_count = 1;
                        while os.path.exists(path) == True:
                                path = initial_path
                                file_name,extension = os.path.splitext(path)
                                path=file_name + "(" + str(file_count) + ")" + extension
                                file_count = file_count + 1
        return (path,r)

def checkdir():
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Application")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Application"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Image")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Image"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Audio")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Audio"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Compressed")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Compressed"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Others")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Others"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Video")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Video"))
        if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Text")) == False:
                os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Text"))

def resume_download(r,path,url):
        statinfo = os.stat(path)
        resume_pos = statinfo.st_size
        if resume_pos < len(r.content):
                print("Resuming download...")
                resume_header = { 'Range' : 'bytes=%d-' % resume_pos}
                r=requests.get(url,headers = resume_header, allow_redirects = True, stream = True)
                return (True,r)
        else:
                print("File already downloaded, downloading again..")
                return (False,r)

def main():
        parser = argparse.ArgumentParser("BLAH BLAH")
        parser.add_argument('url',help="URL of the file to download",type=str)
        args = parser.parse_args()
        download(args.url)

if __name__ == '__main__':
    main()
