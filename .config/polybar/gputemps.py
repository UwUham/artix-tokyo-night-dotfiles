import subprocess
for i in str(subprocess.check_output(['nvidia-smi'])).split("   "):
    if "C" in i and ("1" in i or "2" in i or "3" in i or "4" in i or "5" in i or "6" in i or "7" in i or "8" in i or "9" in i) and "CUDA" not in i:
        print(i.split("C")[0])
