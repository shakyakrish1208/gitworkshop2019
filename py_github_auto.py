import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    print("Organising your files intro [ images - music - video -executable - archive - torrent - document - code - design files]")
    for filename in os.listdir(dir_path):
        
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")):
            
            if not os.path.exists("images"):
                os.makedirs("images")
            shutil.copy2(filename, "images")
            os.remove(filename)

        
        if filename.lower().endswith((".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw")):
            
            if not os.path.exists("music"):
                os.makedirs("music")
            shutil.copy2(filename, "music")
            os.remove(filename)

        
        if filename.lower().endswith((".webm", ".mp4")):
            
            if not os.path.exists("video"):
                os.makedirs("video")
            shutil.copy2(filename, "video")
            os.remove(filename)

        
        if filename.lower().endswith((".exe", ".msi", ".deb" , "dmg")):
            
            if not os.path.exists("executables"):
                os.makedirs("executables")
            shutil.copy2(filename, "executables")
            os.remove(filename)

        
        if filename.lower().endswith((".rar", ".tar" , ".zip" , ".gz")):
            
            if not os.path.exists("archives"):
                os.makedirs("archives")
            shutil.copy2(filename, "archives")
            os.remove(filename)


        
        if filename.lower().endswith((".torrent",)):
            
            if not os.path.exists("torrent"):
                os.makedirs("torrent")
            shutil.copy2(filename, "torrent")
            os.remove(filename)

        
        if filename.lower().endswith((".txt", ".pdf", ".docx" , "doc")):
            
            if not os.path.exists("documents"):
                os.makedirs("documents")
            shutil.copy2(filename, "documents")
            os.remove(filename)


        
        if filename.lower().endswith((".py", ".php", ".html" , ".css" , ".js")):
            
            if not os.path.exists("code"):
                os.makedirs("code")
            shutil.copy2(filename, "code")
            os.remove(filename)

        
        if filename.lower().endswith((".psd", ".ai")):
            
            if not os.path.exists("design-files"):
                os.makedirs("design-files")
            shutil.copy2(filename, "design-files")
            os.remove(filename)

except OSError:
    print("Error happened ...... try again")
finally:
    
    os.system("cls" if os.name == "nt" else "clear")
print("Finished organising your files")