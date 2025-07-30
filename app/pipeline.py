import os
# Set cache directory to avoid PermissionError in Docker
os.environ["TRANSFORMERS_CACHE"] = "/app/hf_cache"

from transformers import pipeline
from app.config import ASR_MODEL, TRANSLATION_MODEL

# Load pipelines
asr_pipeline = pipeline("automatic-speech-recognition", model=ASR_MODEL)
translator = pipeline("translation", model=TRANSLATION_MODEL)

def transcribe_speech(filepath, target_language):
    if not filepath:
        return "No audio found, please retry.", ""

    # Transcription
    output = asr_pipeline(filepath)
    transcription = output["text"]

    # Translation
    translated = translator(transcription, src_lang="eng_Latn", tgt_lang=target_language)
    translation = translated[0]["translation_text"]

    return transcription, translation


