import time
import json
import pyautogui
import pyaudio
from vosk import Model, KaldiRecognizer
import threading
import eel

stop_event_speech = threading.Event()
speech_recognition_process = None


def listen_for_commands(command_dict, stop_event):
    model_path = "vosk model english"  # Correct model path
    print(f"Loading model from: {model_path}")
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1600)
    stream.start_stream()
    print("Listening...")

    while not stop_event.is_set():
        try:
            data = stream.read(1600, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(f"Raw Result: {result}")  # Debugging: Show raw result
                result_dict = json.loads(result)
                command_text = result_dict.get('text', '').lower()
                print(f"Recognized Command: {command_text}")  # Debugging: Show recognized command

                # Split the command text into individual commands
                command_words = command_text.split()
                for command in command_words:
                    if command in command_dict:
                        action = command_dict[command]
                        pyautogui.press(action)
                        print(f"Executing Action: {action}")  # Debugging: Show action being executed

        except Exception as e:
            print(f"An error occurred: {e}")

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Stopped Listening.")


@eel.expose
def valuespeech(command_dict):
    global speech_recognition_process
    global stop_event_speech

    print("User-defined command-to-key mappings:", command_dict)

    if speech_recognition_process is None or not speech_recognition_process.is_alive():
        print("Starting Speech Recognition...")
        stop_event_speech.clear()
        speech_recognition_process = threading.Thread(target=listen_for_commands,
                                                      args=(command_dict, stop_event_speech))
        speech_recognition_process.start()
    else:
        print("Speech Recognition is already running.")


@eel.expose
def stop_listening():
    global stop_event_speech
    global speech_recognition_process
    if speech_recognition_process is not None and speech_recognition_process.is_alive():
        print("Stopping Speech Recognition...")
        stop_event_speech.set()
        speech_recognition_process.join()  # Wait for the process to finish
        print("Speech Recognition Stopped.")
    else:
        print("Speech Recognition is not running.")




if __name__ == '__main__':
        eel.init('web')
        eel.start('speechcode.html',port=0)
