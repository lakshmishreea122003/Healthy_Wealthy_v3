# Healthy_Wealthy_v3

Unlock Your Healthy Wealth with MongoDB Atlas, AI, LLM, and CV: Your Personalized Health Assistant!

## How to try out this project
- git clone the repo
- open the project in the IDE
- in the files that fetch data from the MongoDB Atlas make the required changes in the line 'mongo_uri = "mongodb+srv://<username>:<password>@<cluster_url>/<database_name>?retryWrites=true&w=majority" '
- in the terminal type 'streamlit run <path to the Home.py file>'

## Inspiration
The inspiration behind creating the Healthy Wealthy app stemmed from the frustration of waiting in clinics for extended periods to access health professionals and the high costs associated with their services. Recognizing the importance of prioritizing health and not ignoring any health concerns, the need for a solution became evident. The app aims to address these challenges and be a go-to resource for mental health support, healthy eating guidance, exercise advice, and instant access to medical perspectives. By harnessing the power of AI, the app empowers individuals to take charge of their health anywhere, anytime, making health truly wealth.

## What it does
Healthy Wealthy is an AI-powered app utilizing MongoDB Atlas, Computer Vision (CV) and Language Model (LLM) to empower users with health and wellness insights. It detects health issues in X-ray scans, guides healthy eating, plans diets, suggests wholesome shopping options, provides emotion-based mental health support, acts as an AI exercise coach, tracks exercise moves, corrects pose estimation, checks for proper gestures, generates summaries of medical reports, and much more.

-AI Dr = The AI Dr. app uses MongoDB Atlas to get the personalised info about the patient, Language Model to provide instant health insights, addressing users' doubts and summarizing complex medical reports. Empowering individuals with accessible, AI-driven healthcare support and informed decision-making.
-Disease Detection🔍 = IT uses MongoDB Atlas to get the personalised info about the person .Here patients can upload X-ray scan images to check for diseases like pneumonia, using AI-powered algorithms to aid in accurate diagnosis and timely medical assistance.
-Daily Diet Planner🥗📅 = uses MongoDB Atlas to get the personalised info about the person . Here users can input their diet preferences, including calorie goals and cuisine choices, to receive a comprehensive daily meal plan for breakfast, lunch, and dinner. Additionally, they can seek healthy snack suggestions to curb cravings effectively.
-MoodBoost Companion 🌞🌈 = uses MongoDB Atlas to get the personalized info about the person. It is an all-in-one mental health support app powered by advanced emotion detection technology and Language Model (LLM) capabilities. It compassionately identifies users' emotions and offers personalized messages and uplifting quotes to promote emotional well-being, providing timely mental health assistance and fostering a positive mindset.
-NutriGuide 🥦 = NutriGuide empowers users with an AI-driven culinary companion, offering expert health perspectives on food-related queries. From understanding sugar's impact on diabetes to discovering nutritious alternatives and calorie insights, explore a world of healthier, delectable options for a balanced lifestyle.
-NutriScan 🍎🔍 = NutriScan revolutionizes your food choices with instant real-time detection of healthy options. Whether you're shopping or in the kitchen, NutriScan analyzes food items, providing detailed insights into their nutritional value. Empower yourself to make informed decisions, fostering a healthier and wealthier lifestyle.

## How we built it
This project uses MongoDB Atlas, AI, CV, LLM and Streamlit
-MongoDB Atlas to get the users info
-Streamlit - it is used to build the web app.
-CV = it is used for image processing and real time video processing
-llm = it is used to chat with patients, provide aditional info, give summary and a lot more.

## Challenges we ran into
Since it was my first time working with MongoDB Atlas learning the queries and doing the project simultaneously was challenging
It was challenging to integrate computer vision with llm. Since I am in my initial stage of learning streamlit , making the project was challenging. To build an app for patients in an interactive manner was challenging.

## Accomplishments that we're proud of
-Use MOngoDB Atlas to get the personalised info of the users
-Detect the diseases by processing the xray scans
provide nutritional guidance to patients
-AI Doctor for all time support to patients.
-Use AI for the good of all
-Make attempt to enable health care be accessible to all ## What we learned
-I learnt to use MOngoDB Atlas
-I learnt to use NoSQL in AI projects
-I learnt how to use streamlit learnt to use LLM in my projects Integrate CV with LLM

## What we learned

## What's next for Healthy Wealthy
As of now it is able to detect only diseases like pneumonia, I want to make sure the model can detect a lot more diseases like tumors and more.
I want to include Ai exercise coach. This coach should be able to check if the exercise poses are correct. Provide proper exercise schedules for users.


  
