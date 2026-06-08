import streamlit as st

chat_history = []
last_topic = ""

def chatbot_response(user_input):
    global last_topic

    user_input = user_input.lower()
    chat_history.append(user_input)

    if "مرحبا" in user_input:
        return "أهلاً بيك! إزاي أقدر أساعدك؟"

    elif "hello" in user_input:
        return "Hi How can I help you"

    elif "سعر" in user_input:
        last_topic = "price"
        return """💰 💻 قائمة أسعار Nexora (متوسط)

🧑‍💻 أولًا: البرمجة (Web & Apps)

🌐 مواقع إلكترونية
موقع بسيط (Landing Page): 80 – 200$
موقع شركة (5–10 صفحات): 250 – 600$
موقع متكامل (حجز / متجر): 600 – 1500$

📱 تطبيقات موبايل
تطبيق بسيط: 500 – 1200$
تطبيق متوسط: 1200 – 3000$
تطبيق متكامل (دفع / سيستم كبير): 3000 – 7000$

📢 ثانيًا: التسويق

📱 سوشيال ميديا
بوست: 10 – 20$
15 بوست: 120 – 200$
إدارة كاملة: 200 – 400$/شهر

🎯 إعلانات ممولة
إعداد حملة: 30 – 100$
إدارة شهرية: 150 – 400$
أو نسبة: 10% – 20%

📊 ثالثًا: استشارات البيزنس

جلسة 30 دقيقة: 20 – 50$
جلسة ساعة: 50 – 120$
خطة بيزنس كاملة: 150 – 500$
"""

    elif "price" in user_input:
        last_topic = "price"
        return """💰 💻 Nexora Price List (Average)

🧑‍💻 First: Programming (Web & Apps)

🌐 Websites
Simple Website (Landing Page): $80 – $200
Company Website (5–10 Pages): $250 – $600
Complete Website (Booking/Shop): $600 – $1500

📱 Mobile Applications
Simple App: $500 – $1200
Medium App: $1200 – $3000
Complete App (Payment/Large System): $3000 – $7000

📢 Second: Marketing

📱 Social Media
Post: $10 – $20
15 Posts: $120 – $200
Complete Management: $200 – $400/month

🎯 Paid Ads
Campaign Setup: $30 – $100
Monthly Management: $150-$400
Or Percentage: 10%-20%

📊 Third: Business Consultations

30-minute session: $20-$50
1-hour session: $50-$120
Complete Business Plan: $150-$500
"""

    elif "خدمات" in user_input:
        last_topic = "services"
        return """🚀 قائمة خدمات Nexora

نقدم حلول متكاملة تساعدك تبدأ وتكبر مشروعك باحترافية، من الفكرة لحد النجاح.

💻 أولًا: خدمات البرمجة والتطوير
تصميم وتطوير المواقع الإلكترونية
برمجة تطبيقات الموبايل
إنشاء أنظمة حجز ودفع إلكتروني
تطوير لوحات تحكم
تحسين سرعة وأداء المواقع
صيانة وتحديث المواقع والتطبيقات

📢 ثانيًا: خدمات التسويق الرقمي
إدارة حسابات السوشيال ميديا
تصميم بوستات وإعلانات احترافية
إنشاء خطط تسويقية شهرية
إدارة الحملات الإعلانية
كتابة محتوى تسويقي
تحليل الأداء وتحسين النتائج

🎯 ثالثًا: خدمات الإعلانات الممولة
إعداد وتجهيز الحملات الإعلانية
استهداف الجمهور المناسب
إدارة وتحسين الحملات
إعادة استهداف العملاء
تقارير أداء مفصلة

📊 رابعًا: استشارات البيزنس
تحليل فكرة المشروع
إعداد خطط عمل
استراتيجيات النمو والتوسع
تحسين المبيعات
استشارات تسويقية وتقنية

🔥 خامسًا: باكدجات متكاملة
بدء مشروع من الصفر
تطوير المشاريع القائمة
إدارة كاملة للمشروع أونلاين

💡 هدفنا
نساعدك تحول فكرتك لمشروع ناجح ونكبره معاك خطوة بخطوة
"""

    elif "services" in user_input:
        last_topic = "services"
        return """🚀 Nexora Services List

We offer comprehensive solutions to help you start and grow your business professionally.

💻 Programming and Development Services
Website Design and Development
Mobile Application Development
Electronic Booking and Payment Systems
Project Management Dashboards
Performance Optimization
Maintenance and Updates

📢 Digital Marketing Services
Social Media Management
Professional Posts and Ads
Marketing Plans
Advertising Campaigns
Copywriting
Performance Analysis

🎯 Paid Advertising Services
Campaign Setup
Audience Targeting
Campaign Optimization
Retargeting
Performance Reports

📊 Business Consulting
Project Analysis
Business Plans
Growth Strategies
Sales Improvement
Marketing and Technical Consulting

🔥 Comprehensive Packages
Start-from-scratch project
Develop existing projects
Complete online project management

💡 Our Goal
Helping you transform your idea into a successful project.
"""

    elif "مواعيد" in user_input or "ميعاد" in user_input:
        return "متاح من 9 صباحًا إلى 5 مساءً"

    elif "working hours" in user_input:
        return "Available from 9 am to 5 pm"

    elif "خصم" in user_input:
        if last_topic == "price":
            return "نعم يوجد خصومات على المشاريع الكبيرة 👍"
        else:
            return "خصم على أنهي خدمة؟"

    elif "discount" in user_input:
        if last_topic == "price":
            return "Yes, we offer discounts on large projects 👍"
        else:
            return "Discount on which service?"

    else:
        return "Sorry, I don't understand. Please contact technical support: amra7777zzxxamr7777@gmail.com"


# ================= STREAMLIT UI =================

st.set_page_config(
    page_title="Nexora ChatBot",
    page_icon="🤖"
)

st.title("🤖 Nexora ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# إدخال المستخدم
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    reply = chatbot_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)
