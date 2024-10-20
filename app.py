import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Streamlit app title
st.title("English to Urdu Translator")

# Text input for the user
english_text = st.text_area("Enter English Text:", "This is a sample paragraph. Translate this into Urdu.")

# Translation functionality
if st.button("Translate"):
    # Perform translation from English to Urdu
    translation = translator.translate(english_text, src='en', dest='ur')

    # Show the result
    st.subheader("Translated Urdu Text:")
    st.write(translation.text)

