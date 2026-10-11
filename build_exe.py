import PyInstaller.__main__
import customtkinter
import os

customtkinter_yolu = os.path.dirname(customtkinter.__file__)

PyInstaller.__main__.run([
    'main.py', 
    '--name=KolayCeviriAsistani',
    '--windowed',
    '--noconfirm',
    f'--add-data={customtkinter_yolu};customtkinter/',
    '--hidden-import=faster_whisper',
    '--hidden-import=ctranslate2',
    '--hidden-import=tokenizers'
])