#Sistem ve İşlem Bilgilerine Erişim Sağlamak için Psutil'i Kütüphanesinin İndirilmesi
!pip install psutil

import os
import subprocess
import psutil
import datetime

# 1. En son kurulan ve kaldırılan programları listeleme
def get_installed_programs():
    installed_programs = []
    try:
        # Windows'ta kayıt defterinden programları alma
        key = r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        programs = subprocess.check_output(
            f'reg query "{key}" /s /v DisplayName', shell=True, text=True
        )
        for line in programs.splitlines():
            if "DisplayName" in line:
                installed_programs.append(line.split("    ")[-1].strip())
    except Exception as e:
        print(f"Hata: {e}")
    
    return installed_programs

# 2. Çalışan programları ve sürelerini listeleme
def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            create_time = datetime.datetime.fromtimestamp(proc.info['create_time'])
            elapsed_time = datetime.datetime.now() - create_time
            processes.append({
                'name': proc.info['name'],
                'pid': proc.info['pid'],
                'elapsed_time': str(elapsed_time).split('.')[0]  # sadece süreyi al
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    return processes

# 3. Açılan belgeler ve klasörleri listeleme
def get_open_files_and_folders():
    open_files = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            open_files.extend(proc.open_files())
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return open_files

# Programları çağırma
if __name__ == "__main__":
    print("En son kurulan programlar:\n")
    for program in get_installed_programs():
        print(program)

    print("\nÇalışan programlar ve süreleri:\n")
    for process in get_running_processes():
        print(f"Ad: {process['name']}, PID: {process['pid']}, Çalışma Süresi: {process['elapsed_time']}")

    print("\nAçılan dosyalar ve klasörler:\n")
    for file in get_open_files_and_folders():
        print(file.path)