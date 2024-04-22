import tkinter as tk
from tkinter import ttk
import pyttsx3

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Application")
        self.root.configure(bg="lightblue")

        self.engine = pyttsx3.init()

        self.heading_label = tk.Label(root, text="Text to Speech", font=("Arial", 14, "bold"), fg="lightblue", bg="blue")
        self.heading_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        self.enter_text_label = tk.Label(root, text="Enter your text:", bg="lightblue",fg="blue")
        self.enter_text_label.grid(row=1, column=0, padx=10, pady=0, sticky="w")

        self.text_input = tk.Text(root, height=10, width=40,fg="blue")
        self.text_input.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

        self.language_label = tk.Label(root, text="Select Language:",fg="blue", bg="lightblue")
        self.language_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(root, textvariable=self.language_var,)
        self.language_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.voice_label = tk.Label(root, text="Select Voice:",fg="blue", bg="lightblue")
        self.voice_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.voice_var = tk.StringVar()
        self.voice_dropdown = ttk.Combobox(root, textvariable=self.voice_var,)
        self.voice_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.update_languages()

        self.rate_label = tk.Label(root, text="Rate:",fg="blue", bg="lightblue")
        self.rate_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.rate_slider = tk.Scale(root, from_=50, to=200, orient="horizontal",bg="lightblue",fg="blue")
        self.rate_slider.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.pitch_label = tk.Label(root, text="Pitch:", bg="lightblue",fg="blue")
        self.pitch_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.pitch_slider = tk.Scale(root, from_=0, to=20, orient="horizontal",bg="lightblue",fg="blue")
        self.pitch_slider.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.volume_label = tk.Label(root, text="Volume:",fg="blue", bg="lightblue")
        self.volume_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal",bg="lightblue",fg="blue")
        self.volume_slider.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.play_button = tk.Button(root, text="Play", command=self.play_text,bg="blue",fg="lightblue")
        self.play_button.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_text,bg="blue",fg="lightblue")
        self.pause_button.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_text,bg="blue",fg="lightblue")
        self.stop_button.grid(row=8, column=2, padx=10, pady=5, sticky="w")

        self.save_button = tk.Button(root, text="Save Audio", command=self.save_audio,bg="blue",fg="lightblue")
        self.save_button.grid(row=9, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

    def update_languages(self):
        self.language_dropdown['values'] = ["English"]
        self.update_voices()

    def update_voices(self, *args):
        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]
        self.voice_dropdown['values'] = voice_names

        default_male_voice = [voice.name for voice in voices if 'male' in voice.name.lower() and 'english' in voice.name.lower()]
        default_female_voice = [voice.name for voice in voices if 'female' in voice.name.lower() and 'english' in voice.name.lower()]

        if default_male_voice:
            self.voice_dropdown.set(default_male_voice[0])
        elif default_female_voice:
            self.voice_dropdown.set(default_female_voice[0])

    def play_text(self):
        text = self.text_input.get("1.0", "end-1c")
        rate = self.rate_slider.get()
        pitch = self.pitch_slider.get()
        volume = self.volume_slider.get()
        voice_id = self.voice_var.get()

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('pitch', pitch)
        self.engine.setProperty('volume', volume / 100)
        self.engine.setProperty('voice', voice_id)

        self.engine.say(text)
        self.engine.runAndWait()

    def pause_text(self):
        self.engine.stop()

    def stop_text(self):
        self.engine.stop()

    def save_audio(self):
        text = self.text_input.get("1.0", "end-1c")
        rate = self.rate_slider.get()
        pitch = self.pitch_slider.get()
        volume = self.volume_slider.get()
        voice_id = self.voice_var.get()

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('pitch', pitch)
        self.engine.setProperty('volume', volume / 100)
        self.engine.setProperty('voice', voice_id)

        file_format = "mp3"
        file_name = "output." + file_format
        self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()

        print(f"Audio file saved as {file_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
