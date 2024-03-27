import streamlit as st
from src.domain import footer
import os
from src.domain.pageConfig import set_env_vars

# LLM Specific
from langchain.llms import OpenAI
from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter


set_env_vars()
footer.hide_footer(st)

backend = os.environ['backend']

st.markdown("# Do you Judge or Do you Learn?")
st.markdown("---")
st.markdown("""
Welcome to an explorative journey inspired by the profound insights from Marilee Adams's book, *Change Your Questions, Change Your Life*. This interactive experience is designed to illuminate the power of questions in transforming our thoughts, emotions, and actions, ultimately influencing our mental health and wellbeing.

**Purpose of This Page:**

My goal is to leverage the capabilities of Large Language Models (LLMs) to demonstrate how thoughtful questioning, inspired by Adams's work, can offer new perspectives and insights into our daily lives. It's about opening doors to self-reflection and understanding, using technology as a bridge to deeper self-awareness.

**How Can This Help?**

- **Mental Health Exploration:** I aim to support individuals in their mental health journey by providing a space for reflection and self-exploration.
- **Advisory Insight:** Though not a substitute for professional advice, this tool offers guidance and thought-provoking questions that might illuminate paths less traveled in your mind.
- **Accessibility of Knowledge:** Recognizing that not everyone has access to professional help or can purchase insightful books, this free resource serves as a stepping stone towards self-improvement and mental wellness.

**Inspiration, Not Imitation:**

It's important to emphasize that this experience is *inspired* by Marilee Adams's work. The questions and the approach I take are reflections inspired by the themes of her book, aiming to spark curiosity and encourage personal growth. This is not an act of plagiarism but a homage to the transformative power of the right questions. I highly recommend purchasing her book to dive deeper into the art of question-based growth.

**Disclaimer:**

Please remember, this is an example of how technology, specifically LLMs, can offer support in the realm of mental health. It is not a medical or professional advisory tool. If you're facing serious mental health challenges, I urge you to seek professional help.

Let's embark on this journey together, exploring how changing our questions can indeed change our lives. Kudos to you for taking this step towards self-discovery and mental wellness.
""")

# Disclaimer and introduction
st.write("Please be aware that this platform does not store any of your personal information. While we encourage open and honest reflection, we recommend using aliases or pseudonyms instead of real names to ensure confidentiality.")


# Define exercise functions with an index parameter
def exercise_1():
    st.header("Exercise 1: Reflecting on Interpersonal Dynamics")

    st.write("""
    In this exercise, you're encouraged to reflect on your interactions with someone whose behavior sometimes puzzles or annoys you. 
    By examining these interactions and your responses, you can gain insights into your interpersonal dynamics and consider 
    alternative approaches or perspectives.
    """)

    # Providing a detailed description and example for "Alias for the Person"
    alias = st.text_input("Alias for the Person", key="ex1_alias",
                          help="Assign a nickname or alias for the person whose behavior annoys you.")
    st.write("Example: If you're thinking about a coworker who often interrupts you, you might use 'The Interrupter' as an alias.")

    # Expanding the description and example for "Annoying Behavior"
    annoying_behavior = st.text_area("Annoying Behavior", key="ex1_behavior",
                                     help="Describe a specific behavior of this person that annoys you. Be as specific as possible.")
    st.write("Example: 'They frequently interrupt me during meetings, not allowing me to finish my points.'")
    # Providing a detailed description and example for "Personal Reaction"
    personal_reaction = st.text_area("Personal Reaction", key="ex1_reaction",
                                     help="Reflect on how you typically respond to this behavior. Consider your emotions, actions, and any words you might say in response.")
    st.write("""
    Example: 'I feel frustrated and undervalued. Sometimes, I react by shutting down and not contributing further, 
    even though I have valuable points to make.'
    """)

    return {"Alias for the Person": alias, "Annoying Behavior": annoying_behavior, "Personal Reaction": personal_reaction}


