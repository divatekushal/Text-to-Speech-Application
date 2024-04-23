import pyttsx3
import customtkinter
import tkinter as tk


customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Application")
        frame = customtkinter.CTkFrame(master=root, width=340, height=500, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.engine = pyttsx3.init()

        self.heading_label = customtkinter.CTkLabel(master=frame, text="Text to Speech", font=("Century Gothic", 20, ), text_color="lightblue")
        self.heading_label.place(relx=0.5, y=15, anchor="center")

        self.enter_text_label = customtkinter.CTkLabel(master=frame, text="Enter your text:")
        self.enter_text_label.place(x=10, y=50)

        self.text_input = customtkinter.CTkTextbox(master=frame, height=150, width=300)
        self.text_input.place(x=10, y=80)

        self.language_label = customtkinter.CTkLabel(master=frame, text="Select Language:")
        self.language_label.place(x=10, y=250)
        self.language_var = customtkinter.StringVar(master=frame)
        self.language_dropdown = customtkinter.CTkComboBox(master=frame)
        self.language_dropdown.place(x=130, y=250)

        self.voice_label = customtkinter.CTkLabel(master=frame, text="Select Voice:")
        self.voice_label.place(x=10, y=280)
        self.voice_var = customtkinter.StringVar(master=frame)
        self.voice_dropdown = customtkinter.CTkComboBox(master=frame)
        self.voice_dropdown.place(x=130, y=280)

        self.update_languages()

        self.rate_label = customtkinter.CTkLabel(master=frame, text="Rate:")
        self.rate_label.place(x=10, y=310)
        self.rate_slider = customtkinter.CTkSlider(master=frame, from_=50, to=200)
        self.rate_slider.place(x=130, y=310)

        self.pitch_label = customtkinter.CTkLabel(master=frame, text="Pitch:")
        self.pitch_label.place(x=10, y=340)
        self.pitch_slider = customtkinter.CTkSlider(master=frame, from_=0, to=20)
        self.pitch_slider.place(x=130, y=340)

        self.volume_label = customtkinter.CTkLabel(master=frame, text="Volume:")
        self.volume_label.place(x=10, y=370)
        self.volume_slider = customtkinter.CTkSlider(master=frame, from_=0, to=100)
        self.volume_slider.place(x=130, y=370)

        self.play_button = customtkinter.CTkButton(master=frame, text="Play", command=self.play_text,width=100)
        self.play_button.place(x=10, y=410)

        self.pause_button = customtkinter.CTkButton(master=frame, text="Pause", command=self.pause_text,width=100)
        self.pause_button.place(x=120,y=410)

        self.stop_button = customtkinter.CTkButton(master=frame, text="Stop", command=self.stop_text,width=100)
        self.stop_button.place(x=230, y=410)

        self.save_button = customtkinter.CTkButton(master=frame, text="Save Audio", command=self.save_audio)
        self.save_button.place(relx=0.5, y=470,anchor="center")

    def update_languages(self):
        self.language_dropdown['values'] = ["English"]
        self.language_dropdown.set("English")  

        self.update_voices()

    def update_voices(self, *args):
        voices = self.engine.getProperty('voices')
        voice_names = [voice.name for voice in voices]
        self.voice_dropdown['values'] = ["Male"]
        self.voice_dropdown.set("Male")
        
        if not voice_names: 
            self.voice_dropdown['values'] = ["Male"]
            self.voice_dropdown.set("Male")
        else:
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
    app = customtkinter.CTk()
    app.title('Text to Speech App')
    app.geometry("400x600")
    TextToSpeechApp(app)
    
    app.mainloop()
