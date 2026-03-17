import domain.dictionary as dc
import threading
import time
import os

from domain.dictionary import Dictionary
from domain.spellcheck import Spellcheck

def scan_available_languages() -> set[str]:
    files = os.listdir(Dictionary.__DICT_BASE_PATH__)
    r = set(map(lambda x: x.replace(".txt", ""), files))
    return r

def main():
    print("Hello World")
    available_languages: set[str] = scan_available_languages()
    dictionaries: dict[str, Dictionary] = {}
    threads: list[threading.Thread] = []
    tic = time.time()

    # load all available dictionaries with different threads
    for language in available_languages:
        dictionary = dc.Dictionary(f"{language}.txt", language)
        print(f"Start loading {language}")
        dictionaries[language] = dictionary
        load_tread = threading.Thread(target = dictionary.load)
        threads.append(load_tread)
        load_tread.start()

    for t in threads:
        t.join()
        threads.remove(t)

    toc = time.time()
    print("Finished loading dictionaries")
    print("Elapsed time: ", toc - tic)

    for dictionary in dictionaries.values():
        print(dictionary)

    language = input("Scegliere una lingua: ")
    print()

    if language in available_languages:
        print(f"Verrà utilizzato il dizionario di {language}")
        print()
        txt = input("Inserire il testo da correggere: ")

        if txt.startswith("file:"):
            f_path = txt.replace("file:", "")
            f = open(f_path, "r", encoding="utf-8")
            txt = f.readlines()[0]

        results = Spellcheck(txt, dictionaries[language]).spellcheck()
        print(results)

if __name__ == "__main__":
    main()

