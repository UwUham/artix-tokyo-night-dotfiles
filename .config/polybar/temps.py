import subprocess
print(str(subprocess.check_output(['sensors'])).split("+")[1].split("Tctl")[0].split("\\")[0].split(".")[0])
