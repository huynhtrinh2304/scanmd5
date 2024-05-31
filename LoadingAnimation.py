import tkinter as tk
from PIL import Image, ImageTk
import threading

class AnimatedGif(tk.Label):
    def __init__(self, master, gif_file_path, delay=None):
        super().__init__(master)
        self.pack(fill=tk.BOTH)

        self.gif_frames = []
        self.frame_delay = None
        self.frame_count = -1
        self.stop_flag = False

        self.load_gif(gif_file_path, delay)

    def load_gif(self, gif_file_path, delay=None):
        try:
            gif_file = Image.open(gif_file_path)
            self.frame_delay = delay or gif_file.info['duration']
            for frame in range(0, gif_file.n_frames):
                gif_file.seek(frame)
                self.gif_frames.append(ImageTk.PhotoImage(gif_file.copy()))
            self.current_frame = self.gif_frames[0]
            self.config(image=self.current_frame)
        except FileNotFoundError:
            print(f"Error: GIF file '{gif_file_path}' not found.")

    def start(self):
        if not self.stop_flag:
            self.play_gif()

    def play_gif(self):

        if self.frame_count >= len(self.gif_frames) - 1:
            self.frame_count = -1
        else:
            self.frame_count += 1
            self.current_frame = self.gif_frames[self.frame_count]
            self.config(image=self.current_frame)
        if not self.stop_flag:
            self.after(self.frame_delay, self.play_gif)

    def stop(self):
        self.config(state='disabled')
