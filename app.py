#import the libraries

# from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
# from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D
# from tensorflow.keras.models import Sequential
import tensorflow as tf
import math
import numpy as np
import pickle
import streamlit as st
import os
import warnings
warnings.filterwarnings("ignore")
import keras
# from librosa import librosa
#SET PAGE WIDE
st.set_page_config(page_title='Music Genre Prediction',layout="centered",initial_sidebar_state="collapsed",

page_icon="logo.jpeg",
    menu_items={
        'Get Help': 'https://github.com/regnna',
        'Report a bug': 'https://github.com/regnna',
        'About': 'Regnna'
    })


st.markdown(
    f"""
         <style>
         .stApp {{
             background-image:
              url("https://images.unsplash.com/photo-1524678606370-a47ad25cb82a?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: violet;'> Music Genre Prediction </h1>", unsafe_allow_html=True)

hide_st_style="""
                <style>
                #MainMenu {visibility:hidden;}
                header{visibility:hidden;}
                footer{visibility:hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html=True)
#Add background image
import base64

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


# set_bg_hack('1333741.png')
#Add description

def getmetadata(y,sr):
    import numpy as np

    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    feature_dict = {

        'chroma_stft_mean': np.mean(chroma_stft),
        'chroma_stft_var': np.var(chroma_stft),
        'rms_mean': np.mean(rms),
        'rms_var': np.var(rms),
        'spectral_centroid_mean': np.mean(spec_cent),
        'spectral_centroid_var': np.var(spec_cent),
        'spectral_bandwidth_mean': np.mean(spec_bw),
        'spectral_bandwidth_var': np.var(spec_bw),
        'rolloff_mean': np.mean(rolloff),
        'rolloff_var': np.var(rolloff),
        'zero_crossing_rate_mean': np.mean(zcr),
        'zero_crossing_rate_var': np.var(zcr),
        # 'harmony_mean': ..., # Not standard, requires additional context.
        # 'harmony_var': ..., # Not standard, requires additional context.
        # 'perceptr_mean': ..., # Not standard, requires additional context.
        # 'perceptr_var': ..., # Not standard, requires additional context.
        'tempo': librosa.feature.tempo(y=y, sr=sr)[0],

    }

    for i in range(1, 21):  # For each of 20 MFCCs
        feature_dict[f'mfcc{i}_mean'] = np.mean(mfcc[i-1])
        feature_dict[f'mfcc{i}_var'] = np.var(mfcc[i-1])
    # 'label': ... # Requires additional context.
    return list(feature_dict.values())

with st.expander("Description"):
    st.info("""A Simple ML Website to predict genre of a given music/song, the .wav file of the audio required to detect its genre.
    ENJOY!!
    
 """)
uploaded_file = st.file_uploader(
    "Upload the file here", type='wav')

if uploaded_file is None:
    # st.write("Upload WAV file")
    st.markdown(f"<h3 style='text-align: center; color: black;'> Upload a .wav file please</h3>",
                unsafe_allow_html=True)

else:
    # Process the uploaded WAV file
    import librosa
    y, sr = librosa.load(uploaded_file, mono=True, duration=500)
    st.audio(y, sample_rate=sr)
    g=getmetadata(y,sr)
    path = os.path.join( 'cnn_model.hdf5')
    # picklein = open("cnn_model.hdf5", encoding="utf-8")
    # data=pickle.load(picklein)
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    # with open(path, 'rb') as pickled:
    #     data = pickle.load(pickled)
    
# load and evaluate a saved model
# from numpy import loadtxt
    from tensorflow.keras.models import load_model
 
# load model
    cnn = load_model('model.h5')
    scaler = data['scaler']
    # cnn = data['cnn']
    encoder = data['encoder']
    input=np.array(g)
    input=scaler.transform([input])
    x=input.reshape(1,input[0].shape[0],1)
    pred=cnn.predict(x)
    pred=np.argmax(pred)
    pred=encoder.classes_[pred]
    st.markdown(f"<h1 style='text-align: center; color: black;'> {pred} </h1>",
                unsafe_allow_html=True)