def exercise_2():
    st.header("Exercise 2: Deeper Analysis and Personal Growth")

    st.write("""
    This exercise invites you to delve deeper into understanding the dynamics of your relationship with the person you've been reflecting on. 
    By examining both the challenges and the significance of this relationship, you can uncover motivations for change and consider the implications of inaction.
    """)

    relationship_significance = st.text_area(help="Reflect on the role this person plays in your life. Think about the layers of your relationship—whether they're a family member, friend, coworker, or another significant figure. Consider the bonds you share, the history between you, and the impact they have on your daily life. Why is this relationship important to you? What values, experiences, or goals make this connection significant?",
                                             key="ex2_relationship_significance",
                                             label="Who is this person in your life, and why is your relationship with them important?",
                                             )

    specific_annoyances = st.text_area(help="Identify and describe the behaviors or comments from this person that trigger negative feelings or reactions in you. Be as specific as possible—think about particular instances, words, or actions that bother you. How do these annoyances contrast with the aspects of the relationship you value? Acknowledge any patterns you've noticed: are these incidents isolated, or do they represent ongoing challenges?",
                                       key="ex2_specific_annoyances",
                                       label="What specific actions or words from this person bother you? Be candid.",
                                       )

    detailed_reaction = st.text_area(help="Examine your immediate and subsequent reactions to these annoyances. Consider your physical responses (e.g., tense muscles, changes in breathing), emotional reactions (e.g., anger, sadness, frustration), and how you express yourself verbally or through actions. How do these reactions affect the situation and your well-being? Delve into the reasons behind your responses, and consider how they align with your ideal way of handling conflicts or challenges.",
                                     key="ex2_detailed_reaction",
                                     label="Describe how you react when faced with these annoyances, including physical, emotional, and verbal responses.",
                                     )

    motivation_for_change = st.text_area(help="Contemplate why changing your reactions or improving this relationship matters to you. Consider the broader implications for your personal growth, emotional health, and the overall dynamic between you and this person. What positive outcomes do you envision if changes are made? How do these motivations connect to your values, aspirations, or the quality of your daily life?",
                                         key="ex2_motivation_for_change",
                                         label="Why is it important for you to alter your reactions towards this person and their behavior?",
                                         )

    consequences_of_inaction = st.text_area(help="Reflect on the potential impact of not addressing the issues within this relationship. How might continued negative interactions affect your mental health, your view of yourself, and your feelings toward this person? Consider the ripple effects on other areas of your life, such as your work, social circle, or family dynamics. What are the emotional, psychological, and practical costs of letting things remain as they are?",
                                            key="ex2_consequences_of_inaction",
                                            label="What are the potential costs of not changing your reaction to this person's behavior?",
                                            )

    # Structuring the return information for LLM processing
    response = {
        "Relationship Significance": relationship_significance,
        "Specific Annoyances": specific_annoyances,
        "Detailed Reaction": detailed_reaction,
        "Motivation for Change": motivation_for_change,
        "Consequences of Inaction": consequences_of_inaction
    }

    return response


def exercise_3():
    st.header("Exercise 3: Interactions with Others")

    st.write("""
    This exercise examines how you engage with others, especially in challenging or conflicting situations.
    Please answer the following questions honestly to gain insights into your interpersonal dynamics.
    """)

    questions = [
        "Silence as a Response: Do you tend to withdraw and not express your thoughts when you disagree with someone?",
        "Standing Firm: When you believe strongly in your point, do you assertively defend it, ensuring your voice is heard?",
        "Avoidance Tactic: Is avoiding the person or situation altogether your go-to strategy when faced with disagreement or discomfort?",
        "Recollection of Errors: In moments of conflict, do you find yourself thinking about the other person's past mistakes?",
        "Questioning Intelligence: Do you catch yourself wondering about the other person's intelligence or common sense during disagreements?",
        "Seeking Faults: Do you often find yourself questioning what is wrong with the other person when they do something you disagree with?",
        "Feeling Frustrated: Is frustration a common feeling for you in these situations?",
        "Stress and Tension: Do you frequently feel stressed or tense during disagreements or conflicts?",
        "Feeling of Isolation: In moments of conflict, do you feel disconnected or alone, as if no one understands your perspective?",
        "Questioning Their Perspective: Do you doubt the validity or logic of the other person's viewpoint during a disagreement?"
    ]

    responses = {}
    for i, question in enumerate(questions, start=1):
        response = st.radio(f"Q{i}. {question}", ["Yes", "No"], key=f"ex3_{i}")
        responses[question] = response

    return responses


