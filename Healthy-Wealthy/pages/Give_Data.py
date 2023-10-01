import pymongo
import streamlit as st


st.set_page_config(
    page_title="data"
)

st.markdown("<h1 style='color: #3B444B; font-style: italic; font-family: Comic Sans MS; font-size:4rem' >Healthy Wealthy Data Collector</h1> <h3 style='color:#54626F; font-style: italic; font-family: Comic Sans MS; font-size:2rem'>Lets collect your health related data to be used for personalised health assistance</h3>", unsafe_allow_html=True)


mongo_uri = "mongodb+srv://<username>:<password>@<cluster_url>/<database_name>?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_uri)
db = client.get_database()
collection = db.get_collection("users")

name = st.text_input('User name')

physical = st.text_input('Physical Health(comma seperated)')

mental = st.text_input('Mental Health(comma seperated)')

exercise = st.text_input('Exercise Preferences')

date = st.text_input('Dai;y Activity Date (YYYY-MM-DD)')

ac_type = st.text_input('Daily Activity Type')

ac_duration = st.text_input('Daily Activity duration (minutes)')

mood = st.text_input("Daily Activity Mood")

blog_title = st.text_input("Blog Title")

blog_content = st.text_input("Blog content")

if st.button('Submit'):
    data = {
        "name": name,
        "physical_health": physical,
        "mental_health": mental,
        "exercise": exercise,
        "ac_type" : ac_type,
        "ac_duration" : ac_duration,
        "mood": mood,
        "blog_title" : blog_title,
        "blog_content" : blog_content
    }
    result = collection.insert_one(data)



