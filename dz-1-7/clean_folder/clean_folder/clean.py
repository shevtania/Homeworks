import re
from pathlib import Path
import shutil
import sys

images = []
video =  []
audio = []
documents = []
archives = []

known_extentions = {
    'jpeg': images,
    'png': images,
    'jpg': images,
    'svg': images,
    'avi': video,
    'mp4': video,
    'mov': video,
    'mkv': video,
    'doc': documents,
    'docx': documents,
    'txt': documents,
    'pdf': documents,
    'xlsx': documents,
    'ppt': documents,
    'pptx': documents,
    'mp3': audio,
    'ogg': audio, 
    'wav': audio,
    'amr': audio,
    'zip': archives,
    'gz': archives,
    'tar': archives
}

folders = []
extensions = set()
unknown = set()
other = []
container = []

def scan_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            if el.name not in ('archives', 'audio', 'documents', 'images', 'video', 'other'):
                folders.append(el)
                scan_folder(el)
        else:
            ext = el.suffix  
            ext = ext[1:] # el - файл
            fullname = path / el.name
            if not ext:
                other.append(fullname)
            else:
                try:
                    container  = known_extentions[ext]
                    extensions.add(ext)
                    container.append(fullname) 
                except KeyError:
                    unknown.add(ext)
                    other.append(fullname)
    return




CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    trans_name = name.translate(TRANS)
    trans_name = re.sub(r'\W', '_', trans_name)
    return trans_name


def handle_media(filename: Path, output_folder: Path):
    output_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(output_folder / normalize(filename.name))
    return

def handle_other(filename: Path, output_folder: Path):
    output_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(output_folder / normalize(filename.name))
    return

def handle_archive(filename: Path, output_folder: Path):
    output_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = output_folder / normalize(filename.name.replace(filename.suffix, ''))


    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'this is not archive {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Folder delete error {folder}')
    return



def file_processing(folder: Path):

    for file in images:
        handle_media(file, folder / "images")

    for file in video:
        handle_media(file, folder / "video")

    for file in audio:
        handle_media(file, folder / "audio")

    for file in documents:
        handle_media(file, folder / "documents")



    for file in other:
        handle_other(file, folder / "other")

    for file in archives:
        handle_archive(file, folder / "archives")


     
    for folder in folders[::-1]:
        handle_folder(folder)



def input_dir():
    try:
        input_folder = sys.argv[1]
    except IndexError:
        print('Enter valid path to folder')
    else:
        folder_for_scan = Path(input_folder)
        print(f'Start in folder {folder_for_scan.resolve()}') #Make the path absolute, resolving any symlinks. 
        scan_folder(folder_for_scan.resolve())
        file_processing(folder_for_scan.resolve())
        print(f'Sorted file extentions {extensions}')
        print(f'Unknown file extentions {unknown}')
        print(f' Files of images: {images}')
        print(f'Audio files: {audio}')
        print(f'Video files: {video}')
        print(f'Documents: {documents}')
        print(f'List of archives: {archives}')



if __name__ == '__main__':

    input_dir()