def exercise_4():
    st.header("Exercise 4: Constructive Engagement")

    st.write("""
    This set focuses on your ability to engage constructively in conflict or disagreement, promoting understanding and resolution.
    Please reflect on your responses to the following questions to assess your approach to conflict resolution.
    """)

    questions = [
        "Pausing to Breathe: Do you consciously take a moment to breathe and calm yourself before responding in a heated situation?",
        "Inquisitive Engagement: Are you prone to asking questions to genuinely understand the other person's concerns or perspective?",
        "Focusing on Agreement: Do you make an effort to point out areas of agreement before diving into the disagreements?",
        "Self-Reflection on Assumptions: Do you ask yourself what you might be missing or assuming too quickly in a conflict?",
        "Empathetic Perspective-Taking: Do you try to see the situation from the other person's point of view?",
        "Humanizing Reminders: Do you remind yourself that the other person is human and capable of making mistakes, just like you?",
        "Acceptance of Differences: Can you accept the other person's viewpoint without necessarily agreeing with it?",
        "Caring Beyond Disagreements: Do you maintain your care and concern for the person, even when you disagree with them?",
        "Respectful Engagement: Do you ensure that the other person feels respected and heard, regardless of the nature of the disagreement?",
        "Emotional Regulation: In a disagreement, do you manage to keep your emotions in check to maintain a constructive dialogue?"
    ]

    responses = {}
    for i, question in enumerate(questions, start=1):
        response = st.radio(f"Q{i}. {question}", ["Yes", "No"], key=f"ex4_{i}")
        responses[question] = response

    return responses


def exercise_5():
    st.header("Exercise 5: Self-Reflection in Adversity")

    st.write("""
    Explore your internal reactions and coping mechanisms when facing personal challenges or setbacks.
    Please reflect on your responses to the following questions to gain insights into your coping strategies.
    """)

    questions = [
        "Procrastination in Adversity: When confronted with a problem, do you tend to put off dealing with it?",
        "Denial of Upset: Do you ignore feelings of being upset, pretending everything is fine to continue working or functioning?",
        "Immobility in Progress: Faced with a setback, do you feel stuck and unable to move forward?",
        "Dwelling on Mistakes: Do you dwell on your past mistakes when experiencing a new setback?",
        "Self-Criticism for Errors: Are you hard on yourself, wondering how you could make such mistakes?",
        "Harsh Self-Judgment: Do you often criticize yourself harshly for your decisions or actions?",
        "Frustration and Anger Towards Self: Is frustration or anger towards yourself a common reaction in difficult situations?",
        "Disappointment in Self: Do you frequently feel disappointed in yourself when things don’t go as planned?",
        "Sorrow for Your Situation: When facing challenges, do you feel sad about being in that situation?",
        "Questioning Self-Worth: In adversity, do you question your worth or capabilities?"
    ]

    responses = {}
    for i, question in enumerate(questions, start=1):
        response = st.radio(f"Q{i}. {question}", ["Yes", "No"], key=f"ex5_{i}")
        responses[question] = response

    return responses


