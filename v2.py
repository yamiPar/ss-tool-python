import pyautogui
import time
import tkinter as tk
import tkinter.filedialog as filedialog
import os

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        global selected_folder
        selected_folder = folder_path
        folder_label.config(text=f"Selected folder: {folder_path}")

def take_screenshot():
    if selected_folder:  # Correct indentation for the if statement
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{time.strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot.save(os.path.join(selected_folder, filename))
        screenshot_label.config(text=f"Screenshot saved to: {filename}")
    else:
        screenshot_label.config(text="Please select a folder first.")

root = tk.Tk()

# Label 
folder_label = tk.Label(root, text="No folder selected")
folder_label.pack()

# Button 
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack()

# Button 
take_screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
take_screenshot_button.pack()

# Label 
screenshot_label = tk.Label(root)
screenshot_label.pack()

root.mainloop()