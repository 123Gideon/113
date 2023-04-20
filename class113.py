from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
from_dir=r"C:\Users\17034\Downloads"
class FileEventHandler(FileSystemEventHandler):

    def on_createds(self,event):
        print(f"hey, {event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"opps! someone deleted {event.src_path}!")    

    def on_modified(self,event):
        print(f"hey there, {event.src_path} has been modified")

    def on_moved(self,event):
        print(f"someone moved {event.src_path} to{event.dest_path}")   
myevents=FileEventHandler()
myobserver=Observer()
myobserver.schedule(myevents,path=from_dir,recursive=True)
try:
    while True:
         time.sleep(2)
         print("running")

except KeyboardInterrupt:
    print("stopped")
    myobserver.stop()