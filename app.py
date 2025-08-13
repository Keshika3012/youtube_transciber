import os
import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from pytube import YouTube
from youtube_transcript_api import(
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
    CouldNotRetrieveTranscript
)

from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

def get_youtube_transcript(url):
    try:
        video_id = YouTube(url).video_id
        st.write(f"Video ID: {video_id}") 
        
        # Create API instance and fetch transcript directly
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=['en'])
        text = " ".join([item.text for item in transcript_data])
        st.write(f"Transcript length: {len(text)} characters") 
        return text
    except TranscriptsDisabled:
        st.error("Transcripts Disabled")
    except NoTranscriptFound:
        st.error("No Transcript Found")
    except VideoUnavailable:
        st.error("Video Unavailable")
    except CouldNotRetrieveTranscript:
        st.error("Could not retrieve transcript")
    except Exception as e:
        st.error(f"Unexpected Error: {str(e)}")
        return None

def save_transcript_to_file(text, filename = "transcript.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

st.title("AI Powered Tutor")
st.write("Ask questions from Youtube lecture")

video_url = st.text_input("Enter Youtube Video URL")

if st.button("process video"):
    if video_url:
        transcript_text = get_youtube_transcript(video_url)
        if transcript_text:
            save_transcript_to_file(transcript_text)

            loader = TextLoader("transcript.txt", encoding="utf-8")
            documents = loader.load()

            splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
            docs = splitter.split_documents(documents)

            embeddings = OpenAIEmbeddings()
            vectorstores = FAISS.from_documents(docs, embeddings)
            retriever = vectorstores.as_retriever()
            qa_chain = RetrievalQA.from_chain_type(llm = OpenAI(), retriever = retriever)

            st.session_state.qa_chain = qa_chain
            st.success("Transcript processed successfully. You can ask questions now")
        else:
            st.warning("Please enter the valid URL")

if "qa_chain" in st.session_state:
    user_question = st.text_input("Ask a question")
    if user_question:
        answer = st.session_state.qa_chain.run(user_question)
        st.write("**Answer:**", answer)
