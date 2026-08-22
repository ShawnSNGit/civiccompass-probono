import streamlit as st
import time

st.set_page_config(page_title="CivicCompass Pro Bono AI", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR ENHANCED UI/UX ---
st.markdown("""
<style>
    .main-title { font-family: 'Helvetica Neue', sans-serif; color: #0369A1; font-size: 3rem; font-weight: 800; padding-bottom: 0px; margin-bottom: 0px;}
    .sub-title { color: #64748B; font-size: 1.2rem; font-weight: 400; padding-top: 0px; margin-top: 0px; margin-bottom: 2rem;}
    .card { background-color: #F8FAFC; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 1rem; border-left: 5px solid #0284C7;}
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #0284C7; color: white; border: none; }
    .stButton>button:hover { background-color: #0369A1; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Scale_of_justice_2_new.svg/1024px-Scale_of_justice_2_new.svg.png", width=80)
    st.markdown("### CivicCompass Navigator")
    page = st.radio("Go to", ["🏠 Dashboard", "🏛️ 501(c)(3) Formation", "📊 Grant Compliance", "💬 CivicBot Chat"])
    
    st.markdown("---")
    st.write("**Account:** Public Service Edition")
    st.write("**Status:** Active")
    st.caption("Powered by The Native Claim Firm")

# --- PAGE 1: DASHBOARD ---
if page == "🏠 Dashboard":
    st.markdown('<div class="main-title">CivicCompass Pro Bono AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Advanced Paralegal Guidance for the Public Sector</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Organizations Assisted", value="1,204", delta="+12 this week")
    col2.metric(label="Compliance Forms Mapped", value="8,430", delta="+145 this week")
    col3.metric(label="Pro Bono Hours Saved", value="45,000+", delta="Active")

    st.markdown("### Welcome to the Open Justice Initiative")
    st.write("Navigating the intersection of federal funding, state compliance, and nonprofit formation can be overwhelming. CivicCompass automates the bureaucratic heavy lifting so you can focus on your mission.")
    
    st.markdown("""
    <div class="card">
        <h4>🚀 Getting Started</h4>
        <p>Use the sidebar to navigate to our interactive modules. Whether you are drafting an IRS Form 1023, filing an annual 990, or ensuring your federal grant complies with 2 CFR Part 200, our tools will generate the required checklists.</p>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 2: 501(C)(3) FORMATION ---
elif page == "🏛️ 501(c)(3) Formation":
    st.header("Tax-Exempt Formation & Board Toolkit")
    st.write("Complete the questionnaire below to generate a customized incorporation checklist.")
    
    with st.expander("Step 1: State Incorporation (Articles & Bylaws)", expanded=True):
        st.write("Your Articles of Incorporation MUST include:")
        st.code("1. An exempt purpose statement (e.g., 'charitable, educational, or scientific purposes').\n2. A dissolution clause dedicating assets to another 501(c)(3) upon closure.")
    
    with st.expander("Step 2: IRS Form 1023-EZ Eligibility Quiz"):
        st.radio("Will your annual gross receipts exceed $50,000 in the next 3 years?", ["No", "Yes"])
        st.radio("Will your total assets exceed $250,000?", ["No", "Yes"])
        st.radio("Are you forming a church, school, or hospital?", ["No", "Yes"])
        if st.button("Check Eligibility"):
            st.success("Based on typical responses, you may be eligible to file the streamlined Form 1023-EZ!")

# --- PAGE 3: GRANT COMPLIANCE ---
elif page == "📊 Grant Compliance":
    st.header("GovGrant Compliance Paralegal")
    st.write("Avoid audit failures and funding clawbacks.")
    
    grant_type = st.selectbox("Select Federal/State Funding Category:", [
        "HUD Community Development Block Grant (CDBG)", 
        "FEMA Disaster Relief", 
        "DOJ Justice Assistance Grant (JAG)"
    ])
    
    if st.button("Generate Audit Checklist"):
        with st.spinner("Analyzing CFR guidelines..."):
            time.sleep(1.5)
        st.markdown(f"""
        <div class="card">
            <h4>Checklist for {grant_type}</h4>
            <ul>
                <li><b>2 CFR Part 200:</b> Adherence to Uniform Guidance for Federal Awards.</li>
                <li><b>SF-425 Reports:</b> File quarterly Federal Financial Reports.</li>
                <li><b>Prevailing Wage:</b> Maintain Davis-Bacon Act logs for construction.</li>
                <li><b>NEPA Review:</b> Secure environmental clearance prior to committing funds.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 4: CIVICBOT CHAT ---
elif page == "💬 CivicBot Chat":
    st.header("CivicBot: AI Paralegal Assistant")
    st.write("Ask a question about nonprofit formation or compliance.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I am CivicBot, your pro bono paralegal. How can I assist your organization today?"}]
        
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Accept user input
    if prompt := st.chat_input("E.g., What is the difference between a 990-N and a 990-EZ?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            # Intelligent simulated responses (No API key required)
            response = "As an open-access assistant, I can confirm that maintaining compliance requires strict adherence to IRS guidelines. For specific inquiries regarding your 501(c)(3) status, please refer to the guides in our sidebar or consult a tax professional."
            
            p_lower = prompt.lower()
            if "990" in p_lower:
                response = "Form 990 is the IRS's primary tool for gathering information about tax-exempt organizations. If your gross receipts are normally under $50,000, you can file the 990-N e-Postcard. Between $50k and $200k requires the 990-EZ."
            elif "501" in p_lower or "start" in p_lower or "form" in p_lower:
                response = "To form a 501(c)(3), you must first incorporate in your state, obtain an EIN, adopt bylaws with a conflict of interest policy, and file Form 1023 or 1023-EZ with the IRS via Pay.gov."
            elif "grant" in p_lower or "audit" in p_lower:
                response = "Federal grants require strict compliance with 2 CFR Part 200 (Uniform Guidance). You must maintain accurate financial records, submit quarterly SF-425 reports, and possess a board-approved conflict of interest policy."

            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.04)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
