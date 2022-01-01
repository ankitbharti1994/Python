import os
import shutil
import zipfile

print(os.getcwd())
os.chdir(os.path.expanduser("~/Desktop"))
print(os.getcwd())
os.mkdir("Payload")
print(os.getcwd())
shutil.copyfile("netflix.png", "Payload/netflix.png")

# shutil.make_archive("AppleEasyPay", "zip", "Payload")
with zipfile.ZipFile("AppleEasyPay.zip", 'w', zipfile.ZIP_DEFLATED) as obj:
    obj.write("Payload/")
