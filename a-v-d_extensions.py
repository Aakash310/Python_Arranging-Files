import os , shutil

dict_extensions = {
'picture_extensions' : ('.PNG','.jpeg'),
'video_extensions' : ('.mp4','.mkv','.flv','.MKV','.mpeg'),
'document_extensions' : ('.docx','.pdf'),
}

folderpath = input("Enter the File Path")

def file_finder(folderpath, file_extensions):
    files = []
    for file in os.listdir(folderpath):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

#print(file_finder(folderpath,picture_extensions))       
for extension_name,extension_tuple in dict_extensions.items():
    folder_name = extension_name.split('_')[0] + ' Files'
    Folder_path = os.path.join(folderpath,folder_name)
    os.mkdir(Folder_path)
    for item in (file_finder(folderpath,extension_tuple)):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(Folder_path,item)
        shutil.move(item_path,item_new_path)
    #print(file_finder(folderpath , extension_tuple))         