import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
)

st.write("# Welcome to My Profile! 👋")

st.sidebar.success("Select a demo above.")

# CSS to create a card layout, circular image, and hover effect
st.markdown(
    """
    <style>
    .profile-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .profile-card {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 20px;
        width: 350px;
        margin: 10px;
        transition: box-shadow 0.3s ease;
    }
    .profile-card:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .circle-img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin-right: 20px;
    }
    .profile-info {
        text-align: left;
    }
    .profile-name {
        font-size: 1.5em;
        margin: 0;
    }
    .profile-link {
        color: #1f77b4;
        text-decoration: none;
    }
    .profile-link:hover {
        text-decoration: underline;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Display profile items in card layout
st.markdown(
    """
    <div class="profile-container">
        <div class="profile-card">
            <img src="https://via.placeholder.com/150" alt="Profile Picture 1" class="circle-img">
            <div class="profile-info">
                <p class="profile-name">Your Name 1</p>
                <a href="https://your-link-1.com" target="_blank" class="profile-link">Your Link 1</a>
            </div>
        </div>
        <div class="profile-card">
            <img src="https://via.placeholder.com/150" alt="Profile Picture 2" class="circle-img">
            <div class="profile-info">
                <p class="profile-name">Your Name 2</p>
                <a href="https://your-link-2.com" target="_blank" class="profile-link">Your Link 2</a>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)

# Feedback form
st.markdown("## Feedback Form")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Submit"):
    if name and email and message:
        try:
            sender_email = "your-email@gmail.com"
            sender_password = "your-email-password"
            recipient_email = "recipient-email@gmail.com"

            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = "New Feedback from Streamlit App"
            
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the Gmail SMTP server and send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()

            st.success("Thank you for your feedback! Your message has been sent.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill out all fields in the feedback form.")
