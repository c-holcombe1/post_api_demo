from io import BytesIO
import streamlit as st
from PIL import Image
import requests
#GET Request with existing API

api_key = st.secrets['api_key']
query = st.text_input("Enter a search term for a GIF (e.g., 'cheeseburgers')","")

@st.cache
def get_gif(api_key, query):
    api_url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": query,
        "limit": 1,
        "rating": "g",
        "lang": "en"
    }
    response = requests.get(api_url, params)
    if response.status_code == 200 and response.json()['data']:
        return response.json()['data'][0]['images']['original']['url']
    return None

if query:
    url = get_gif(st.secrets['api_key'], query)

if query:
    st.image(url)
else:
    st.write("No GIF found for this query.")



img=Image.open('raw_data/download_lewagon.png')
st.image(img)

from PIL import Image
 # prep the image to send to the FastAPI
if st.button('Flip Image'):
    img_buffer = BytesIO()

    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

# POST request

    fastapi_url = "http://localhost:8000/flip-image/"

    pass
    files = {"file": ("filename.png", img_buffer, "image/png")}


    response = requests.post(fastapi_url, files=files)

    if response:
        if response.status_code == 200:
            flipped_img_data = response.content
            flipped_img = Image.open(BytesIO(flipped_img_data))
            st.image(flipped_img, caption="Flipped Image.", use_column_width=True)
    else:
            st.error("An error occurred while processing the image.")