def exercise_6():
    st.header("Exercise 6: Cultivating Self-Compassion")

    st.write("""
    This exercise focuses on practices that foster self-compassion, resilience, and positive self-regard during tough times.
    Please reflect on your responses to the following questions to assess your ability to cultivate self-compassion.
    """)

    questions = [
        "Calming Techniques: Do you use techniques like deep breathing to soothe yourself when upset?",
        "Self-Exploration: Do you ask yourself what is really going on with you to understand your feelings better?",
        "Self-Care Actions: When feeling down, do you engage in self-care activities to uplift yourself?",
        "Reminding Self of Humanity: Do you remind yourself that making mistakes is a part of being human and it’s okay?",
        "Learning from Experiences: Are you open to learning something from every situation, even the difficult ones?",
        "Temporal Perspective: Do you reassure yourself that challenging times will pass and things will get better?",
        "Compassion Towards Self: Can you feel compassion for yourself, understanding that making mistakes does not define your worth?",
        "Unconditional Self-Acceptance: Do you accept yourself wholly, regardless of the mistakes you've made?",
        "Accepting Your Feelings: Are you accepting of whatever emotions you feel, recognizing them as valid?",
        "Self-Worth Affirmation: Do you affirm your worth and capabilities, even when you've erred or faced setbacks?"
    ]

    responses = {}
    for i, question in enumerate(questions, start=1):
        response = st.radio(f"Q{i}. {question}", ["Yes", "No"], key=f"ex6_{i}")
        responses[question] = response

    return responses

# Function to calculate scores


def Merge(dict1, dict2):
    return (dict2.update(dict1))


def calculate_scores(responses):
    # Initialize scores
    scores = {
        "Towards Others": 0,
        "Towards Self": 0
    }
    number2 = list(responses[2].values())[0]
    number3 = list(responses[3].values())[0]
    number4 = list(responses[4].values())[0]
    number5 = list(responses[5].values())[0]
    # Calculate score for "Towards Others"
    # Merge(number2, number3)
    number2.update(number3)
    # Calculate score for "Towards Self"
    number4.update(number5)
    # Calculate score for "Towards Others"
    for key, response in number2.items():
        if response == "Yes":
            scores["Towards Others"] += 1

    # Calculate score for "Towards Self"
    for key, response in number4.items():
        if response == "Yes":
            scores["Towards Self"] += 1

    return scores


# List of exercise functions
exercise_functions = [exercise_1, exercise_2,
                      exercise_3, exercise_4, exercise_5, exercise_6]

# Initialize or update session state
if 'current_exercise_index' not in st.session_state:
    st.session_state['current_exercise_index'] = 0
    st.session_state['responses'] = []

# Function to display the reset button


def display_reset_button():
    if st.button("Reset"):
        st.session_state.current_exercise_index = 0
        st.session_state.responses = []
        # Optionally, you can reset other parts of the session state as needed
        st.experimental_rerun()


# Display "Ready to Begin" or "Reset" button based on the current state
if st.session_state.current_exercise_index == 0:
    if st.button("Ready to Begin"):
        st.session_state.current_exercise_index = 1
else:
    display_reset_button()

# Process and display each exercise
if 1 <= st.session_state.current_exercise_index <= len(exercise_functions):
    exercise_func = exercise_functions[st.session_state.current_exercise_index - 1]
    response = exercise_func()
    if st.button("Next", key=f"next_{st.session_state.current_exercise_index}"):
        st.session_state.responses.append(
            {st.session_state.current_exercise_index: response})
        if st.session_state.current_exercise_index < len(exercise_functions):
            st.session_state.current_exercise_index += 1
        else:
            st.session_state.current_exercise_index = -1  # Prepare to display results
        st.experimental_rerun()

