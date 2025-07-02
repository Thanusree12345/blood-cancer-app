import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please login first.")
    st.stop()

st.title("🔍 Prediction Page")

model = tf.keras.models.load_model("cnn_model.h5")

uploaded_image = st.file_uploader("Upload Image to Predict", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image).resize((224, 224))  # match model input size
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image) / 255.0
    if img_array.shape[-1] == 4:  # Handle alpha channel
        img_array = img_array[..., :3]
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    pred_class = np.argmax(pred)

    label_map = {
        0: "Benign",
        1: "Malignant Pro B",
        2: "Malignant Early Pre B",
        3: "Malignant Pre B"
    }

    st.markdown("### 🔬 Prediction Result:")
    st.success(f"**{label_map[pred_class]}**")