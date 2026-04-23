import tkinter as tk
from datetime import datetime
import time
import threading
import pygame

# Initialize sound
pygame.mixer.init()

alarms = []

def play_sound():
    pygame.mixer.music.load("alarm.mp3")  # put your MP3 file in same folder
    pygame.mixer.music.play()

def check_alarms():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        
        for alarm in alarms:
            if alarm["time"] == current_time and not alarm["triggered"]:
                alarm["triggered"] = True
                play_sound()
                print("⏰ Alarm ringing:", alarm["time"])
        
        time.sleep(1)

def add_alarm():
    alarm_time = entry.get()
    alarms.append({"time": alarm_time, "triggered": False})
    listbox.insert(tk.END, alarm_time)
    entry.delete(0, tk.END)

def stop_alarm():
    pygame.mixer.music.stop()

# GUI setup
root = tk.Tk()
root.title("Alarm Clock")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Alarm", command=add_alarm)
add_button.pack()

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_button.pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Start background thread
threading.Thread(target=check_alarms, daemon=True).start()

root.mainloop()