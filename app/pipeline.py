from transformers import pipeline
from app.config import ASR_MODEL, TRANSLATION_MODEL

# Load pipelines
asr_pipeline = pipeline("automatic-speech-recognition", model=ASR_MODEL)
translator = pipeline("translation", model=TRANSLATION_MODEL)

def transcribe_speech(filepath, target_language):
    if not filepath:
        return "No audio found, please retry.", []

    # Transcription
    output = asr_pipeline(filepath)
    transcription = output["text"]

    # Translation
    text_translated = translator(transcription, src_lang="eng_Latn", tgt_lang=target_language)
    translation = text_translated[0]['translation_text']

    return transcription, translation

