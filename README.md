# AI-CHATBOT-WITH-NLP

***COMPANY*:** CODTECH IT SOLUTIONS

***NAME*:** DHIVYA SHREE M

***INTERN ID*:** CT04DF78

***DOMAIN*:** PYTHON

***DURATION*:** 4 WEEKS

***MENTOR*:** NEELA SANTHOSH

## DESCRIPTION
### INTRODUCTION  
This task involves the creation of an intelligent chatbot using Python, incorporating Natural Language Processing (NLP) techniques to enhance user interaction. The chatbot is designed to handle basic conversations, answer questions, provide time/date information, and respond dynamically to user inputs. The implementation leverages multiple NLP and machine learning libraries to improve text understanding and generate meaningful responses.

### TABLE OF CONTENTS  
1. [INTRODUCTION](#introduction)
2. [TOOLS AND LIBRARIES USED](#tools-and-libraries-used)
3. [EDITOR AND PLATFORM COMPATIBILITY](#editor-and-platform-compatibility)
4. [FUNCTIONALITY AND WORKFLOW](#functionality-and-workflow)
5. [APPLICATION AND USE CASES](#applications-and-use-cases)
6. [ADVANTAGES OF THIS APPROACH](#advantages-of-this-approach)
7. [OUTPUT](#output)
8. [CONCLUSION](#conclusion)
   
### TOOLS AND LIBRARIES USED  
The chatbot is built using the following Python libraries and frameworks:

**1. Natural Language Toolkit (NLTK)**  
**- nltk.chat.util** → Provides a rule-based chatbot framework with predefined response patterns.

**- nltk.download('punkt')** → Used for tokenization (splitting text into words/sentences).

**- nltk.download('wordnet')** → Enables lemmatization (reducing words to their base forms).

**2. spaCy**  
- A powerful NLP library used for advanced text preprocessing.

- en_core_web_sm – A pre-trained English language model for tokenization, lemmatization, and stopword removal.

- Helps in understanding user intent by analyzing sentence structure.

**3. Python Standard Libraries**  
**datetime** → Used to fetch and display the current time and date.

**random** → Helps in selecting random responses for a more dynamic conversation.

**subprocess** → Ensures the spaCy language model is downloaded if missing.

### EDITOR AND PLATFORM COMPATIBILITY  
This chatbot can be developed and executed in various environments:

**1. Integrated Development Environments (IDEs)**  
- **VS Code** → Excellent for debugging and testing with Python extensions.

- **PyCharm** → Provides advanced code analysis and NLP toolkit integrations.

- **Jupyter Notebook / JupyterLab** → Useful for interactive testing and NLP experimentation.

**2. Cloud-Based Platforms**  
- **Google Colab** → Allows running the chatbot without local installations.

- **Replit** → A browser-based IDE for quick deployment and sharing.

### FUNCTIONALITY AND WORKFLOW  
The chatbot follows a structured interaction flow:

**1. Initialization**  
- Downloads necessary NLTK datasets (punkt, wordnet).
- Loads the spaCy English language model (en_core_web_sm).

**2. Predefined Response Pairs**  
- The chatbot uses pattern-response pairs to match user inputs with answers.

**3. Text Preprocessing**  
- Converts text to lowercase.
- Removes stop words (e.g., "the", "is") and punctuation.
- Uses lemmatization to normalize words (e.g., "running" → "run").

**4. Dynamic Response Handling**  
- If no direct match is found, the chatbot reprocesses the input using NLP techniques.
- Falls back to a default response if the query is still unrecognized.

**5. Contextual Features**  
- Time/Date Awareness – Responds to "What time is it?" or "Today's date?".
- Exit Handling – Recognizes "quit," "bye," or "exit" to end the conversation.

**6. Interactive Chat Loop**  
- Continuously prompts the user for input.
- Processes each query and generates a response until the user exits.

### Applications and Use Cases  
This chatbot can be applied in various domains:

**1. Customer Support**  
- E-commerce websites – Handles FAQs about orders, returns, and products.
- Banking – Answers queries about account balances, transactions, and policies.

**2. Healthcare Assistance**  
- Symptom checking – Provides basic medical advice (with proper integration).
- Appointment scheduling – Interacts with patients to book doctor visits.

**3. Education & E-Learning**  
- Tutoring bots – Answers student questions on coursework.
- Language learning – Engages in conversational practice.

**4. Business Automation**  
- HR chatbots – Assists employees with leave requests and policies.
- IT helpdesk – Resolves common technical issues.

**5. Smart Home & IoT**  
- Voice assistants – Can be extended to work with Alexa/Google Home.
- Home automation – Responds to commands like "Turn on lights."

### Advantages of This Approach  
- Rule-Based + NLP Hybrid → Combines structured responses with machine learning for better understanding.

- Lightweight & Fast → Doesn’t require heavy AI models like GPT-3.

- Customizable Responses → Easy to modify or expand response pairs.

- No Internet Dependency → Works offline once dependencies are installed.

### OUTPUT
![Image](https://github.com/user-attachments/assets/ca8b026d-bb5e-48b8-b872-9df87e651671)

### CONCLUSION
This NLP-enhanced chatbot demonstrates how rule-based systems and machine learning can work together to create an interactive virtual assistant. Its applications span across industries, from customer service to healthcare, making it a versatile tool for automated communication.

By improving its language understanding and response accuracy, this chatbot can evolve into a fully functional AI assistant capable of handling complex queries. Whether used in business automation or personal projects, it serves as a foundation for intelligent conversational agents.
