import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Jagadeesh Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
.project-card {
    padding:20px;
    border-radius:15px;
    background-color:#f5f5f5;
    margin-bottom:15px;
}
.skill-box {
    padding:10px;
    border-radius:10px;
    text-align:center;
    background-color:#E8F0FE;
    margin:5px;
}
h1,h2,h3{
    color:#1f77b4;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🚀 Portfolio")

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "About", "Projects", "Skills", "Certificates", "Contact"]
)

if menu == "Home":

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("assets/profile.jpeg", width=250)
    with col2:
        st.title("Jagadeeswar Rallapalli")
        st.subheader("Computer Science Engineering Student")

        st.write("""
        Passionate about:

        ✔ Python Development

        ✔ Machine Learning

        ✔ Data Science

        ✔ Web Development

        ✔ Artificial Intelligence
        """)
        st.success("Seeking Internship & Software Development Opportunities")
        with open("assets/resume.pdf","rb") as pdf:
            st.download_button(
                "📄 Download Resume",
                pdf,
                file_name="Jagadeeswar_Resume.pdf"
            )
elif menu == "About":
    st.header("👨‍💻 About Me")
    st.write("""
    Hello! I am Jagadeesh Rallapalli, a Computer Science Engineering student.

    I enjoy building real-world software solutions using Python,
    Machine Learning, Data Science, and Web Technologies.

    My goal is to become a Data Scientist and pursue
    higher education in the USA.

    I actively work on:
    - Machine Learning Projects
    - Recommendation Systems
    - Data Analysis
    - Artificial Intelligence Applications
    - Python Libraries
    """)
elif menu == "Projects":
    st.header("🚀 Projects")
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("assets/ai_career_chatbot.png")

    with col2:
        st.subheader("AI Career Guidance Chatbot")

        st.write("""
        AI-powered chatbot that provides career guidance,
        skill recommendations, and personalized learning roadmaps.
        """)

        st.write("**Technologies:**")
        st.write("Python, Streamlit, Generative AI")

        st.link_button(
            "GitHub Repository",
            "https://github.com/jagadeesh2006-R/AI-Career-Guidance-Chatbot"
        )
        st.link_button("Live Demo","https://ai-career-guidance-chatbot.streamlit.app")
    st.divider()
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("assets/car_price.png")
    with col2:
        st.subheader("Car Price Prediction System")
        st.write("""
        Machine Learning application that predicts
        vehicle prices using regression algorithms.
        """)
        st.write("**Technologies:**")
        st.write("Python, Pandas, Scikit-Learn, Streamlit")
        st.link_button(
            "GitHub Repository",
            "https://github.com/jagadeesh2006-R/Car-Price-Prediction")
        st.link_button("Live Demo","https://car-price-prediction-projects.streamlit.app")
    st.divider()
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("assets/movie_recommendation.png")
    with col2:
        st.subheader("Movie Recommendation System")
        st.write("""
        Content-based recommendation system
        that suggests movies using similarity scores.
        """)
        st.write("**Technologies:**")
        st.write("Python, Pandas, Streamlit")
        st.link_button(
            "GitHub Repository",
            "https://github.com/jagadeesh2006-R/Movie-Recommendation-System-project"
        )
        st.link_button("Live Demo","https://movie-recommendation-system-projects.streamlit.app")
    st.divider()

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("assets/todo_list.png")

    with col2:
        st.subheader("To-Do List Management Application")

        st.write("""
        Task management application that helps users
        create, update, delete, and track daily tasks efficiently.
        """)

        st.write("**Technologies:**")
        st.write("Python, Streamlit")

        st.link_button(
            "GitHub Repository",
            "https://github.com/jagadeesh2006-R/Smart-Todo-List-App"
        )
        
        st.link_button("Live Demo","https://smart-todo-list.streamlit.app")

elif menu == "Skills":

    st.header("🛠 Technical Skills")

    skills = [
        "Python",
        "Data Analaysis",
        "Machine Learning",
        "Data Science",
        "Pandas",
        "NumPy",
        "Scikit-Learn",
        "MySQL",
        "Git",
        "GitHub",
        "HTML",
        "CSS",
        "PHP",
        "Streamlit",
        "VS Code"
    ]
    cols = st.columns(4)
    for index, skill in enumerate(skills):
        cols[index % 4].success(skill)
elif menu == "Certificates":

    st.header("📜 Certifications")

    st.write("""
    ✔ Data Analytics Internship Certificate

    ✔ Python Programming Certificate

    ✔ Machine Learning Course Certificate

    ✔ Workshop Participation Certificates

    ✔ Online Technical Certifications
    """)
elif menu == "Contact":

    st.header("📞 Contact Me")

    st.write("📧 Email: jagadeeshrallapall148@gmail.com")

    st.write(
        "LinkedIn :https://linkedin.com/in/jagadeeswar-rallapalli-855200282"
    )

    st.write(
        "GitHub :https://github.com/jagadeesh2006-R"
    )

    st.write("📱 Phone: +91-6304343349")

    st.success("Thank you for visiting my portfolio!")