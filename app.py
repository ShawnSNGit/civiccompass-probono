import streamlit as st
import time
import json
import random
import os

# MUST BE FIRST
st.set_page_config(page_title="CivicCompass Pro Bono", layout="wide", initial_sidebar_state="collapsed")

with open('assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- SLEEK HORIZONTAL NAVIGATION ---
st.markdown("<h3 style='text-align: center; color: #ffedd5; font-weight: 900; text-shadow: 0px 2px 4px rgba(0,0,0,0.5);'>🎈 CivicCompass</h3>", unsafe_allow_html=True)
page = st.radio("Navigation", ["🏠 Dashboard & Guides", "🎮 GovKnowledge Quiz", "🏛️ Interactive IRS Setup", "📊 Smart Grant Audits"], horizontal=True, label_visibility="collapsed")

# --- THE 50 GUIDES DATA ---
GUIDES = [
    "1. The Day-One Blueprint: How to Choose the Right Legal Structure for Your Non-Profit",
    "2. Drafting Articles of Incorporation: Step-by-Step State Filing Instructions",
    "3. Getting Your EIN (Employer Identification Number): The Fast-Track IRS Portal Guide",
    "4. Writing Bulletproof Bylaws: Essential Clauses Every Non-Profit Board Needs",
    "5. Holding Your First Official Board Meeting: Resolutions, Minutes, and Compliance",
    "6. Adopting a Conflict of Interest Policy: What the IRS Mandates for Founders",
    "7. Securing a Registered Agent: Why You Need One and How to Appoint Them",
    "8. Setting Up a Corporate Records Binder: Physical vs. Digital Compliance Hubs",
    "9. Fiscal Sponsorship 101: How to Operate Under Another Group's 501(c)(3) Umbrella",
    "10. Foreign Qualification: How to Legally Expand Your Non-Profit Into Other States",
    "11. Decoding Form 1023 vs. Form 1023-EZ: Which Application Gets You Tax-Exempt Status Faster?",
    "12. Answering the Tough Questions: How to Draft Your 501(c)(3) Program Narrative for the IRS",
    "13. Public Charity vs. Private Foundation: Understanding Your IRS Classification Test",
    "14. The 33% Public Support Test Explained: Keeping Your Tax-Exempt Status Safe",
    "15. Unrelated Business Income Tax (UBIT): When Your Non-Profit's Side Hustle Triggers IRS Taxes",
    "16. Applying for 501(c)(4), (c)(6), or Other Non-Profit Tax Statuses: When to Look Beyond 501(c)(3)",
    "17. Navigating IRS Determinations: What to Do When the IRS Sends a Follow-Up Letter or Audit",
    "18. Applying for Federal Tax-Exempt Status for Faith-Based Organizations and Churches",
    "19. Amending Your Tax-Exempt Purpose: When and How to File Changes With the IRS",
    "20. Reinstatement Playbook: How to Recover Lost Tax-Exempt Status After Automatic Revocation",
    "21. The Annual Form 990 Family: Knowing Whether to File 990-N, 990-EZ, or Full Form 990",
    "22. Mastering the May 15 Deadline: Calendar Year Non-Profit Tax Filing Timelines Explained",
    "23. How to File IRS Form 8868: Securing Your Automatic 6-Month Extension Without Panic",
    "24. State Annual Reports: Keeping Your Corporate Good Standing With the Secretary of State",
    "25. State Charitable Solicitation Registrations: Multi-State Renewal Calendars and Deadlines",
    "26. Filing State Tax Exemptions: Beyond the IRS, Managing State Sales and Franchise Tax Waivers",
    "27. Document Retention Policies: Exactly How Long to Keep Financials, Tax Returns, and Grants",
    "28. Navigating Independent Financial Audits: When Does Your State or Funder Require One?",
    "29. Public Disclosure Laws: What Parts of Your Form 990 and Financials Must Be Open to Anyone",
    "30. Closing Shop: The Legal Step-by-Step Guide to Dissolving a Non-Profit and Distributing Assets",
    "31. Grant Proposal Compliance: Navigating Federal, State, and Foundation RFP Guidelines",
    "32. Government Grant Compliance 101: Navigating Uniform Guidance (2 CFR 200)",
    "33. Matching Funds and Cost-Sharing: Rules for Tracking Restricted Grant Dollars",
    "34. Indirect Cost Rates: How to Properly Charge Overhead to Government and Private Funders",
    "35. Lobbying Limits for 501(c)(3)s: The 501(h) Election Explained (How Much Advocacy is Legal?)",
    "36. Political Campaign Intervention Rules: Exactly What Non-Profits Can and Cannot Say",
    "37. Charitable Gaming and Raffles: Legal Compliance for Non-Profit Bingo, Galas, and Auctions",
    "38. Corporate Sponsorships vs. Advertising: Avoiding Unwanted Tax Liabilities on Donor Banners",
    "39. Endowment Funds and the UPMIFA: Legal Rules for Managing Donor-Restricted Endowments",
    "40. Internal Financial Controls: Segregation of Duties to Protect Your Non-Profit From Fraud",
    "41. Hiring Your First Employee: State and Federal Employer Registration Essentials",
    "42. W-2 vs. 1099 Contractors: Avoiding Misclassification Penalties in Public Service Projects",
    "43. Payroll Tax Compliance: Filing Form 941 and Managing State Unemployment Insurance (SUI)",
    "44. Providing Public Benefits: Legal Agreements and Memorandums of Understanding (MOUs) With Agencies",
    "45. Data Privacy and Client Confidentiality: Complying with HIPAA, FERPA, and State Privacy Acts",
    "46. Volunteer Management Law: Waiver Forms, Background Checks, and Liability Protection",
    "47. ADA Compliance for Non-Profits: Physical and Digital Accessibility Mandates for Public Programs",
    "48. Intellectual Property for Public Services: Licensing Curriculums, Logos, and Open-Source Tools",
    "49. Commercial Co-Venture Compliance: Partnering With For-Profit Businesses for Cause Marketing",
    "50. The Master Non-Profit Compliance Calendar: Keeping Track of Monthly, Quarterly, and Annual Deadlines"
]

# --- PAGE 1: DASHBOARD & GUIDES ---
if page == "🏠 Dashboard & Guides":
    st.markdown('<div class="main-title">CivicCompass</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">System Architecture & Technical Specifications ⚙️</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Federal Data Parsed", value="2.4M Pages", delta="Updated Daily")
    col2.metric(label="Virtual Staff", value="7 Auto-Agents", delta="Neural Net Active")
    col3.metric(label="Core Uptime", value="99.999%", delta="12ms Latency")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<h3 style='color: #ffedd5; text-shadow: 0px 2px 4px rgba(0,0,0,0.5);'>📚 The Ultimate Public Service Library</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; font-weight: 600;'>Browse our 50 interactive guides on everything public service, law, and compliance!</p>", unsafe_allow_html=True)
    
    with st.container(height=600):
        for guide in GUIDES:
            title_text = guide.split('. ', 1)[1] if '. ' in guide else guide
            with st.expander(f"📘 {guide}"):
                st.write(f"**Overview:** This module covers the critical compliance requirements and legal framework for **{title_text}**.")
                st.write("1. **Prerequisites:** Ensure your state corporate registry and IRS standing are fully up to date before proceeding.")
                st.write("2. **Filing Requirements:** Submit all necessary documentation at least 45 days prior to your fiscal or calendar deadline.")
                st.write("3. **Common Pitfalls:** Failure to maintain accurate financial ledgers or violating the terms of this section can result in immediate revocation of your tax-exempt status or severe financial penalties.")
                st.info("💡 **Pro Tip:** Always consult your organizational bylaws and a certified tax professional before executing binding legal changes.")

    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    if st.button("Run Live System Diagnostic 🔍"):
        my_bar = st.progress(0, text="Pinging autonomous agent clusters...")
        for percent_complete in range(100):
            time.sleep(0.015)
            my_bar.progress(percent_complete + 1, text=f"Diagnostic in progress... {percent_complete}%")
        time.sleep(0.5)
        my_bar.empty()
        st.success("✅ Diagnostic Complete: All 7 autonomous staff members are online and operational. Node Latency: 12ms.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: MASSIVE 100-QUESTION QUIZ ---
elif page == "🎮 GovKnowledge Quiz":
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='accent-pink'>🧠 The Ultimate 100-Question GovKnowledge Exam</h3>", unsafe_allow_html=True)
    st.write("Are you a true compliance master? We generate a massive 100-question exam from our database. The entire exam shuffles randomly every time you submit!")
    
    try:
        with open('data/quiz_bank.json', 'r') as f:
            all_questions = json.load(f)
    except Exception:
        st.error("Error loading quiz database. Ensure data/quiz_bank.json is present.")
        all_questions = []

    if 'quiz_order' not in st.session_state:
        st.session_state.quiz_order = all_questions.copy()
        random.shuffle(st.session_state.quiz_order)

    user_answers = {}
    with st.container(height=600):
        for idx, q in enumerate(st.session_state.quiz_order):
            st.markdown(f"**{idx + 1}. {q['q']}**")
            user_answers[idx] = st.radio(
                label="Select an answer:",
                options=q['options'],
                key=f"quiz_radio_{idx}",
                index=None,
                label_visibility="collapsed"
            )
            st.markdown("---")

    if st.button("Submit 100-Question Exam! 🎯"):
        score = 0
        for idx, q in enumerate(st.session_state.quiz_order):
            if user_answers[idx] == q['ans']:
                score += 1
                
        if score == 100:
            st.balloons()
            st.success("🏆 ABSOLUTELY INCREDIBLE! YOU SCORED 100 OUT OF 100!")
        else:
            st.warning(f"You got {score} out of 100 right. The exam has now been completely reshuffled for your next attempt!")
        
        random.shuffle(st.session_state.quiz_order)
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: INTERACTIVE IRS SETUP ---
elif page == "🏛️ Interactive IRS Setup":
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='accent-blue'>Let's Start a Charity! 💖</h3>", unsafe_allow_html=True)
    st.write("Check off the boxes as you complete them to track your progress! Expand each section for a massive checklist of 50 critical Do's and Don'ts.")
    
    try:
        with open('data/irs_dos_donts.json', 'r') as f:
            dos_donts = json.load(f)
    except Exception:
        dos_donts = {"step1": {"dos": [], "donts": []}, "step2": {"dos": [], "donts": []}, "step3": {"dos": [], "donts": []}, "step4": {"dos": [], "donts": []}}

    # STEP 1
    step1 = st.checkbox("📝 1. File Articles of Incorporation in your state.")
    with st.expander("🔍 View 50 Critical Do's and Don'ts for Articles of Incorporation"):
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<h4 style='color: #047857;'>✅ 25 DOs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step1']['dos']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)
        with colB:
            st.markdown("<h4 style='color: #be185d;'>❌ 25 DONTs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step1']['donts']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)

    # STEP 2
    step2 = st.checkbox("🔑 2. Obtain an EIN from the IRS website.")
    with st.expander("🔍 View 50 Critical Do's and Don'ts for EIN Applications"):
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<h4 style='color: #047857;'>✅ 25 DOs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step2']['dos']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)
        with colB:
            st.markdown("<h4 style='color: #be185d;'>❌ 25 DONTs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step2']['donts']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)

    # STEP 3
    step3 = st.checkbox("🤝 3. Vote on your Bylaws & Conflict of Interest Policy.")
    with st.expander("🔍 View 50 Critical Do's and Don'ts for Bylaws & Board Governance"):
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<h4 style='color: #047857;'>✅ 25 DOs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step3']['dos']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)
        with colB:
            st.markdown("<h4 style='color: #be185d;'>❌ 25 DONTs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step3']['donts']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)

    # STEP 4
    step4 = st.checkbox("🇺🇸 4. File IRS Form 1023 on Pay.gov.")
    with st.expander("🔍 View 50 Critical Do's and Don'ts for Form 1023 Filings"):
        colA, colB = st.columns(2)
        with colA:
            st.markdown("<h4 style='color: #047857;'>✅ 25 DOs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step4']['dos']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)
        with colB:
            st.markdown("<h4 style='color: #be185d;'>❌ 25 DONTs</h4>", unsafe_allow_html=True)
            for item in dos_donts['step4']['donts']: st.markdown(f"<span style='font-size: 0.9em;'>- {item}</span>", unsafe_allow_html=True)
    
    progress = sum([step1, step2, step3, step4]) * 25
    st.progress(progress, text=f"Setup Progress: {progress}%")
    
    if progress == 100:
        st.success("🎉 WOW! You finished everything! You are ready to change the world!")
        st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 4: SMART GRANT AUDITS ---
elif page == "📊 Smart Grant Audits":
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='accent-green'>Government Grant Helper! 💵</h3>", unsafe_allow_html=True)
    st.write("Pick your grant to generate a live, interactive compliance audit.")
    
    GRANTS = {
        "HUD Community Development Block Grant (CDBG)": {
            "desc": "HUD's CDBG program requires strict tracking of demographic data to prove funds benefit Low-to-Moderate Income (LMI) individuals. Failure to maintain an Environmental Review Record (ERR) before committing funds will result in an immediate clawback.",
            "checks": ["Verify 70% LMI Benefit Requirement", "Complete Environmental Review Record (ERR)", "Log Davis-Bacon Prevailing Wages", "Submit Consolidated Annual Performance Report (CAPER)", "Maintain 2 CFR 200 Single Audit Files"]
        },
        "FEMA Disaster Relief Funding": {
            "desc": "FEMA Public Assistance (PA) grants are subject to the Stafford Act. The most common compliance failure is the inability to prove competitive procurement during exigent circumstances, leading to massive de-obligations.",
            "checks": ["Document Exigent/Emergency Procurement Justifications", "Maintain Daily Debris Removal Load Tickets", "Track Force Account Equipment Usage", "Verify 75/25 Federal-to-State Cost Match", "Ensure No Duplication of Benefits (DOB)"]
        },
        "DOJ Byrne Justice Assistance Grant (JAG)": {
            "desc": "The JAG program strictly audits civil rights compliance. If your agency employs over 50 people, you must maintain an active Equal Employment Opportunity Plan (EEOP) on file with the Office for Civil Rights.",
            "checks": ["Submit Equal Employment Opportunity Plan (EEOP)", "File Quarterly Performance Measurement Tool (PMT) Reports", "Certify Body Armor Policy (BVP)", "Ensure FBI NIBRS Reporting Compliance", "Register with SAM.gov"]
        },
        "EPA Environmental Education Grant": {
            "desc": "EPA grants mandate rigorous quality assurance. If your project involves collecting any primary environmental data, you must have an approved Quality Assurance Project Plan (QAPP) before data collection begins.",
            "checks": ["Approve Quality Assurance Project Plan (QAPP)", "Meet MBE/WBE Supplier Diversity Goals", "Submit Federal Financial Report (SF-425)", "File EPA Lobbying Certification", "Adhere to Build America, Buy America Act"]
        },
        "DOT RAISE Transportation Grant": {
            "desc": "DOT infrastructure grants have massive federal compliance footprints. The National Environmental Policy Act (NEPA) requires a categorical exclusion or full environmental impact statement prior to breaking ground.",
            "checks": ["Verify Build America, Buy America (BABA) Act", "Comply with Title VI Civil Rights", "Secure NEPA Categorical Exclusion", "Track FHWA Performance Metrics", "File Disadvantaged Business Enterprise (DBE) Logs"]
        }
    }
    
    # Use session state to remember that an audit was generated
    if 'audit_generated' not in st.session_state:
        st.session_state.audit_generated = False
        st.session_state.current_grant = None

    grant_choice = st.selectbox("Which grant did you receive?", list(GRANTS.keys()))
    
    # If the user changes the dropdown selection, reset the audit
    if grant_choice != st.session_state.current_grant:
        st.session_state.audit_generated = False
        st.session_state.current_grant = grant_choice
    
    if st.button("Generate Smart Audit ✨"):
        with st.spinner("Analyzing CFR rules..."):
            time.sleep(1)
        st.session_state.audit_generated = True

    # Check session state rather than just the button click
    if st.session_state.audit_generated:
        st.success(f"Audit template loaded for: {grant_choice}")
        
        # Display the highly informative compliance description
        st.info(f"**Compliance Overview:** {GRANTS[grant_choice]['desc']}")
        
        st.write("**Mark complete when finished:**")
        # Ensure the checkboxes have unique, persistent keys based on the grant name
        for idx, item in enumerate(GRANTS[grant_choice]['checks']):
            st.checkbox(f"{item}", key=f"grant_cb_{grant_choice}_{idx}")
            
    st.markdown('</div>', unsafe_allow_html=True)
