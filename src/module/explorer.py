import os


def explorer(target: str):
    target_path = []
    visited_path = []
    startin_path = os.getcwd()
    current_folder = os.getcwd()

    while True:

        for item in os.listdir(current_folder):
            print(f"\n[ITEM] : {item}")

            if os.path.isdir(''.join((os.getcwd(), "/", item))):
                print(f"[is folder] : {''.join((os.getcwd(), '/', item))}")
                ending = "/"
            elif os.path.isfile(''.join((os.getcwd(), "/", item))):
                print(f"[is file] : {''.join((os.getcwd(), '/', item))}")
                ending = ""
            else:
                print("[Error]")

            item_path = ''.join((os.getcwd()+"/", item, ending))

            # DEBUG: item_path + current_folder
            print(f"[ITEM PATH] : {item_path}")
            print(f"[CURRENT PATH] : {current_folder}")


            # DEBUG: Target Path
            print(f"[TARGET PATH] : {len(target_path)} ->")
            for i in target_path:
                print(f"    > {i}")
            
            # DEBUG: Visited Path
            print(f"[VISITED PATH] : {len(visited_path)} ->")
            for i in visited_path:
                print(f"    > {i}")
            print("\n")

            # The target is part of the item and has not yet been found
            if target in item and item_path not in target_path:
                target_path.append(item_path)
            
            if item_path not in visited_path:
                visited_path.append(item_path)

                if os.path.isdir(item_path):
                    current_folder = item_path
                    os.chdir(current_folder)
                    continue
