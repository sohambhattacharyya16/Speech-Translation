# from os import environ
# environ["TRANSFORMERS_CACHE"] = "/app/hf_cache"  # Optional: already handled in Dockerfile

from transformers import pipeline
from app.config import ASR_MODEL, TRANSLATION_MODEL

CACHE_DIR = "/app/hf_cache"

# Load pipelines with explicit cache directory
asr_pipeline = pipeline("automatic-speech-recognition", model=ASR_MODEL, cache_dir=CACHE_DIR)
translator = pipeline("translation", model=TRANSLATION_MODEL, cache_dir=CACHE_DIR)

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



