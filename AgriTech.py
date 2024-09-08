import streamlit as st
import pandas as pd
from PIL import Image
import io

# Set page config
st.set_page_config(page_title="AgriDetect", page_icon="🌾", layout="wide")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define pages
def home():
    st.title("Welcome to AgriDetect")
    st.write("AgriDetect is a cutting-edge application designed to detect crop leaf diseases in rice agriculture using advanced image processing techniques.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/300x200.png?text=Rice+Field", caption="Rice Field")
        st.image("https://via.placeholder.com/300x200.png?text=Leaf+Close-up", caption="Leaf Close-up")
    
    st.header("User Testimonials")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/100x100.png?text=User+1", caption="John Doe")
        st.write('"AgriDetect has revolutionized how we monitor our rice crops. The accuracy is impressive!"')
    with col2:
        st.image("https://via.placeholder.com/100x100.png?text=User+2", caption="Jane Smith")
        st.write('"This app has helped us identify diseases early, saving us from major crop losses."')
    
    st.header("Image Gallery")
    gallery = st.columns(3)
    for i in range(3):
        with gallery[i]:
            st.image(f"https://via.placeholder.com/200x200.png?text=Rice+Image+{i+1}")

def upload_image():
    st.title("Upload Image of Rice Leaves")
    st.write("Please upload a clear image of the rice leaves you want to analyze for disease detection. Ensure the leaves are well-lit and in focus.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Submit"):
            st.session_state.page = 'detection_result'
            st.session_state.uploaded_image = image

def detection_result():
    st.title("Detection Result")
    if 'uploaded_image' in st.session_state:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(st.session_state.uploaded_image, caption="Analyzed Image")
        with col2:
            st.write("Disease Type: Powdery Mildew")
            st.write("Severity Level: Moderate")
        
        st.subheader("Recommended Actions")
        actions = [
            "Apply a fungicide suitable for powdery mildew.",
            "Ensure plants have good air circulation.",
            "Remove and dispose of infected leaves.",
            "Avoid overhead watering."
        ]
        for action in actions:
            st.write(f"- {action}")
        
        st.subheader("Additional Resources")
        resources = st.columns(3)
        resource_images = [
            "https://via.placeholder.com/100x100.png?text=Fungicide+Products",
            "https://via.placeholder.com/100x100.png?text=Air+Circulation+Tips",
            "https://via.placeholder.com/100x100.png?text=Watering+Techniques"
        ]
        for i, img in enumerate(resource_images):
            with resources[i]:
                st.image(img)

def leaf_disease_search():
    st.title("Leaf Disease Search")
    st.write("Search for leaf diseases and view results")
    
    search_term = st.text_input("Enter your search")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write("Refine your search")
        st.checkbox("Bacterial diseases")
        st.checkbox("Fungal diseases")
        st.checkbox("Viral diseases")
        st.selectbox("Sort by", ["Relevance", "Name", "Severity"])
    with col2:
        diseases = [f"Leaf disease {i}" for i in range(1, 10)]
        for disease in diseases:
            st.image(f"https://via.placeholder.com/100x100.png?text={disease}")
            st.write(disease)

# Navigation
menu = ["Home", "Upload Image", "Detection Result", "Leaf Disease Search"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.session_state.page = 'home'
elif choice == "Upload Image":
    st.session_state.page = 'upload_image'
elif choice == "Detection Result":
    st.session_state.page = 'detection_result'
elif choice == "Leaf Disease Search":
    st.session_state.page = 'leaf_disease_search'

# Display page
if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'upload_image':
    upload_image()
elif st.session_state.page == 'detection_result':
    detection_result()
elif st.session_state.page == 'leaf_disease_search':
    leaf_disease_search()

# Footer
st.markdown("---")
st.write("© 2023 AgriDetect. All rights reserved.")
st.write("Privacy Policy | Terms of Service | Contact Us")