import domain.dictionary as dc
import threading
import time
import os
import flet as ft
# file:inputs/test_spellcheck_italiano.txt

from domain.dictionary import Dictionary
from domain.spellcheck import Spellcheck
from ui.spellcheckcontroller import SpellcheckController
from ui.view import HomePage


# NEL CASO IN CUI DIA ERRORE ALLA PRIMA INSTALLAZIONE SUL PROGETTO, LANCIARE IL COMANDO "INSTALL CERTIFICATES.COMMAND" DALLA CARTELLA APPLICATIONS/PYTHON 3.10

def scan_available_languages() -> set[str]:
    files = os.listdir(Dictionary.__DICT_BASE_PATH__)
    r = set(map(lambda x: x.replace(".txt", ""), files))
    return r

def main():
    print("Hello World")
    available_languages: set[str] = scan_available_languages()
"""
    if language in available_languages:
        print(f"Verrà utilizzato il dizionario di {language}")
        print()
        txt = input("Inserire il testo da correggere (oppure file: per caricare un file): ")

        if txt.startswith("file:"):
            f_path = txt.replace("file:", "")
            print(f"Avvio correzione file {f_path}")
            f = open(f_path, "r", encoding="utf-8")
            txt = f.readlines()[0]

        results = Spellcheck(txt, dictionaries[language]).spellcheck_dicotomic()
        print(results)
        
    else:
        print(f"Unable to find dictionary for {language}, quitting")
"""
def main_flet(page: ft.Page):
    page.height = 1200
    page.views.append(HomePage(page))
    page.update()

if __name__ == "__main__":
    ft.run(main_flet)

