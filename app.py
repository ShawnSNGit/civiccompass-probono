import streamlit as st
import time

st.set_page_config(page_title="Pro Bono Appellate Guide | Open Justice", layout="centered")

st.markdown("""
<style>
    .header { font-family: 'Helvetica Neue', sans-serif; color: #0284C7; font-size: 2.5rem; font-weight: bold; text-align: center; margin-bottom: 0px; }
    .subheader { text-align: center; color: #64748B; font-size: 1.1rem; margin-bottom: 2rem; margin-top: 5px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">Pro Bono Appellate Guide</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Open Justice Initiative: Structural resources for pro bono clinics and pro se litigants.</div>', unsafe_allow_html=True)

st.info("🌍 **Our Mission:** We believe in increasing access to justice. This open-source tool is designed to help underfunded legal clinics and pro se litigants demystify complex state appellate filing requirements.")

court = st.selectbox("Select Jurisdiction to review filing requirements:", ["Ohio Supreme Court", "Georgia Supreme Court", "Texas Supreme Court", "Pennsylvania Supreme Court"])

issue = st.text_area("Briefly describe the legal issue (to map structural constraints):", height=150)

if st.button("Generate Pro Bono Filing Structure"):
    st.success("Mapping local rules and formatting requirements...")
    time.sleep(2)
    
    if "Ohio" in court:
        st.write("### Foundational Filing Structure (Ohio S.Ct.Prac.R.)")
        st.write("To ensure your filing is not rejected by the Clerk's office, it must strictly adhere to the following sequence:")
        st.write("1. **Table of Contents** (Mandatory per Rule 7.02)")
        st.write("2. **Table of Authorities**")
        st.write("3. **Statement of Interest** (If filing as Amicus Curiae)")
        st.write("4. **Law and Argument** (Must be divided by explicit Propositions of Law)")
        st.write("5. **Conclusion**")
        
        st.warning("⚖️ **Public Service Notice:** This open-access sandbox provides baseline procedural outlines to prevent clerk rejections. Substantive legal drafting, adversarial red-teaming, and predictive judicial modeling are restricted to enterprise systems. Please consult retained counsel for substantive litigation.")
    else:
        st.write("### General Appellate Structure")
        st.write("Please consult the local rules of practice for your selected jurisdiction to ensure compliance.")

st.markdown("---")
st.caption("A Public Service Resource provided by The Native Claim Firm")
