!pip install deep-translator
import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit app title
st.title("English to Urdu Translator")

# Text input for the user
english_text = st.text_area("Enter English Text:", "This is a sample paragraph. Translate this into Urdu.")

# Translation functionality
if st.button("Translate"):
    # Perform translation from English to Urdu using deep_translator
    try:
        translated_text = GoogleTranslator(source='en', target='ur').translate(english_text)

        # Show the result
        st.subheader("Translated Urdu Text:")
        st.write(translated_text)
    except Exception as e:
        st.error(f"Error occurred during translation: {e}")
streamlit run your_script_name.py

