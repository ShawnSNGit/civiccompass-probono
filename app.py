import streamlit as st
import time

st.set_page_config(page_title="CivicCompass Pro Bono AI", layout="centered")

st.markdown("""
<style>
    .header { font-family: 'Helvetica Neue', sans-serif; color: #0284C7; font-size: 2.8rem; font-weight: bold; text-align: center; margin-bottom: 0px; }
    .subheader { text-align: center; color: #475569; font-size: 1.2rem; margin-bottom: 2rem; margin-top: 5px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">CivicCompass Pro Bono AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">The Native Claim Firm | Public Service Initiative</div>', unsafe_allow_html=True)

st.info("🌍 **Mission:** Empowering nonprofits, charities, and public service organizations with free, automated paralegal guidance from start to finish.")

tab1, tab2, tab3 = st.tabs(["🏛️ 501(c)(3) Formation", "📊 Annual IRS Compliance", "📝 GovGrant Paralegal"])

with tab1:
    st.subheader("IRS 501(c)(3) Tax-Exempt Formation Guide")
    st.write("A step-by-step paralegal checklist to forming your public charity and securing tax-exempt status.")
    st.write("**1. Incorporate at the State Level:** File Articles of Incorporation as a nonprofit in your state. Ensure you include IRS-mandated language (Specific Purpose and Dissolution clauses).")
    st.write("**2. Obtain an EIN:** Apply for an Employer Identification Number via the IRS website.")
    st.write("**3. Draft Bylaws & Conflict of Interest Policy:** The board of directors must officially adopt these governing documents at their first meeting.")
    st.write("**4. File IRS Form 1023 or 1023-EZ:** Submit the application for Recognition of Exemption under Section 501(c)(3) via Pay.gov. The EZ form is available for organizations projecting under $50,000 in annual gross receipts.")
    if st.button("Generate Document Checklist (PDF)"):
        st.success("Drafting checklist... (Includes: Articles, Bylaws, EIN, Form 1023, State Filing Fees).")

with tab2:
    st.subheader("Filing Annual Returns (Form 990)")
    st.write("Maintaining your tax-exempt status requires strict annual reporting to the IRS and your State Attorney General.")
    st.write("Depending on your organization's financials, you must file one of the following by the 15th day of the 5th month after your accounting period ends:")
    st.write("- **Form 990-N (e-Postcard):** For nonprofits with gross receipts normally ≤ $50,000.")
    st.write("- **Form 990-EZ:** For gross receipts < $200,000 and total assets < $500,000.")
    st.write("- **Form 990 (Full):** For gross receipts ≥ $200,000 or total assets ≥ $500,000.")
    st.write("- **State Registration:** Don't forget to renew your state Charitable Solicitation registration annually before legally soliciting public donations.")
    st.error("⚠️ **Warning:** Failure to file the 990 for three consecutive years results in automatic revocation of tax-exempt status by the IRS.")

with tab3:
    st.subheader("GovGrant Compliance Paralegal")
    st.write("Navigate complex federal grant compliance and state auditing rules.")
    grant_type = st.selectbox("Select Funding Category:", [
        "HUD Community Development Block Grant (CDBG)", 
        "FEMA Disaster Relief", 
        "DOJ Justice Assistance Grant (JAG)"
    ])
    if st.button("Generate Grant Checklist"):
        st.info("Analyzing CFR guidelines...")
        time.sleep(1)
        st.write(f"**Standard Compliance Checklist for {grant_type}:**")
        st.write("- **2 CFR Part 200:** Strict adherence to Uniform Guidance for Federal Awards.")
        st.write("- **SF-425 Reports:** File quarterly Federal Financial Reports.")
        st.write("- **Prevailing Wage:** Maintain Davis-Bacon Act logs if funding public construction.")
        st.write("- **NEPA Review:** Secure environmental clearance prior to committing funds.")

st.markdown("---")
st.caption("CivicCompass is a free public service tool provided by The Native Claim Firm. It is an automated paralegal resource and does not constitute formal legal counsel or certified financial auditing.")
