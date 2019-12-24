import pyjadx
import argparse
import threading
from multiprocessing import Process
from threading import Thread
import time

def load_apk(apk, i):
    print(apk, i)
    jadx = pyjadx.Jadx()
    jadx.load(args.apk)
    #time.sleep(10)

def test_threads(apk):
    th = []
    for i in range(3):
        process = Thread(target=load_apk, args=[apk, i])
        process.start()
        th.append(process)
    for t in th:
        t.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load an APK with Pyjadx")
    parser.add_argument("apk", help="Target apk")

    args = parser.parse_args()
    test_threads(args.apk)

