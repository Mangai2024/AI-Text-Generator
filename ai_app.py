
import streamlit as st
from transformers import pipeline


#Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")
#Streamlit App layout
st.title("AI Text Generator")
st.write("Generate creative text using GPT-2 model")
#user input
prompt = st.text_input("Enter your  prompt:", "Artificial Intelligence is transforming the future of healthcare")

# Generate Button
if st.button("Generate"):
    with st.spinner("Generating..."):
        output = generator(prompt, max_length=150, num_return_sequences=1)
        st.success("Here's your AI-generated text:")
        st.write(output[0]['generated_text'])
