import streamlit as st
import time

st.set_page_config(page_title="CivicCompass Pro Bono AI", layout="wide", initial_sidebar_state="expanded")

with open('assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #fbcfe8;'>CivicCompass</h2>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Navigation", ["✨ Dashboard", "🏛️ IRS Formation", "📊 Grant Audits", "💬 CivicBot AI"])
    st.markdown("---")
    st.write("**Account:** Enterprise Non-Profit")
    st.write("**Server:** Active (Node 4)")
    st.caption("Native Claim Firm Open Justice")

if page == "✨ Dashboard":
    st.markdown('<div class="main-title">CivicCompass AI</div>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #94a3b8; font-weight: 300;">Advanced Public Sector Intelligence</h3>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Nonprofits Assisted", value="1,204", delta="+12")
    col2.metric(label="Grants Audited", value="$4.2M", delta="+$250k")
    col3.metric(label="Pro Bono Hours", value="45,000+", delta="Active")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('''<div class="glass-card">
        <h4 class="accent-text">🚀 Automated Paralegal Tools</h4>
        <p>CivicCompass uses advanced machine learning to parse federal CFR guidelines, state statutes, and IRS tax codes to generate start-to-finish compliance matrixes for public service organizations.</p>
    </div>''', unsafe_allow_html=True)

elif page == "🏛️ IRS Formation":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Tax-Exempt Formation Toolkit")
    st.write("Complete the checklist to generate an automated IRS Form 1023 logic map.")
    
    st.markdown("<h5 class='accent-text'>Step 1: State Incorporation</h5>", unsafe_allow_html=True)
    st.write("Draft Articles of Incorporation including the IRS Purpose Clause and Dissolution Clause.")
    
    st.markdown("<h5 class='accent-text'>Step 2: Bylaws & Governance</h5>", unsafe_allow_html=True)
    st.write("Ensure your Conflict of Interest Policy is ratified by the Board of Directors.")
    
    if st.button("Generate Formation Map"):
        st.success("Securely generating PDF toolkit...")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📊 Grant Audits":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("GovGrant Compliance Matrix")
    
    grant_type = st.selectbox("Select Federal Funding Framework:", [
        "HUD Community Development Block Grant", 
        "FEMA Disaster Relief", 
        "DOJ Justice Assistance Grant"
    ])
    
    if st.button("Execute Matrix Audit"):
        with st.spinner("Compiling 2 CFR Part 200 data..."):
            time.sleep(1.5)
        st.markdown(f"<ul><li><b>Uniform Guidance:</b> Subject to Single Audit Act requirements.</li><li><b>SF-425:</b> Quarterly financial reporting mandatory.</li><li><b>Davis-Bacon Act:</b> Prevailing wage enforcement required for sub-contractors.</li></ul>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "💬 CivicBot AI":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("CivicBot: Compliance Neural Net")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Initializing CivicBot Node... How can I assist your organization today?"}]
        
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("E.g., What are the rules for Form 990-N?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = "Accessing federal tax matrices... To file Form 990-N (e-Postcard), your organization's gross receipts must normally be $50,000 or less."
            
            full_response = ""
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.04)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.markdown('</div>', unsafe_allow_html=True)
