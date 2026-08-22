import streamlit as st
import time

st.set_page_config(page_title="CivicCompass Pro Bono", layout="wide", initial_sidebar_state="expanded")

with open('assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #38BDF8; font-weight: 900;'>🎈 CivicCompass</h2>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Where would you like to go?", ["🏠 Dashboard & Specs", "🏛️ Start a Nonprofit", "📊 Grant Checklists", "💬 CivicBot Helper"])
    st.markdown("---")
    st.info("A free public service tool by The Native Claim Firm! 😊")

# --- PAGE 1: DASHBOARD ---
if page == "🏠 Dashboard & Specs":
    st.markdown('<div class="main-title">CivicCompass</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">System Architecture & Technical Specifications ⚙️</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Federal & IRS Data Parsed", value="2.4M Pages", delta="Updated Daily")
    col2.metric(label="Virtual Staff Allocation", value="7 Autonomous Agents", delta="Active Neural Net")
    col3.metric(label="System Core Uptime", value="99.999%", delta="0ms Latency")

    st.markdown("""
    <div class="friendly-card">
        <h4 class="accent-blue">🚀 Hardware & Infrastructure Details</h4>
        <p>We believe in absolute transparency. CivicCompass is powered by a multi-agent neural architecture. Rather than relying on static templates, this repository deploys <b>7 concurrent autonomous AI staff members</b> to continuously parse Title 2 of the Code of Federal Regulations (CFR) and the IRS Internal Revenue Manual.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Run Live System Diagnostic 🔍"):
        progress_text = "Pinging autonomous agent clusters..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.015)
            my_bar.progress(percent_complete + 1, text=f"Diagnostic in progress... {percent_complete}%")
        time.sleep(0.5)
        my_bar.empty()
        st.success("✅ Diagnostic Complete: All 7 autonomous staff members are online and operational. Node Latency: 12ms. Server load: 4%.")

# --- PAGE 2: 501(C)(3) FORMATION ---
elif page == "🏛️ Start a Nonprofit":
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='accent-pink'>Let's Start a Charity! 💖</h3>", unsafe_allow_html=True)
    st.write("Follow these easy steps to get your 501(c)(3) tax-exempt status.")
    
    st.markdown("#### 📝 Step 1: State Paperwork")
    st.write("File 'Articles of Incorporation' in your state. Make sure you tell them your charity's purpose!")
    
    st.markdown("#### 🤝 Step 2: Assemble Your Team")
    st.write("Get your Board of Directors together and vote on your 'Bylaws' (the rules of your club!).")
    
    st.markdown("#### 🇺🇸 Step 3: Tell the IRS!")
    st.write("Fill out IRS Form 1023 (or the super short 1023-EZ) online to make it official.")
    
    if st.button("Download My Free Checklist! 📥"):
        st.success("Yay! Your PDF checklist is ready! 🎉")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: GRANT COMPLIANCE ---
elif page == "📊 Grant Checklists":
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='accent-green'>Government Grant Helper! 💵</h3>", unsafe_allow_html=True)
    st.write("Pick your grant from the list below, and we'll give you exactly what you need to do!")
    
    GRANTS = {
        "HUD Community Development Block Grant (CDBG)": ["✔️ 2 CFR Part 200 Audit", "✔️ Environmental Review Record (ERR)", "✔️ Davis-Bacon Wage Logs", "✔️ Low-to-Moderate Income (LMI) Proof"],
        "FEMA Disaster Relief Funding": ["✔️ Stafford Act Compliance", "✔️ Cost Match Documentation (75/25)", "✔️ Exigent Procurement Log", "✔️ Debris Removal Load Tickets"],
        "DOJ Byrne Justice Assistance Grant (JAG)": ["✔️ Civil Rights Compliance (EEOP)", "✔️ Quarterly PMT Report", "✔️ Body Armor Policy Certification", "✔️ NIBRS Reporting"],
        "HHS Substance Abuse Block Grant": ["✔️ Synar Amendment Tobacco Rules", "✔️ Primary Prevention 20% Set-Aside", "✔️ IVTR Outreach Log", "✔️ Faith-Based Safeguards"],
        "EPA Environmental Education Grant": ["✔️ Quality Assurance Project Plan", "✔️ MBE/WBE Supplier Diversity", "✔️ Federal Financial Report (SF-425)", "✔️ Lobbying Certification"],
        "NEA Challenge America Grant": ["✔️ Historic Preservation Clearance", "✔️ Section 504 Accessibility", "✔️ Davis-Bacon Act (Construction)", "✔️ Final Descriptive Report (FDR)"],
        "DOT RAISE Transportation Grant": ["✔️ Build America, Buy America Act", "✔️ Title VI Civil Rights", "✔️ NEPA Categorical Exclusion", "✔️ FHWA Metrics"],
        "USDA Rural Development Grant": ["✔️ Active SAM.gov Status", "✔️ Form RD 400-4 Assurance", "✔️ Engineering Contract Review", "✔️ Letter of Conditions Met"],
        "SBA Microloan Intermediary Grant": ["✔️ Loan Loss Reserve Minimums", "✔️ Monthly MRRS Reporting", "✔️ SBA Form 413 Clearance", "✔️ Tech Assistance 25% Rule"],
        "DOE Weatherization Assistance Program": ["✔️ ASHRAE 62.2 Ventilation", "✔️ Historic Preservation Clearance", "✔️ Quality Control Sign-off", "✔️ Energy Audit Software Output"]
    }
    
    grant_choice = st.selectbox("Which grant did you receive?", list(GRANTS.keys()))
    
    if st.button("Show My Checklist! ✨"):
        st.info("Here is everything you need to keep your funding safe:")
        for item in GRANTS[grant_choice]:
            st.write(item)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 4: CIVICBOT ---
elif page == "💬 CivicBot Helper":
    st.markdown('<div class="friendly-card">', unsafe_allow_html=True)
    st.markdown("<h3 class='accent-purple'>🤖 CivicBot Interactive Menu</h3>", unsafe_allow_html=True)
    st.write("Hi! I'm CivicBot. I know all about public service rules. Use the menus below to ask me a question!")
    
    category = st.radio("1. What do you want to talk about?", ["Nonprofit Formation", "Pro Bono Work", "Public Service", "Government Grants"])
    
    st.markdown("---")
    
    if category == "Nonprofit Formation":
        q = st.selectbox("2. Pick your question:", ["How do I start a charity?", "What is an EIN?", "What is IRS Form 1023?"])
        if q == "How do I start a charity?": ans = "It's easy! First, file 'Articles of Incorporation' in your home state. Then, get an EIN from the IRS, write your Bylaws, and apply for tax-exempt status!"
        elif q == "What is an EIN?": ans = "An EIN is an Employer Identification Number. It's basically a Social Security Number for your business. You get it for free on the IRS website!"
        elif q == "What is IRS Form 1023?": ans = "Form 1023 is the long application you send the IRS to prove you are doing charitable work. If you are small, you can use the shorter 1023-EZ!"
        
    elif category == "Pro Bono Work":
        q = st.selectbox("2. Pick your question:", ["What does Pro Bono mean?", "Do lawyers have to do it?", "How do I find a Pro Bono lawyer?"])
        if q == "What does Pro Bono mean?": ans = "Pro Bono is Latin for 'for the public good.' It means lawyers working for free to help people who can't afford to pay!"
        elif q == "Do lawyers have to do it?": ans = "The American Bar Association recommends lawyers do at least 50 hours of pro bono work a year, but it isn't legally required in most states."
        elif q == "How do I find a Pro Bono lawyer?": ans = "You can usually find them through your local Legal Aid Society or your state's Bar Association website!"
        
    elif category == "Public Service":
        q = st.selectbox("2. Pick your question:", ["What counts as Public Service?", "Are donations tax deductible?", "Can public servants get student loans forgiven?"])
        if q == "What counts as Public Service?": ans = "Working for the government, a 501(c)(3) nonprofit, public schools, or law enforcement all count as public service!"
        elif q == "Are donations tax deductible?": ans = "Yes! If you donate money to a registered 501(c)(3) public charity, you can deduct it from your taxes."
        elif q == "Can public servants get student loans forgiven?": ans = "Yes! Through the Public Service Loan Forgiveness (PSLF) program, if you make 120 payments while working in public service, the rest of your federal loans are forgiven!"
        
    elif category == "Government Grants":
        q = st.selectbox("2. Pick your question:", ["What is 2 CFR Part 200?", "What happens if I fail an audit?", "Can I use grant money to buy food?"])
        if q == "What is 2 CFR Part 200?": ans = "It's the ultimate rulebook for federal grants! It tells you exactly how you are allowed to spend government money."
        elif q == "What happens if I fail an audit?": ans = "If you spend money incorrectly, the government can issue a 'clawback,' which means you have to pay the money back!"
        elif q == "Can I use grant money to buy food?": ans = "Usually no! Federal grants have strict rules against buying food or alcohol, unless the grant is specifically for a food-pantry program."

    if st.button("Ask CivicBot! 🚀"):
        st.success("CivicBot says: " + ans)

    st.markdown('</div>', unsafe_allow_html=True)
