import streamlit as st

st.set_page_config(page_title="MediBot - Health Assistant", page_icon="💊", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .title {
            text-align: center;
            color: #2a9d8f;
            font-size: 40px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #264653;
            font-size: 20px;
        }
        .result-box {
            background-color: #e9f5f2;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #2a9d8f;
            color: #264653;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💊 MediBot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI-Powered Health Assistant</div>", unsafe_allow_html=True)
st.write("Select your symptoms below and let MediBot guide you!")

# Symptoms 

disease_data = {
    "Fever": {
        "symptoms": ["High temperature", "Chills", "Watery eyes"],
        "medications": ["Paracetamol (500 mg) every 6-8 hours", "Drink warm fluids"],
        "tips": "Take rest, drink plenty of water. If fever persists >102°F for 3 days, consult a doctor."
    },
    "Cold": {
        "symptoms": ["Runny nose", "Sneezing", "Watery eyes"],
        "medications": ["Antihistamines like Cetirizine at night", "Steam inhalation twice a day"],
        "tips": "Stay hydrated, avoid cold drinks. If symptoms persist beyond 7 days, see a doctor."
    },
    "Cough": {
        "symptoms": ["Dry throat", "Sore throat", "Mild chest pain"],
        "medications": ["Cough syrup (Dextromethorphan) twice daily", "Warm salt water gargle"],
        "tips": "Avoid cold beverages. If cough lasts >2 weeks or with blood, visit a doctor."
    },
    "Headache": {
        "symptoms": ["Pain in forehead", "Tension in neck", "Light sensitivity"],
        "medications": ["Paracetamol (500 mg) as needed", "Rest in a quiet room"],
        "tips": "Stay hydrated, avoid stress. If severe headache with vomiting, consult doctor immediately."
    },
    "Body Ache": {
        "symptoms": ["Muscle pain", "Weakness", "Fatigue"],
        "medications": ["Pain relief tablets (Paracetamol)", "Warm compress"],
        "tips": "Gentle stretching, warm bath. If pain persists >1 week, see a doctor."
    },
    "Anxiety": {
        "symptoms": ["Restlessness", "Rapid heartbeat", "Sweating"],
        "medications": ["Deep breathing exercises", "Avoid caffeine"],
        "tips": "Practice meditation, talk to a therapist if frequent anxiety attacks occur."
    }
}


# UI Components

selected_symptoms = st.multiselect("Select your symptoms:", 
                                   ["High temperature", "Chills", "Watery eyes", "Runny nose", "Sneezing", "Dry throat", 
                                    "Sore throat", "Pain in forehead", "Tension in neck", "Light sensitivity", 
                                    "Muscle pain", "Weakness", "Fatigue", "Restlessness", "Rapid heartbeat", "Sweating"])

if st.button("Analyze"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        possible_diseases = []
        for disease, details in disease_data.items():
            if any(symptom in details["symptoms"] for symptom in selected_symptoms):
                possible_diseases.append(disease)

        if len(possible_diseases) == 1:
            disease = possible_diseases[0]
            st.markdown(f"<div class='result-box'><h3>🩺 Condition: {disease}</h3>", unsafe_allow_html=True)
            st.write("**Recommended Medications:**")
            for med in disease_data[disease]["medications"]:
                st.write(f"- {med}")
            st.write("**Care Tips:**")
            st.write(disease_data[disease]["tips"])
            st.markdown("</div>", unsafe_allow_html=True)

        elif len(possible_diseases) > 1:
            st.info("Multiple possible conditions detected. Let's narrow it down.")
            for d in possible_diseases:
                question = st.radio(f"Do you have these symptoms related to {d}?", disease_data[d]["symptoms"], index=0)
                if question:
                    st.write(f"Based on your answer, you might have **{d}**.")
                    st.write("**Recommended Medications:**")
                    for med in disease_data[d]["medications"]:
                        st.write(f"- {med}")
                    st.write("**Care Tips:**")
                    st.write(disease_data[d]["tips"])
                    break
        else:
            st.error("No matching disease found. Please consult a doctor.")
