import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="movein2.com", layout="centered")

# Custom CSS to style the page
st.markdown(
    """
    <style>
        .center {
            display: flex;
            justify-content: center;
            font-size: 50px;
            color: #003366;
        }
        .description {
            font-size: 16px;
            color: #606060;
            margin-bottom: 20px;
        }
        .footer {
            font-size: 10px;
            color: grey;
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Heading
st.markdown("<div class='center'>movein2.com</div>", unsafe_allow_html=True)

# Subheading
st.subheader("Type your address")

# Initialize session state for address input
if "address" not in st.session_state:
    st.session_state["address"] = ""

# Input field for the address
address = st.text_input("Enter the address", st.session_state["address"])

# Display API functionality description
st.markdown(
    "<div class='description'>This will display the nearest Education Institutions, Transportations and Nearby Shops along with their distance details.</div>",
    unsafe_allow_html=True,
)

# Button to submit the address
if st.button("Submit"):
    if address:  # Ensure the input field is not empty
        # Send POST request to the API
        url = "https://2owawgyt71.execute-api.us-east-1.amazonaws.com/dev/blog-generation"
        data = {"blog_topic": address}
        
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            # Display results from the API
            st.write("Here are the nearest Education Institutions, Transportations and Nearby Shops along with their distances from the address:")
            st.write(result)
        else:
            st.error("Error: Unable to fetch data. Please try again.")
        
        # Clear the input field after submission
        st.session_state["address"] = ""
    else:
        st.warning("Please enter an address.")

# Footer
st.markdown("<div class='footer'><span style='font-size: 14px;'>Build by movein2 team</span></div>", unsafe_allow_html=True)
