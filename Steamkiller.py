import psutil
def stopsteam():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == 'steam.exe':
            try:
                p = psutil.Process(process.info['pid'])
                p.terminate()
                print("steam.exe stopped")
            except psutil.NoSuchProcess:
                print("steam.exe not found")
            except psutil.AccessDenied:
                print("unable to stop steam.exe")

if __name__ == "__main__":
    stopsteam()
