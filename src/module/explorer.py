import os


def explorer(target: str):
    target_path = []
    visited_path = []
    startin_path = os.getcwd()

    while True:
        for item in os.listdir():
            # ending definition
            if os.path.isdir(''.join((os.getcwd(), item))):
                ending = "/"
            else:
                ending = ""

            item_path = ''.join((os.getcwd(), item, ending))
             
            if target in item and item_path not in target_path: 
                target_path.append(item_path)
            
            if os.path.isdir(item_path) and item_path not in visited_path:
                os.chdir(item_path)
                visited_path.append(os.getcwd())

            if item == os.listdir()[-1] and item_path in visited_path:
                os.chdir('../')
            
            if os.getcwd() == startin_path and item == os.listdir()[-1] and item_path in visited_path:
                return target_path
