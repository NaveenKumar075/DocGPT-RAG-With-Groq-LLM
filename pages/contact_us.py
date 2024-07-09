import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
)

st.write("# Welcome to My Profile! 👋")

# Define CSS for profile card layout
st.markdown(
    """
    <style>
    .profile-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    .profile-card {
        display: flex;
        flex-direction: column; /* Arrange content in a column layout */
        align-items: center;
        justify-content: flex-start;
        border: 1px solid #262730; /* Border color */
        border-radius: 10px;
        padding: 20px;
        width: 45%;
        margin: 10px;
        transition: box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #262730; /* Card background color */
        color: #ffffff; /* Text color */
    }
    .profile-card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        transform: translateY(-5px); /* Adjust hover effect */
    }
    .circle-img {
        border-radius: 50%;
        width: 150px; /* Adjust image size */
        height: 150px; /* Adjust image size */
        object-fit: cover;
        margin-bottom: 20px; /* Add spacing between image and content */
    }
    .profile-info {
        text-align: center; /* Center align profile information */
    }
    .profile-name {
        font-size: 1.5em;
        margin: 0;
    }
    .profile-links {
        display: flex;
        align-items: center;
        justify-content: center; /* Center align links */
        margin-top: 10px;
    }
    .profile-links a {
        display: inline-block;
        margin-right: 10px;
    }
    .profile-links img {
        width: 25px;
        height: 25px;
        margin-right: 5px;
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
            <img src="https://imgur.com/a/rm3FngG" alt="Profile Picture 1" class="circle-img">
            <div class="profile-info">
                <p class="profile-name">Jothika R</p>
                <p>Hey there, I'm Jothika, aspiring ML Engineer, with nearly a year experience in data, passionate about AI, Gen AI, and LLM, eager to create impactful projects!</p>
                <div class="profile-links">
                    <a href="https://www.linkedin.com/in/jothika-r/" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png" alt="LinkedIn" title="LinkedIn">
                    </a>
                    <a href="https://github.com/jothikar" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" title="GitHub">
                    </a>
                </div>
            </div>
        </div>
        <div class="profile-card">
            <img src="https://via.placeholder.com/150" alt="Profile Picture 2" class="circle-img">
            <div class="profile-info">
                <p class="profile-name">Naveen Kumar S</p>
                <p>Hey there, I'm Naveen, aspiring ML Engineer, with nearly a year experience in data, passionate about AI, Gen AI, and LLM, eager to create impactful projects!</p>
                <div class="profile-links">
                    <a href="https://www.linkedin.com/in/naveenkumar/" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png" alt="LinkedIn" title="LinkedIn">
                    </a>
                    <a href="https://github.com/naveenkumar" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" title="GitHub">
                    </a>
                </div>
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
            sender_email = "naveenkumarmusiq@gmail.com"
            sender_password = "cjjntqmlfaretnvl"
            recipient_email = "docgptrag@gmail.com"

            cc = ['jothika.r2031@gmail.com', 'friendschannel007@gmail.com']

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
            server.sendmail(sender_email, [recipient_email] + cc, text)
            server.quit()

            st.success("Thank you for your feedback! Your message has been sent :)")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please fill out all fields in the feedback form.")
