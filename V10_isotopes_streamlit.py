import streamlit as st

st.set_page_config(page_title="Average Atomic Weight Quiz")

st.title("Average Atomic Weight")

# Display reference image
st.image("2.png", caption="Reference Formula", use_column_width=True)

st.write("### Multiple Choice Quiz")
st.write("Select the best answer for each question.")

# -----------------------------
# Questions, choices, answers
# -----------------------------
questions = [
    "1. Define the term isotope.",
    "2. Why do elements have non-integer atomic weights?",
    "3. An isotope has % abundance = 35.00%. What is the decimal equivalent?",
    "4. An isotope with 20.00% abundance has a mass of 80.00 amu. What is its contribution to the average atomic weight?",
    "5. A hypothetical element has two isotopes: 90% at 60 amu and 10% at 70 amu. The average atomic weight lies closest to:",
    "6. Two isotopes each have 50.00% abundance. Isotope A = 40.00 amu, Isotope B = 50.00 amu. What is the quickest way to compute the average?",
    "7. What is the average atomic weight of the element in question 6?",
    "8. Chlorine has isotopes Cl‑35 and Cl‑37. What do the numbers 35 and 37 refer to?",
    "9. What is the difference between chlorine‑35 and chlorine‑37?",
    "10. Compute the average atomic mass of chlorine: Cl‑35 (75.77%, 34.97 amu) and Cl‑37 (24.23%, 36.97 amu).",
    "11. Magnesium has isotopes Mg‑24 (78.70%, 23.985 amu), Mg‑25 (10.13%, 24.986 amu), Mg‑26 (11.16%, 25.983 amu). What is the average atomic weight?"
]

choices = [
    ["Atoms of the same element with different numbers of neutrons",
     "Atoms with the same mass but different elements",
     "Atoms that are unstable and radioactive"],

    ["Because atomic weights are rounded",
     "Because most elements have multiple isotopes with different masses and abundances",
     "Because electrons contribute to atomic weight"],

    ["3.5", "0.35", "0.035"],

    ["80.00 amu", "20.00 amu", "16.00 amu"],

    ["70 amu", "65 amu", "60 amu"],

    ["Add the masses and divide by 2",
     "Multiply each mass by its abundance",
     "Use the isotope with the higher mass"],

    ["50.00 amu", "40.00 amu", "45.00 amu"],

    ["Mass numbers (sum of protons and neutrons)",
     "Atomic numbers (number of protons)",
     "Number of electrons"],

    ["Chlorine‑37 has two more protons",
     "Chlorine‑37 has two more neutrons",
     "Chlorine‑37 has more electrons"],

    ["35.00 amu", "35.45 amu", "36.00 amu"],

    ["24.000 amu", "25.000 amu", "24.307 amu"]
]

correct_answers = [
    "Atoms of the same element with different numbers of neutrons",
    "Because most elements have multiple isotopes with different masses and abundances",
    "0.35",
    "16.00 amu",
    "60 amu",
    "Add the masses and divide by 2",
    "45.00 amu",
    "Mass numbers (sum of protons and neutrons)",
    "Chlorine‑37 has two more neutrons",
    "35.45 amu = 0.7577x34.97+0.2423x36.97",
    "24.307 amu = 0.787x23.95+0.1013x24.986+0.1116x25.983"
]

# Mini-explanations
explanations = [
    "Isotopes have the same number of protons but different numbers of neutrons, which changes their mass.",
    "Atomic weight is a weighted average of all naturally occurring isotopes, so it rarely lands on a whole number.",
    "Convert percent abundance to decimal by dividing by 100.",
    "Multiply fractional abundance by isotope mass: 0.20 × 80 = 16 amu.",
    "The average is pulled toward the isotope with the highest abundance — here, 90% at 60 amu.",
    "Equal abundances mean a simple average: (40 + 50) / 2 = 45 amu.",
    "Direct result of the simple average from question 6.",
    "Mass numbers represent protons + neutrons in the nucleus.",
    "Both isotopes have 17 protons; the difference is in the number of neutrons.",
    "Weighted average using fractional abundances and isotope masses.",
    "Multiply each mass by its fractional abundance and sum the contributions."
]

# -----------------------------
# Collect student responses
# -----------------------------
responses = []
for i, q in enumerate(questions):
    st.write(f"**{q}**")
    response = st.radio(
        label="",
        options=choices[i],
        key=f"q{i}",
        index=None
    )
    responses.append(response)
    st.write("---")

# -----------------------------
# Submit button
# -----------------------------
if st.button("Submit"):
    score = 0
    for i in range(len(questions)):
        if responses[i] == correct_answers[i]:
            score += 1

    st.write(f"## Final Score: {score} / {len(questions)}")

    # Feedback tiers
    if score >= 10:
        st.success(
            "Outstanding work! Your understanding of isotopes and average atomic weight is exceptional."
        )
        st.write("**Next step:** Try creating your own isotope sets and predicting the average atomic weight.")

    elif score >= 8:
        st.info(
            "Strong performance! You clearly understand the core ideas — isotopes, mass numbers, and weighted averages."
        )
        st.write("**To strengthen further:** Review how percent abundance influences the weighted average.")

    elif score >= 5:
        st.warning(
            "You’re making progress, but some key ideas need reinforcement."
        )
        st.write("**Focus on:** converting % to decimals, weighted averages, and mass number vs. atomic number.")

    else:
        st.error(
            "This attempt shows you're still building foundational understanding — and that's okay!"
        )
        st.write("**Start with:** what isotopes are, how mass number works, and why weighted averages matter.")

    # -----------------------------
    # Per-question feedback + explanations
    # -----------------------------
    st.write("---")
    st.write("## Detailed Feedback by Question")

    for i in range(len(questions)):
        st.write(f"### Question {i+1}")
        st.write(questions[i])

        # Safe handling of unanswered questions
        student = responses[i] if responses[i] is not None else "No answer selected"
        correct = correct_answers[i]

        if student == correct:
            st.success(f"Your answer: {student}")
        else:
            st.error(f"Your answer: {student}")

        st.write(f"**Correct answer:** {correct}")
        st.write(f"**Explanation:** {explanations[i]}")
        st.write("")
