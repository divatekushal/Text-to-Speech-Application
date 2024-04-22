# Text-to-Speech Application

The Text-to-Speech Application is a Python GUI application that allows users to input text and convert it into speech. It provides various customization options for adjusting speech parameters such as rate, pitch, and volume, as well as options for selecting different languages and voices.

![Text-to-Speech Application](path/to/your/image.png)


## Features

- **Graphical User Interface (GUI)**: The application has an interactive interface built using Python's tkinter library, providing an intuitive user experience for text input and speech output.
  
- **Text-to-Speech Conversion**: Utilizes the pyttsx3 library to convert the entered text into speech.

- **Language and Voice Selection**: Users can choose from different languages and voices supported by the pyttsx3 library to customize the speech output.

- **Speech Parameter Adjustment**: Allows users to adjust speech parameters including rate, pitch, and volume using sliders.

- **Playback Controls**: Includes buttons for play, pause, and stop functionalities to manage the speech output effectively.

- **Save Audio**: Users can save the generated speech as audio files in MP3 format for offline use or sharing purposes.

## Requirements

- Python 3.x
- tkinter library
- pyttsx3 library

## Installation

1. Clone the repository:

```
git clone https://github.com/your_username/text-to-speech-app.git
```

2. Navigate to the project directory:

```
cd text-to-speech-app
```

3. Install dependencies:

```
pip install tkinter
pip install pyttsx3
```

## Usage

1. Run the application:

```
python text_to_speech.py
```

2. Enter the text you want to convert into speech in the input field.

3. Choose the language and voice for the speech output from the dropdown menus.

4. Adjust speech parameters (rate, pitch, volume) using the sliders if desired.

5. Click the "Play" button to listen to the speech output. Use the playback controls (pause, stop) as needed.

6. Click the "Save Audio" button to save the speech as an audio file in MP3 format.

