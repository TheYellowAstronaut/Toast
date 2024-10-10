# Toast
import os
def install(app, src):
    if src == "-w" or src == "-winget":
        os.startfile(f"winget install {app}")
    else:
        pass
