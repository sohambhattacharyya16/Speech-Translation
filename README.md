# 🎙️ Speech-to-Text and Translation Pipeline

This project is an end-to-end pipeline for **speech transcription** and **translation**, built with open-source Hugging Face models. The application is containerized using Docker and includes a GitHub Actions workflow for automatic image builds and deployments — making it universally portable and cloud-ready.

---

## 🚀 Features

- 🎤 Automatic Speech Recognition (ASR) with [distil-whisper/distil-small.en](https://huggingface.co/distil-whisper/distil-small.en)
- 🌍 Translation to multiple languages with [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M)
- ⚙️ Dockerized for platform independence
- 🔁 GitHub Actions for CI/CD: automatic image builds and Docker Hub push
- 📦 Clean, modular Python structure
- ☁️ OpenShift compatible deployment

---

## 🧠 Models Used

| Task          | Model                                                  |
|---------------|--------------------------------------------------------|
| ASR           | `distil-whisper/distil-small.en`                       |
| Translation   | `facebook/nllb-200-distilled-600M`                     |

---

# Choices are presented as the model expects. The language codes are provded in "Languages in FLORES-200" in the link below
https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200
