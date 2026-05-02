
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

chat_history = []
last_topic = ""

def chatbot_response(user_input):
    global last_topic

    user_input = user_input.lower()
    chat_history.append(user_input)

    if "مرحبا" in user_input:
        return "أهلاً بيك! إزاي أقدر أساعدك؟"

    elif "hello" in user_input or "hello" in user_input:
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

    elif "price" in user_input or "price" in user_input:
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
تصميم وتطوير المواقع الإلكترونية (شركات – متاجر – صفحات هبوط)
برمجة تطبيقات الموبايل (Android & iOS)
إنشاء أنظمة حجز ودفع إلكتروني
تطوير لوحات تحكم (Dashboard) لإدارة المشاريع
تحسين سرعة وأداء المواقع (Performance Optimization)
صيانة وتحديث المواقع والتطبيقات
📢 ثانيًا: خدمات التسويق الرقمي
إدارة حسابات السوشيال ميديا
تصميم بوستات وإعلانات احترافية
إنشاء خطط تسويقية شهرية
إدارة الحملات الإعلانية (Facebook – Instagram – Google)
كتابة محتوى تسويقي جذاب (Copywriting)
تحليل الأداء وتحسين النتائج
🎯 ثالثًا: خدمات الإعلانات الممولة
إعداد وتجهيز الحملات الإعلانية
استهداف الجمهور المناسب بدقة
إدارة وتحسين الحملات لزيادة الأرباح
إعادة استهداف العملاء (Retargeting)
تقارير أداء مفصلة
📊 رابعًا: استشارات البيزنس
تحليل فكرة المشروع
إعداد خطط عمل (Business Plans)
استراتيجيات النمو والتوسع
تحسين المبيعات وزيادة الأرباح
استشارات تسويقية وتقنية
🔥 خامسًا: باكدجات متكاملة
بدء مشروع من الصفر (برمجة + تسويق)
تطوير المشاريع القائمة وزيادة أرباحها
إدارة كاملة للمشروع أونلاين
💡 هدفنا
نساعدك تحول فكرتك لمشروع ناجح ونكبره معاك خطوة بخطوة
"""

    elif "services" in user_input:
        last_topic = "services"
        return """🚀 Nexora Services List
We offer comprehensive solutions to help you start and grow your business professionally, from idea to success.
💻 First: Programming and Development Services
Website Design and Development (Companies – Stores – Landing Pages)
Mobile Application Development (Android & iOS)
Creating Electronic Booking and Payment Systems
Developing Project Management Dashboards
Website Speed and Performance Optimization
Website and Application Maintenance and Updates
📢 Second: Digital Marketing Services
Social Media Account Management
Designing Professional Posts and Ads
Creating Monthly Marketing Plans
Managing Advertising Campaigns (Facebook – Instagram – Google)
Creating Engaging Marketing Content (Copywriting)
Analyzing Performance and Improving Results
🎯 Third: Paid Advertising Services
Preparing and Setting Up Advertising Campaigns
Accurately Targeting the Right Audience
Managing and Improving Campaigns to Increase Profits
Retargeting Customers
Detailed Performance Reports
📊 Fourth: Business Consulting
Project Idea Analysis
Developing Business Plans
Growth and Expansion Strategies
Improving Sales and Increasing Profits
Marketing and Technical Consulting
🔥 Fifth: Comprehensive Packages
Getting Started Start-from-scratch project (programming + marketing)
Developing existing projects and increasing their profits
Complete online project management
💡 Our goal
To help you transform your idea into a successful project and grow it with you step by step
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
        return "Sory but I don't understand you can call technical support amra7777zzxxamr7777@gmail.com"


# ================== FLASK ROUTES ==================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data["message"]
    reply = chatbot_response(user)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)