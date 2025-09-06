import streamlit as st
import base64
from openai import OpenAI

#Initialize OpenAI client
client = OpenAI()

#Streamlit App
st.title("OpenAI Image Generator")
st.write('Enter a prompt below to generate an image using OpenAI's mode")

# input prompt
prompt = st.text_input("Eneter your prompt for image generation:")

if st.button("Generate Image")
  if prompt :
    try:
        with st.spinner("Generating Image...")
              # Call OpenAI Image API
              img = Client.image.generate( 
              model ="gpt-image1",
              n=1, size="1024X1024"
              )

              # Decode base64 image
              image_bytes = base64.b64decode(img.data[0].b64_json)

              #save temp image
              with open('generated_image.png", "wb") as f:fwrite(image-bytes)

              # Display in streamlit
              st.image("generated_image.png", caption="Generated
