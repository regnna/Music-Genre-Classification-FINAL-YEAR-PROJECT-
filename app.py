# import the libraries

import math
import numpy as np
import pickle
import streamlit as st
import os
import warnings
warnings.filterwarnings("ignore")
# from librosa import librosa
# SET PAGE WIDE
st.set_page_config(page_title='Music Genre Prediction', layout="centered", initial_sidebar_state="collapsed",

                   page_icon="icon.jpeg",
                   menu_items={
                       'Get Help': 'https://github.com/regnna',
                       'Report a bug': 'https://github.com/regnna',
                       'About': 'Regnna'
                   })


st.markdown("<h1 style='text-align: center; color: gold;'> Music Genre Prediction </h1>",
            unsafe_allow_html=True)

hide_st_style = """
                <style>
                MainMenu {visibility:hidden;}
                header{visibility:hidden;}
                footer{visibility:hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Add background image

st.markdown(
    f"""
         <style>
         .stApp {{
             background-image:
              url("https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)

# Add description


def getmetadata(song):
    import librosa
    y, sr = librosa.load(song, mono=True, duration=500)
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
    
    for i in range(1, 21): # For each of 20 MFCCs
        feature_dict[f'mfcc{i}_mean'] = np.mean(mfcc[i-1])
        feature_dict[f'mfcc{i}_var'] = np.var(mfcc[i-1])
    st.audio(y, sample_rate=sr)
    # 'label': ... # Requires additional context. 
    return list(feature_dict.values())


with st.expander("Description"):
    st.info("""A Simple ML Website to predict genre of a given music/song, the .wav file of the audio required to detect its genre.
    ENJOY!!
 """)
uploaded_file = st.file_uploader("Upload a .wav file please", type='wav')

if uploaded_file is None:
    st.write("Please upload a WAV file.")

else:
    # Process the uploaded WAV file
    
    g = getmetadata(uploaded_file)
    path = os.path.join('svc_model (2).hdf5')
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    svmp = data['svmp']
    norma = data['norma']
    lgn = data['lgn']
    x = norma.transform([g])
    pred = svmp.predict(x)
    st.markdown(f"<h3 style='text-align: center; color: white;'> {pred[0]} </h3>",
                unsafe_allow_html=True)
    # st.write(pred[0])
