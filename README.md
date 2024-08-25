# Speech-Controlled Automation

This project provides a Python-based application that enables speech-controlled automation of keyboard commands using the Vosk speech recognition library. The application uses a web interface for controlling the start and stop of the speech recognition process.

## Features

- **Speech Recognition**: Uses the Vosk API to recognize speech and map recognized words to keyboard commands.
- **Keyboard Automation**: Integrates with PyAutoGUI to simulate keyboard presses based on recognized speech commands.
- **Web Interface**: Provides a simple web-based interface to start and stop the speech recognition process.
- **Threaded Execution**: Speech recognition runs in a separate thread, allowing for responsive control via the web interface.

## Prerequisites

Before you can run this application, ensure you have the following installed:

- Python 3.x
- [Vosk](https://alphacephei.com/vosk/) (Speech recognition library)
- PyAutoGUI
- PyAudio
- Eel (For the web interface)

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ahadrazarc/SpeechRecognition.git
    cd SpeechRecognition
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the Vosk model (English) and place it in the project directory. Update the `model_path` variable in the code if necessary.

4. Create the `web` directory and add an HTML file named `speechcode.html` for the user interface.

### Usage

1. Start the application:

    ```bash
    python app.py
    ```

2. The application will launch a web interface. Use the interface to start and stop speech recognition.

3. Define your custom command-to-key mappings through the web interface. The application will listen for the specified commands and execute the corresponding keyboard actions.

### Code Overview

- **`listen_for_commands()`**: This function handles the speech recognition process, converting recognized speech into text and mapping it to corresponding keyboard actions.

- **`valuespeech()`**: Exposed to Eel, this function starts the speech recognition process in a new thread.

- **`stop_listening()`**: Exposed to Eel, this function stops the speech recognition process.

- **Web Interface**: The application uses Eel to create a web interface for controlling the speech recognition process. The HTML file (`speechcode.html`) should be placed in the `web` directory.

### Notes

- The Vosk model path should be updated in the code if you place the model in a different directory.
- Ensure your microphone is properly configured and accessible by PyAudio.
- Customize the `command_dict` with the commands and corresponding keyboard actions you need.


### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

### Acknowledgments

- [Vosk](https://alphacephei.com/vosk/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Eel](https://github.com/samuelhwilliams/Eel)
