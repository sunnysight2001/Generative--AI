#!pip install -qU openai
!pip install openai==0.28
!pip install gradio
import openai
import gradio as gr
import requests
from PIL import Image
from io import BytesIO
# SET openai api key

openai.api_key = "your api key"
# function for image generation


def generate_image(prompt):

  response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
  )
  image_url = response['data'][0]['url']

  image_bytes = requests.get(image_url).content
  return Image.open(BytesIO(image_bytes))

  return image_bytes
  import gradio as gr

result = gr.Interface(fn=generate_image, inputs="text", outputs="image")
result.launch(debug='True')

  
