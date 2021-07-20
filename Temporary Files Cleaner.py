import os
import shutil
from colorama import Fore, init

init(convert=True)


def main():
    folders = [os.environ.get('TEMP').replace("\\", "/"),
               os.environ.get('TMP').replace("\\", "/"),
               os.environ.get("USERPROFILE").replace("\\", "/") + "/downloads"]

    deleteFileCount = 0
    deleteFolderCount = 0

    for folder in folders:
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            indexNo = file_path.find('\\')
            itemName = file_path[indexNo+1:]
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f'{Fore.GREEN}File deleted{Fore.RESET} {itemName}')
                    deleteFileCount += 1

                elif os.path.isdir(file_path):
                    if file_path.__contains__('chocolatey'):
                        continue
                    shutil.rmtree(file_path)
                    print(f'{Fore.GREEN}Folder deleted{Fore.RESET} {itemName}')
                    deleteFolderCount += 1

            except Exception as e:
                print(f'{Fore.RED}Access Denied{Fore.RESET} {itemName}')

    input("\n"+str(deleteFileCount) + ' files and ' +
          str(deleteFolderCount) + ' folders deleted. Press enter to exit')


if __name__ == "__main__":
    main()
