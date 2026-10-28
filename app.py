import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="YOLOv7 Object Detection", page_icon="🎯", layout="wide")

st.title("🎯 Real-Time Object Detection Using the YOLOv7 Algorithm")
st.write("Upload an image to prepare it for object detection.")

st.sidebar.header("Project Information")
st.sidebar.write("Algorithm: YOLOv7")
st.sidebar.write("Framework: PyTorch")
st.sidebar.write("Application: Object Detection")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)
    st.info(
        "Image uploaded successfully. To detect objects, "
        "configure the YOLOv7 model weights and dependencies."
    )
else:
    st.info("Choose an image to begin.")

st.caption("Final-year project demonstration")
