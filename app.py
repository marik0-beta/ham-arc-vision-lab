import cv2
import time
from collections import deque

import numpy as np
import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="HAM ARC Vision Lab", page_icon="🔎", layout="wide")

st.title("HAM ARC Vision Lab")
st.caption("A small computer-vision lab: explore image processing, edge detection, and color segmentation.")

st.info(
    "This demo runs on uploaded images; it does not require Arduino, sensors, or a webcam. "
    "It is an image-processing prototype, not a trained object detector."
)

uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"])

mode = st.selectbox(
    "Choose a vision operation",
    [
        "Grayscale",
        "Canny edge detection",
        "Threshold segmentation",
        "HSV color mask",
        "Compare original and processed",
    ],
)

col1, col2 = st.columns(2)

def pil_to_bgr(pil_image):
    rgb = np.array(pil_image.convert("RGB"))
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

def bgr_to_pil(image):
    if len(image.shape) == 2:
        return Image.fromarray(image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)

if uploaded is None:
    st.subheader("Try it")
    st.write("Upload a photo or screenshot to see how classical computer vision transforms it.")
    st.markdown(
        "- **Grayscale:** removes color information.\n"
        "- **Canny edges:** highlights strong intensity boundaries.\n"
        "- **Thresholding:** separates pixels by brightness.\n"
        "- **HSV color mask:** isolates a selected hue range."
    )
else:
    try:
        original_pil = Image.open(uploaded).convert("RGB")
        image_bgr = pil_to_bgr(original_pil)
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

        if mode == "Grayscale":
            processed = gray
        elif mode == "Canny edge detection":
            threshold1 = st.sidebar.slider("Lower edge threshold", 0, 255, 80)
            threshold2 = st.sidebar.slider("Upper edge threshold", 0, 255, 160)
            processed = cv2.Canny(gray, threshold1, threshold2)
        elif mode == "Threshold segmentation":
            threshold = st.sidebar.slider("Brightness threshold", 0, 255, 127)
            _, processed = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        elif mode == "HSV color mask":
            st.sidebar.write("Adjust the HSV hue interval to isolate a color.")
            hue_low = st.sidebar.slider("Minimum hue", 0, 179, 0)
            hue_high = st.sidebar.slider("Maximum hue", 0, 179, 25)
            sat_low = st.sidebar.slider("Minimum saturation", 0, 255, 70)
            val_low = st.sidebar.slider("Minimum value/brightness", 0, 255, 50)
            hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
            lower = np.array([hue_low, sat_low, val_low], dtype=np.uint8)
            upper = np.array([hue_high, 255, 255], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower, upper)
            processed = cv2.bitwise_and(image_bgr, image_bgr, mask=mask)
        else:
            processed = cv2.Canny(gray, 80, 160)

        st.subheader("Results")
        left, right = st.columns(2)
        with left:
            st.image(original_pil, caption="Original image", use_container_width=True)
        with right:
            st.image(bgr_to_pil(processed), caption=mode, use_container_width=True)

        if mode == "Compare original and processed":
            st.write("The right panel shows edges; change the operation to explore other transformations.")

        if len(processed.shape) == 2:
            export_image = Image.fromarray(processed)
        else:
            export_image = bgr_to_pil(processed)
        import io
        buffer = io.BytesIO()
        export_image.save(buffer, format="PNG")
        st.download_button(
            "Download processed image",
            data=buffer.getvalue(),
            file_name="ham_arc_processed.png",
            mime="image/png",
        )
        st.caption(f"Image size: {original_pil.width} × {original_pil.height} pixels")
    except Exception as exc:
        st.error(f"Could not process this image. Try a different PNG or JPEG. Details: {exc}")

with st.expander("How it works"):
    st.write(
        "The app uses OpenCV for image transformations, NumPy for pixel arrays, and Streamlit "
        "for the interface. Classical image processing is useful for understanding the vision "
        "pipeline before moving on to object detection or hardware integration."
    )
