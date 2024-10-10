# Toast
import os
def install(app, src):
    if src == "-w" or src == "-winget":
        os.system(f"winget install {app}")
    else:
        pass
app = input("Toast>> ")
install(app, "-w")
