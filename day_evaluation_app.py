import streamlit as st

# عنوان التطبيق
st.title("🌞 تقييم يومك")

st.write("مرحبًا! خلينا نقيم يومك النهارده مع بعض 😊")

# دالة لحساب تقييم النوم
def calculate_sleep(hours_sleep):
    if hours_sleep >= 9:
        return 10
    elif hours_sleep >= 7:
        return 8
    elif hours_sleep >= 5:
        return 6
    else:
        return 3

# دالة لحساب المزاج
def calculate_mood(users_mood):
    if users_mood == 5:
        return 10
    elif users_mood == 4:
        return 8
    elif users_mood == 3:
        return 6
    elif users_mood == 2:
        return 4
    elif users_mood == 1:
        return 2

# دالة لحساب الإنتاجية
def calculate_productivity(users_productivity):
    if users_productivity == 5:
        return 10
    elif users_productivity == 4:
        return 8
    elif users_productivity == 3:
        return 6
    elif users_productivity == 2:
        return 4
    elif users_productivity == 1:
        return 2

# دالة حساب التقييم النهائي
def calculate_final_evaluation(hours_sleep, users_mood, users_productivity):
    total = (hours_sleep + users_mood + users_productivity) / 3
    return total

# واجهة المستخدم
st.header("📝 أدخل تقييمك:")

hours_sleep = st.slider("كم ساعة نمت؟", 0, 12, 7)
users_mood = st.slider("قيّم مزاجك اليوم (1 إلى 5)", 1, 5, 3)
users_productivity = st.slider("قيّم إنتاجيتك اليوم (1 إلى 5)", 1, 5, 3)

if st.button("احسب تقييمي 🎯"):
    sleep_score = calculate_sleep(hours_sleep)
    mood_score = calculate_mood(users_mood)
    productivity_score = calculate_productivity(users_productivity)

    evaluation = calculate_final_evaluation(sleep_score, mood_score, productivity_score)

    st.write("---")
    if evaluation >= 8:
        st.success(f"🌟 يومك ممتاز! تقييمك: {evaluation:.1f}")
    elif evaluation >= 5:
        st.info(f"🙂 يومك جيد! تقييمك: {evaluation:.1f}")
    else:
        st.warning(f"😴 يومك محتاج راحة! تقييمك: {evaluation:.1f}")
day_evaluation_app.py
