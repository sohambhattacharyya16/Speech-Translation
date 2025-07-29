from transformers import pipeline
from app.config import ASR_MODEL, TRANSLATION_MODEL
import mlflow

# Load pipelines
asr_pipeline = pipeline("automatic-speech-recognition", model=ASR_MODEL)
translator = pipeline("translation", model=TRANSLATION_MODEL)

def transcribe_speech(filepath, target_language):
    if not filepath:
        return "No audio found, please retry.", []

    with mlflow.start_run(nested=True):
        mlflow.log_param("target_language", target_language)
        mlflow.log_param("audio_file", filepath)

        # Transcription
        output = asr_pipeline(filepath)
        transcription = output["text"]
        mlflow.log_text(transcription, "transcription.txt")

        # Translation
        text_translated = translator(transcription, src_lang="eng_Latn", tgt_lang=target_language)
        translation = text_translated[0]['translation_text']
        mlflow.log_text(translation, "translation.txt")

    return transcription, translation
