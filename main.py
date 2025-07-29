import gradio as gr
from app.interface import get_mic_interface, get_file_interface

import mlflow

if __name__ == "__main__":
    mlflow.set_experiment("Speech_Translation_App")

    demo = gr.TabbedInterface(
        [get_mic_interface(), get_file_interface()],
        ["Transcribe Microphone", "Transcribe Audio File"]
    )

    demo.launch(debug=True)