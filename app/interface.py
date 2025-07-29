import gradio as gr
from app.pipeline import transcribe_speech
from app.config import LANGUAGES

def get_mic_interface():
    return gr.Interface(
        fn=transcribe_speech,
        inputs=[
            gr.Audio(sources="microphone", type="filepath"),
            gr.Dropdown(label="Target Language", choices=LANGUAGES, value=LANGUAGES[0])
        ],
        outputs=[
            gr.Textbox(label="Transcription", lines=3),
            gr.Textbox(label="Translation", lines=5)
        ],
        flagging_mode="never"
    )

def get_file_interface():
    return gr.Interface(
        fn=transcribe_speech,
        inputs=[
            gr.Audio(sources="upload", type="filepath"),
            gr.Dropdown(label="Target Language", choices=LANGUAGES, value=LANGUAGES[0])
        ],
        outputs=[
            gr.Textbox(label="Transcription", lines=3),
            gr.Textbox(label="Translation", lines=5)
        ],
        flagging_mode="never"
    )
