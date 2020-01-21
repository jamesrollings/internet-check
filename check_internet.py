import subprocess
import win10toast
import time

IP = '8.8.8.8'
def checkInternet():
    PING = subprocess.Popen('ping ' + IP, stdout=subprocess.PIPE)
    PING.wait()

    if PING.poll() != 0:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast('Internet Check', 'Internet is down', duration=10)


while True:
    time.sleep(10)
    checkInternet()