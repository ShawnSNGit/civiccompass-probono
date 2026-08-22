import streamlit as st
import time

st.set_page_config(page_title="GovGrant Compliance Paralegal", layout="centered")

st.markdown("""
<style>
    .header { font-family: 'Helvetica Neue', sans-serif; color: #166534; font-size: 2.2rem; font-weight: bold; text-align: center; margin-bottom: 0px; }
    .subheader { text-align: center; color: #475569; font-size: 1.1rem; margin-bottom: 2rem; margin-top: 5px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">GovGrant Compliance Paralegal</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Public Service Edition: Federal Funding & State Guidelines</div>', unsafe_allow_html=True)

st.info("🏛️ **Our Philanthropic Mission:** We provide this free, automated paralegal tool to help nonprofits, charities, and local municipalities navigate complex federal grant compliance and state auditing rules.")

grant_type = st.selectbox("Select Federal/State Funding Category:", [
    "HUD Community Development Block Grant (CDBG)", 
    "FEMA Disaster Relief Funding", 
    "DOJ Byrne Justice Assistance Grant (JAG)", 
    "HHS Substance Abuse Prevention Block Grant"
])

project_desc = st.text_area("Briefly describe your nonprofit project (for compliance mapping):", height=120)

if st.button("Generate Paralegal Compliance Checklist"):
    st.success("Analyzing CFR guidelines and state auditing standards...")
    time.sleep(2)
    
    st.write(f"### Standard Compliance Checklist for {grant_type}")
    st.write("To avoid funding clawbacks or state audit failures, your organization must maintain the following:")
    st.write("1. **2 CFR Part 200 Compliance:** Strict adherence to the Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards.")
    st.write("2. **Quarterly Financial Reporting:** Submission of standard SF-425 Federal Financial Reports.")
    st.write("3. **Prevailing Wage Logs:** If using funds for construction or public works, ensure Davis-Bacon Act or equivalent state prevailing wage documentation is actively filed.")
    st.write("4. **Environmental Review Records:** (If applicable) NEPA compliance sign-offs must be secured *before* the commitment of funds.")
    st.write("5. **Board-Approved Conflict of Interest Policy:** A documented policy must be on file and signed annually by directors.")
    
    st.markdown("---")
    st.warning("📋 **Disclaimer:** This is a free paralegal outline provided for public service organizations. It is an automated checklist and does not constitute formal legal counsel or certified financial auditing.")

st.caption("A Public Service Resource provided by The Native Claim Firm")
