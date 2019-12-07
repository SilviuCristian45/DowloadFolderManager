import glob
import os
import shutil

main_path = r"C:\Users\Silviu\Downloads/"

document_folder = input("Give the path of the folder you want to place your documents : ")
setups_folder = input("Give the path of the folder you want to place your setup files : ")
images_folder = input("Give the path of the folder you want to place your images : ")
music_folder = input("Give the path of the folder you want to place your music : ")
movie_folder = input("Give the path of the folder you want to place your movies : ")
archives_folder = input("Give the path of the folder you want to place your archives : ")

def move_files(): 
        for file_name in os.listdir(r"C:\Users\Silviu\Downloads"):
                if str(file_name).endswith("pdf") or str(file_name).endswith("docx") or str(file_name).endswith("doc"):
                        shutil.move(main_path + file_name, document_folder)
                if str(file_name).endswith("exe") or str(file_name).endswith("msi"):
                        shutil.move(main_path + file_name, setups_folder)
                if str(file_name).endswith("jpg") or str(file_name).endswith("png"):
                        shutil.move(main_path + file_name, images_folder)
                if str(file_name).endswith("mp3") or str(file_name).endswith("wav"):
                        shutil.move(main_path + file_name, music_folder)
                if str(file_name).endswith("mp4") or str(file_name).endswith("avi"):
                        shutil.move(main_path + file_name, movies_folder)
                if str(file_name).endswith("rar") or str(file_name).endswith("zip"):
                        shutil.move(main_path + file_name, archives_folder)

try:
        move_files()
        print("Done")
except expression as identifier:
        print("An error has occured . Try again .")


