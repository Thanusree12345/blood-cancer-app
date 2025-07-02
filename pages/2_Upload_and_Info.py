import streamlit as st

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please login first.")
    st.stop()

st.title("📤 Upload Image & Understand Stages")

uploaded_image = st.file_uploader("Upload a blood cell image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

st.markdown("### 🔬 Blood Cancer Stages Information")
st.markdown("""
- **Benign**: Non-cancerous cells.
- **Malignant Pre B**: Precursor B cells showing malignant growth.
- **Malignant Early Pre B**: Early abnormal growth stage.
- **Malignant Pro B**: Advanced malignant Pro-B cell stage.
""")