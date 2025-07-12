# chatbot.py

def get_bot_response(user_input):
    user_input = user_input.lower()

    
    symptom_keywords = ["symptom", "sign"]
    treatment_keywords = ["what should i do", "treat", "remedy", "care", "naturally", "home treatment", "cure", "recover"]
    medicine_keywords = ["medicine", "tablet", "drug", "medication", "what can i take"]

  
    if "covid" in user_input:
        if any(word in user_input for word in symptom_keywords):
            return ("COVID-19 symptoms:\n"
                    "- Fever, chills\n"
                    "- Cough, sore throat\n"
                    "- Loss of taste/smell\n"
                    "- Shortness of breath\n"
                    "- Fatigue or body ache")
        if any(word in user_input for word in medicine_keywords):
            return ("COVID medicines (mild):\n"
                    "- Paracetamol\n"
                    "- Vitamin C, Zinc\n"
                    "- Warm water, steam\n"
                    "- Consult doctor if symptoms worsen")
        if any(word in user_input for word in treatment_keywords):
            return ("Steps for COVID care:\n"
                    "- Isolate, rest, hydrate\n"
                    "- Monitor oxygen level\n"
                    "- Follow medical advice")

   
    if "fever" in user_input:
        if any(word in user_input for word in symptom_keywords):
            return ("Fever symptoms:\n"
                    "- High temperature\n"
                    "- Chills, sweating\n"
                    "- Headache, fatigue\n"
                    "- Body pain")
        if any(word in user_input for word in medicine_keywords):
            return ("Fever medicine:\n"
                    "- Paracetamol 500mg (every 6 hours)\n"
                    "- Stay hydrated, avoid cold drinks")
        if any(word in user_input for word in treatment_keywords):
            return ("Fever remedies:\n"
                    "- Rest in cool place\n"
                    "- Drink warm fluids\n"
                    "- Use wet cloth on forehead\n"
                    "- Take Paracetamol if needed")

    # ------------------- Cold & Cough -------------------
    if "cold" in user_input or "cough" in user_input:
        if any(word in user_input for word in symptom_keywords):
            return ("Cold/Cough symptoms:\n"
                    "- Runny nose, sneezing\n"
                    "- Sore throat\n"
                    "- Dry or wet cough\n"
                    "- Mild fever or fatigue")
        if any(word in user_input for word in medicine_keywords):
            return ("Cold & Cough medicine:\n"
                    "- Cetirizine for sneezing\n"
                    "- Paracetamol for fever\n"
                    "- Cough syrup (Benadryl, Ascoril)\n"
                    "- Steam inhalation")
        if any(word in user_input for word in treatment_keywords):
            return ("Cold & Cough home remedies:\n"
                    "- Hot fluids (soup, tea)\n"
                    "- Gargle with salt water\n"
                    "- Steam inhalation\n"
                    "- Rest and avoid cold food")

    if "headache" in user_input:
        if any(word in user_input for word in symptom_keywords):
            return ("Headache symptoms:\n"
                    "- Pain in forehead or temples\n"
                    "- Throbbing or pressure\n"
                    "- Sensitivity to light/sound\n"
                    "- May be due to stress or dehydration")
        if any(word in user_input for word in medicine_keywords):
            return ("Headache medicine:\n"
                    "- Paracetamol\n"
                    "- Ibuprofen (after food)\n"
                    "- Avoid screens")
        if any(word in user_input for word in treatment_keywords):
            return ("Headache natural treatment:\n"
                    "- Rest in dark quiet room\n"
                    "- Apply warm or cold compress\n"
                    "- Drink plenty of water")

   
    if "stomach" in user_input or "abdominal" in user_input:
        if any(word in user_input for word in symptom_keywords):
            return ("Stomach pain causes:\n"
                    "- Gas, indigestion\n"
                    "- Food poisoning, acidity\n"
                    "- Infection or cramps")
        if any(word in user_input for word in medicine_keywords):
            return ("Stomach pain medicine:\n"
                    "- Antacid (Gelusil, Digene)\n"
                    "- ORS for dehydration\n"
                    "- Avoid painkillers unless prescribed")
        if any(word in user_input for word in treatment_keywords):
            return ("Home remedies for stomach pain:\n"
                    "- Warm water\n"
                    "- Avoid spicy/oily food\n"
                    "- Rest well\n"
                    "- Try ginger or mint tea")

 
    if "vomiting" in user_input:
        return ("Vomiting causes:\n"
                "- Food poisoning, indigestion\n"
                "- Motion sickness, infection\n"
                "Remedy:\n"
                "- ORS to stay hydrated\n"
                "- Eat bland foods\n"
                "- Take antiemetics if needed (like Domperidone)")

   
    if "diarrhea" in user_input or "loose motion" in user_input:
        return ("Diarrhea care:\n"
                "- Drink ORS to stay hydrated\n"
                "- Avoid dairy/spicy food\n"
                "- Eat soft diet (banana, rice)\n"
                "- Medicine: Loperamide (only if prescribed)")

   
    if "dizzy" in user_input or "dizziness" in user_input:
        return ("Dizziness can occur due to:\n"
                "- Dehydration\n"
                "- Low BP or sugar\n"
                "- Lack of sleep\n"
                "What to do:\n"
                "- Sit or lie down immediately\n"
                "- Drink water\n"
                "- Avoid sudden movements")


    if "fatigue" in user_input or "tired" in user_input:
        return ("Fatigue causes:\n"
                "- Lack of sleep\n"
                "- Infection or illness\n"
                "- Poor nutrition\n"
                "What to do:\n"
                "- Get proper sleep\n"
                "- Eat balanced meals\n"
                "- Check for vitamin deficiency")


    if "sore throat" in user_input or "throat pain" in user_input:
        return ("Sore throat care:\n"
                "- Gargle with warm salt water\n"
                "- Drink warm fluids (ginger tea, turmeric milk)\n"
                "- Use lozenges\n"
                "- Avoid cold drinks")

    if "body pain" in user_input or "muscle ache" in user_input:
        return ("Body pain relief:\n"
                "- Paracetamol or Ibuprofen\n"
                "- Warm water bath\n"
                "- Gentle stretching\n"
                "- Rest and hydrate")

    # ------------------- Side Effects -------------------
    if "side effect" in user_input:
        if "paracetamol" in user_input:
            return ("Paracetamol side effects:\n"
                    "- Generally safe\n"
                    "- Overdose may damage liver")
        if "ibuprofen" in user_input:
            return ("Ibuprofen side effects:\n"
                    "- Stomach irritation\n"
                    "- Risk to kidneys (long-term)")
        return "Please specify the medicine name to get side effects."

    # ------------------- Default fallback -------------------
    return ("👩‍⚕️ I am your health assistant.\n"
            "You can ask me things like:\n"
            "- What are the symptoms of fever, covid, cold, or headache?\n"
            "- What medicine should I take for sore throat or stomach pain?\n"
            "- How to treat vomiting or dizziness at home?\n"
            "- What can I do for fatigue or tiredness?\n"
            "- What are the side effects of paracetamol or ibuprofen?\n"
            "- I feel dizzy / I have loose motion / I have throat pain — what should I do?\n"
            "⚠️ For serious symptoms, please consult a medical professional.")
