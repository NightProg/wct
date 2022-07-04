import os, time


def explorer(target: str, username):
    target_path = []
    visited_path = []
    starting_path = os.getcwd()
    current_folder = os.getcwd()

    while True:

        print(f"\n[BEFORE ENTERING, HERE ARE THE CURRENT FOLDER] : {current_folder}")
        for item in os.listdir(current_folder):
            
            print(f"[ITEM] : {item}")

            if os.path.isdir(''.join((os.getcwd(), "/", item))):
                print(f"[is folder] : {''.join((os.getcwd(), '/', item))}")
                ending = "/"
            elif os.path.isfile(''.join((os.getcwd(), "/", item))):
                print(f"[is file] : {''.join((os.getcwd(), '/', item))}")
                ending = ""
            else:
                print("[Error]")

            if os.getcwd() == '/':
                item_path = ''.join((os.getcwd(), item, ending))
            else:
                item_path = ''.join((os.getcwd()+"/", item, ending))


            # DEBUG: item_path + current_folder
            print(f"[ITEM PATH] : {item_path}")
            print(f"[CURRENT PATH] : {os.getcwd()}")


            # The target is part of the item and has not yet been found
            if target in item and item_path not in target_path:
                target_path.append(item_path)

                # DEBUG: Target Path
                print(f"[TARGET PATH] : {len(target_path)} ->")
                for i in target_path:
                    print(f"    > {i}")
           
            if item_path not in visited_path:
                visited_path.append(item_path)

                # DEBUG: Visited Path
                print(f"[VISITED PATH] : {len(visited_path)} ->")
                for i in visited_path:
                    print(f"    > {i}")
                print("\n")

                if os.path.isdir(item_path):
                    os.chdir(item_path)
                    current_folder = item_path
                    print("^ [ENTRY...]\n")
                    continue

            if os.listdir(os.getcwd())[-1] == item and item_path in visited_path:
               os.chdir("../")
               current_folder = os.getcwd()
               continue

            time.sleep(0.1)
