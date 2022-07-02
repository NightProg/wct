import os


def explorer(target: str):
    target_path = []
    visited_path = []
    startin_path = os.getcwd()
    current_folder = os.getcwd()

    while True:
        print(os.listdir())
        print(startin_path)

        for item in os.listdir(current_folder):
            # ending definition
            if os.path.isdir(''.join((os.getcwd(), "/", item))):
                print("[is folder]")
                ending = "/"
            else:
                print("[is file]")
                ending = ""

            item_path = ''.join((os.getcwd(), item, ending))
            print(item_path)
 
            if os.getcwd() == startin_path and item == os.listdir()[-1] and item_path in visited_path:
                return target_path

            if item == os.listdir()[-1] and item_path in visited_path:
                print("exit..")
                os.chdir('../')
                current_folder = os.getcwd()

            if target in item and item_path not in target_path: 
                print("found!")
                print(item)
                target_path.append(item_path)
                print(target_path[-1])

            if os.path.isdir(item_path) and item_path not in visited_path:
                print("enter..")
                visited_path.append(item_path)
                current_folder = item_path
                continue

            if os.path.isdir(item_path) == False and item_path not in visited_path:
                visited_path.append(item_path)
