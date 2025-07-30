import gradio as gr
from app.interface import get_mic_interface, get_file_interface

if __name__ == "__main__":
    demo = gr.TabbedInterface(
        [get_mic_interface(), get_file_interface()],
        ["Transcribe Microphone", "Transcribe Audio File"]
    )

    demo.launch(server_name="0.0.0.0", server_port=7860, debug=True)