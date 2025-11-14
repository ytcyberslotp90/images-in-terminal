import subprocess
import sys
import os
import time

def check_chafa():
    try:
        subprocess.run(["chafa", "--version"],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL,
                       check=True)
        return True
    except:
        return False


def install_chafa():
    print("[+] Installing chafa via winget...")
    os.system('powershell -c "winget install chafa --silent">nul 2>&1')
    time.sleep(2)  # PATH refresh delay



def display_image_with_chafa(image_path):
    if not os.path.exists(image_path):
        print(f"[X] Image not found: {image_path}")
        return

    subprocess.run(['chafa', '--format=sixel', image_path])


def run_all():
    if check_chafa():
        display_image_with_chafa(image_file)
    else:
        print("[!] Chafa missing. Installing...")
        install_chafa()

        # check again after install
        if check_chafa():
            print("[+] Chafa installed successfully.")
            display_image_with_chafa(image_file)
        else:
            exit()


# ------------------------------

image_file = 'image.jpg'
run_all()
os.system("pause")
