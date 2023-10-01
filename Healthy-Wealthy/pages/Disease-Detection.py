import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

import base64

from PIL import ImageOps, Image
import numpy as np


def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def classify(image, model, class_names):
    """
    This function takes an image, a model, and a list of class names and returns the predicted class and confidence
    score of the image.

    Parameters:
        image (PIL.Image.Image): An image to be classified.
        model (tensorflow.keras.Model): A trained machine learning model for image classification.
        class_names (list): A list of class names corresponding to the classes that the model can predict.

    Returns:
        A tuple of the predicted class name and the confidence score for that prediction.
    """
    # convert image to (224, 224)
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # convert image to numpy array
    image_array = np.asarray(image)

    # normalize image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # set model input
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # make prediction
    prediction = model.predict(data)
    # index = np.argmax(prediction)
    index = 0 if prediction[0][0] > 0.95 else 1
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score



st.set_page_config(
    page_title="Desiese Detection",
    page_icon="🔍",
)

st.markdown("<h1 style='color: #3B444B; font-style: italic; font-family: Comic Sans MS; font-size:4rem' >Healthy Wealthy Disease Detection🔍</h1> <h3 style='color:#54626F; font-style: italic; font-family: Comic Sans MS; font-size:2rem'>Healthy Wealthy, Early Detection: Safeguarding Your Well-being Together!🏥🌟</h3>", unsafe_allow_html=True)


# set header
st.header('Please upload a chest X-ray image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('D:/llm projects/Healthy-Wealthy/pneumonia-classification-web-app-python-streamlit-main/model/pneumonia_classifier.h5')

# load class names
with open('D:/llm projects/Healthy-Wealthy/pneumonia-classification-web-app-python-streamlit-main/model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("### score: {}%".format(int(conf_score * 1000) / 10))
