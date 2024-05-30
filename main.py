import tkinter as tk
from PIL import ImageGrab
import pyautogui

class ColorPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")

        # Labels
        self.label = tk.Label(root, text="Press 'Enter' to\npick a color!", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Color display
        self.color_display = tk.Label(root, text="", font=("Helvetica", 14), bg="white", width=40)
        self.color_display.pack(pady=20)

        # Enter key bind
        self.root.bind('<Return>', self.capture_color)

    def capture_color(self, event=None):

        # Wait for user to press enter
        x, y = pyautogui.position()

        try:
            # Capture screen
            screen = ImageGrab.grab()
            rgb = screen.getpixel((x,y))
            hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

            # Display information
            self.color_display.config(text=f"RGB: {rgb}\nHex: {hex_color}", bg=hex_color)
        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPicker(root)
    root.mainloop()
