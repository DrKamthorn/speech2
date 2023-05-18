import streamlit as st
import whisper

st.title("งานสารบรรณ ศูนย์การแพทย์กาญจนาภิเษก")

audio_file=st.file_uploader("Upload ไฟล์เสียง", type=["wav","mp3","m4a"])

model=whisper.load_model("medium")
st.text("กำลัง Upload ไฟล์")

if st.sidebar.button("Transcribe Audio"):
	if audio_file is not None:
		st.sidebar.success("Transcribing Audio")
		transcription=model.transcribe(audio_file.name)
		st.sidebar.success("transcription Complete")
		st.markdown(transcription["text"])
	else:
		st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)