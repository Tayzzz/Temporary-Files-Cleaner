try:
    import ctypes
    import shutil
    import colorama
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()

import os
from colorama import Fore, init

init(convert=True)


def main():

    ctypes.windll.kernel32.SetConsoleTitleW(
        "Temporary Files Cleaner | v0.1 | By Tayz")

    folders = [os.environ.get('TEMP').replace("\\", "/"),
               os.environ.get("USERPROFILE").replace("\\", "/") + "/Downloads"]

    deleteFileCount = 0
    deleteFolderCount = 0

    for folder in folders:

        choice = input(
            f"Do you want clear files and folders in {folder} (y/n) ? ")

        if str(choice) == "yes" or str(choice) == "y":

            if not os.listdir(folder):
                print(f'{Fore.RED}No folders/files{Fore.RESET}\n')
            else:
                for the_file in os.listdir(folder):
                    file_path = os.path.join(folder, the_file)
                    indexNo = file_path.find('\\')
                    itemName = file_path[indexNo+1:]
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                            print(
                                f'{Fore.GREEN}File deleted{Fore.RESET} {itemName}')
                            deleteFileCount += 1

                        elif os.path.isdir(file_path):
                            if file_path.__contains__('chocolatey'):
                                continue
                            shutil.rmtree(file_path)
                            print(
                                f'{Fore.GREEN}Folder deleted{Fore.RESET} {itemName}')
                            deleteFolderCount += 1

                    except Exception as e:
                        print(f'{Fore.RED}Access Denied{Fore.RESET} {itemName}')

                print()
        else:
            print()

    input(str(deleteFileCount) + ' files and ' +
          str(deleteFolderCount) + ' folders deleted. Press enter to exit')


if __name__ == "__main__":
    main()
