import streamlit as st
from PIL import Image


# Covert the pillow image to greyscale
def convert_img(image):
    gray_img = image.convert("L")
    # Show the greyscale image on the webpage
    st.image(gray_img)


st.subheader("Color to Grayscale Converter")

choices = ["From Camera", "From Computer"]
for index, todo in enumerate(choices):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:

        if todo == "From Camera":

            with st.expander("Start Camera"):
                # Start the camera
                camera_image = st.camera_input("Camera")
                if camera_image:
                    # Create a pillow image instance
                    img = Image.open(camera_image)
                    convert_img(img)
        else:
            with st.expander("Browse images"):
                # Start the browsing
                browse_img = st.file_uploader("Upload Image")
                if browse_img:
                    img = Image.open(browse_img)
                    convert_img(img)


