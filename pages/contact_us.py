import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
)

st.write("# Welcome to My Profile! 👋")

# CSS to create a circular image
st.markdown(
    """
    <style>
    .circle-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
    }
    .center-text {
        text-align: center;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Display circular image
st.markdown(
    """
    <img src="https://via.placeholder.com/150" alt="Profile Picture" class="circle-img">
    """, 
    unsafe_allow_html=True
)

# Display name below the image
st.markdown(
    """
    <h2 class="center-text">Your Name</h2>
    """, 
    unsafe_allow_html=True
)

# Add a link
st.markdown(
    """
    <div class="profile-container">
        <div class="profile-item">
            <img src="https://via.placeholder.com/150" alt="Profile Picture 1" class="circle-img">
            <h2>Your Name 1</h2>
            <div><a href="https://your-link-1.com" target="_blank">Your Link 1</a></div>
        </div>
        <div class="profile-item">
            <img src="https://via.placeholder.com/150" alt="Profile Picture 2" class="circle-img">
            <h2>Your Name 2</h2>
            <div><a href="https://your-link-2.com" target="_blank">Your Link 2</a></div>
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
    st.success("Thank you for your feedback :)")