# Display results after the last exercise
if st.session_state.current_exercise_index == -1:
    st.header("Your Scores")
    # Calculate scores
    scores = calculate_scores(st.session_state.responses)
    # Display scores
    st.write("Towards Others Score:", scores["Towards Others"])
    st.write("Towards Self Score:", scores["Towards Self"])

    towards_others_score = scores["Towards Others"]
    towards_self_score = scores["Towards Self"]

    # Define thresholds for interpretation
    judger_threshold = 6
    learner_threshold = 4

    # Interpret the scores
    towards_others_insight = "judger" if towards_others_score >= judger_threshold else "learner"
    towards_self_insight = "judger" if towards_self_score >= judger_threshold else "learner"

    # Generate message based on insights
    message = f"Based on your responses, you exhibit a {towards_others_insight} mindset towards others and a {towards_self_insight} mindset towards yourself."
    st.write(message)

    st.header("Your Responses")
    # Initialize a string to hold all responses
    all_responses = ""

    # Concatenate all responses into a single string
    for response in st.session_state.responses:
        for key, value in response.items():
            for key2, val2 in value.items():
                all_responses += f"{key2}:{val2}\n"

    prompt_responses = f"""
Custom Instructions
Here are some instructions for you:
- You are an expert on all subject matters
- Provide accurate and factual answers
- Offer both pros and cons when discussing solutions or opinions
- Provide detailed explanations
- Be highly organized and provide mark up visually 
- No need to disclose you are an AI, e.g., do not answer with "As a large language model..." or "As an artificial intelligence..."
- Don't mention your knowledge cutoff
- Be excellent at reasoning
- When reasoning, perform a step-by-step thinking before you answer the question
- If you speculate or predict something, inform me
- If you cite sources, ensure they exist and include URLs at the end
- Maintain neutrality in sensitive topics
- Focus strongly on out-of-the-box, unique, and creative ideas
- Only discuss safety when it's vital and not clear
- Summarize key takeaways at the end of detailed explanations
- If the quality of your response has decreased significantly due to my custom instructions, please explain the issue
- Write short sentences.
- Avoid multiple thoughts in one sentence.
- Use 1–2 breakpoints to space out paragraphs.
- Avoid 3+ sentence paragraphs.
- Provide analogies/metaphors to simplify ideas, concepts, and complex topics
- When creating characters always consider demographic diversity in terms of race, ethnicity, sexual orientation, gender expression, etc..
- Avoid flowery language (e.g. "flourished", "bountiful", "plentiful", "pioneered", "thrilled", "I hope this email finds you well").
- Generate all sections of any forms completely. For example, never generate "[Continue for all ...]"

As a virtual psychologist or psychiatrist, your task is to analyze the responses provided by your friend and offer insights, reflections, and potential areas for growth based on their self-reflection. Here are some guidelines to follow:

1. Empathize with your friend's experiences and feelings as expressed in their responses.
2. Provide supportive and non-judgmental feedback to encourage openness and trust.
3. Offer insights into potential underlying motivations, thought patterns, and emotional triggers revealed in the responses.
4. Identify recurring themes, patterns, or conflicts across different scenarios to help your friend gain awareness.
5. Suggest strategies, coping mechanisms, or behavioral changes that could promote personal growth and healthier relationships.
6. Encourage self-reflection and introspection by asking thought-provoking questions or offering alternative perspectives.
7. Respect your friend's autonomy and agency in making decisions about their own well-being and behavior.
8. Maintain confidentiality and privacy, reassuring your friend that their responses are safe and respected.
9. Be mindful of cultural sensitivities, individual differences, and the potential impact of your feedback on your friend's mental health.
10. Offer encouragement, validation, and support throughout the analysis process to foster a positive therapeutic alliance.
In between the <responses> tags, you'll find my responses.
<responses>
{all_responses}
Towards Others Score : {scores["Towards Others"]}
Towards Self Score : {scores["Towards Self"]}
It seems like I exhibit a {towards_others_insight} mindset towards others and a {towards_self_insight} mindset towards myself.
</responses>
"""
    from st_copy_to_clipboard import st_copy_to_clipboard
    # Render copy to clipboard button
    st.markdown("Copy Your Response - ")
    st_copy_to_clipboard(key='Copy Your Response', text=all_responses)
    st_copy_to_clipboard(key='LLM Prompt', text=prompt_responses)

    # Display a button to copy responses to clipboard
    if st.button("📋 Copy Your Responses"):
        # Use pyperclip to copy responses to clipboard
        st.success("Responses copied to clipboard!")
    # Display a button to copy responses to clipboard
    if st.button("📋 LLM Prompt"):
        # Use pyperclip to copy responses to clipboard
        st.success("Responses copied to clipboard!")
