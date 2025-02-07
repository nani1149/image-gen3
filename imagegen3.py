import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")

# Streamlit UI
st.title("AI Image Generator with Google Imagen3")

# User input for prompt
prompt = st.text_input("Enter image description:", "a portrait of a sheepadoodle wearing a cape")

if st.button("Generate Image"):
    try:
        client = genai.Client(api_key=google_api_key)
        response = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            )
        )
        
        for generated_image in response.generated_images:
            image = Image.open(BytesIO(generated_image.image.image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error: {e}")
