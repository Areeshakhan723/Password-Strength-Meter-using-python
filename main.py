import streamlit as st
import re

# Set page configuration
st.set_page_config(page_title="Password stength", page_icon="🔐", layout="centered")

# Custom CSS for styling the app
st.markdown(
    """
    <style>
        .stApp{
            background: #082032;
            color:white;
        }

        div.stButton > button {
            background: #E53888;
            color:white;
            border:none;
            transition: 0.3s;
            padding: 10px 20px;
            font-weight:bold;
        }

        div.stButton > button:hover{
            color: white;
            transform : scale(1.05);
            font-size : 18px;
            font-weight: 900;
        }
        .custom-label {
            color: white;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to Password Strength Checker 🔐")

# Welcome message
st.write(
    """
    🛡️ **Protect your accounts with strong passwords!**  
    Use this tool to check the strength of your password and get tips to make it more secure.  
    A strong password should include:
    - At least **8 characters**
    - A mix of **uppercase (A-Z)** and **lowercase (a-z)** letters
    - At least **one number (0-9)**
    - At least **one special character (!@#$%^&*)**
    """
)

# Function to check password strength
def password_generator(password):
    score = 0  # Initialize score
    feedback = []  # List to store feedback messages


    # Length check
    if  len(password) >= 8:
        score += 1
    else:
        feedback.append(f"❌ **Length:** Your password should be at least 8 characters long.")

    # Uppercase and lowercase check
    if  re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ **Case Sensitivity:** Include both uppercase (A-Z) and lowercase (a-z) letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ **Numbers:** Add at least one number (0-9) to your password.")

    # Special character check
    if re.search(r"[(!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ **Special Characters:** Include at least one special character (!@#$%^&*).")

    # Strength rating
    if score == 4:
        st.success("###### ✅ **Strong Password!** Your password meets all the security requirements.")
    elif score == 3:
        st.info("###### ⚠️ **Moderate Password:** Your password is decent, but it could be stronger. Consider adding more security features.")
    else:
        st.error("###### ❌ **Weak Password:** Your password does not meet the minimum security requirements. Please improve it using the suggestions below.")

    # Display feedback in an expander
    if feedback:
        with st.expander("🔍 **Tips to Improve Your Password**"):
            for items in feedback:
             st.markdown(items)

# Get user input
st.markdown('<div class="custom-label">🔐 Enter Your Password</div>', unsafe_allow_html=True)
password = st.text_input( 
    "",  # Empty label (using custom HTML for the label)
    type="password",  # Hide input characters
    help="Ensure your password is strong! 🔐",  # Help text
    placeholder="Type your password here..."  # Placeholder text
    )

# Check password strength on button click
if st.button("Check Strength"):
    if password:
        password_generator(password)    
    else:
       st.warning("⚠️ **Please enter a password first!**")

