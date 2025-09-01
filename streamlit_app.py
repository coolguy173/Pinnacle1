import streamlit as st

st.set_page_config(page_title="Pinnacle Investment Advisor", page_icon="💰", layout="centered")

st.title("📊 Pinnacle Investment Advisor")
st.write("Welcome! Let's help you invest smarter based on your salary.")

# Input: Salary
salary = st.number_input("Enter your monthly salary (₹):", min_value=0, step=1000)

# Input: Percentage to invest
percentage = st.slider("What percentage of your salary do you want to invest?", 0, 100, 20)

# Logic: Calculate investment
if salary > 0 and percentage > 0:
    investment = (salary * percentage) / 100

    st.success(f"You should invest ₹{investment:,.2f} every month 💰")

    # Simple suggestion based on risk
    if percentage <= 20:
        st.info("💡 Suggestion: Start safe with mutual funds or fixed deposits.")
    elif percentage <= 40:
        st.info("💡 Suggestion: Mix of mutual funds and index funds.")
    else:
        st.info("💡 Suggestion: Consider higher-risk options like stocks or ETFs for faster growth.")
else:
    st.warning("Please enter a salary and choose a percentage to see recommendations.")
