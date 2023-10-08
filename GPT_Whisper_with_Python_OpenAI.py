# First need to create an OpenAI developer account, and add OpenAI API key as an environment variable.

# Install the langchain package
!pip install langchain==0.0.286

# Update the typing_extensions package
!pip install typing_extensions==4.7.1

# Import the os package
import os

# Import the openai package
import openai

# Set openai.api_key to the OPENAI_API_KEY environment variable
# gives permission to open OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Import the langchain package as lc
import langchain as lc

# From the langchain.chat_models module, import ChatOpenAI
from langchain.chat_models import ChatOpenAI

# From the langchain.schema module, import AIMessage, HumanMessage, SystemMessage
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# From the langchain.prompts module, import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate

# Create a ChatOpenAI object. Assign to chat.
chat = ChatOpenAI()

# Create a list of messages. Assign to msgs_what_is_llm.
msgs_what_is_llm = [
    SystemMessage(content="You are a machine learning expert who writes for an audience of ten year olds."),
    HumanMessage(content="Explain what a large language model is.")
]


# Pass your message to GPT. Assign to response_what_is_llm.
response_what_is_llm = chat(msgs_what_is_llm)

# Print the response
print(response_what_is_llm)
#shows dictionary with a content element, and shows additional arguments

print("\n----\n")

# Print the response's content
print(response_what_is_llm.content)
#shows the pertinent text

# Append the response and a new message to the previous messages. 
# Assign to msgs_what_is_llm_conversation.
msgs_what_is_llm_conversation = msgs_what_is_llm + [
    response_what_is_llm,
    HumanMessage("Why might that be useful?")
]
# context from previous conversation will help answer this question

# Pass your message to GPT. Assign to response_what_is_llm_conversation.
response_what_is_llm_conversation = chat(msgs_what_is_llm_conversation)

# Print the response's content
print(response_what_is_llm_conversation.content)

# Open the file audio-logan-gpt-plugins.mp3 as audio_file. Copied path from files
# Transcribe the file using Whisper. Assign to transcript.
# Placeholder name used for .mp3 file
with open("placeholder.mp3", "r") as audio_file: # "r" shows it's binary
    transcript = openai.Audio.transcribe( # assign to transcript
        file=audio_file,
        model="whisper-1",
        response_format="text",
        language="en" #optional, while detect but this makes it faster
    )
    
# Print the transcript.
print(transcript)

# Might get an error the first time
# Could wrap the above code into a try block for if it didn't work the first time
# Shows both voices mixed together into one text. you can distinguish between the two voices, but not be built into the API, he's not sure
# Will show ChatGPT is some sections because of the accents, clean up in next bit

# Create a list of messages. Assign to msgs_clean_transcript.
msgs_clean_transcript = [
    SystemMessage(content="You are a copywriter."),
    HumanMessage(content=f"Fix the spelling mistakes in this transcript. Pay careful attention to the name of the software, ChatGPT\n\n{transcript}.")
] # f string lets you include variables (transcript) in your string

# Pass your message to GPT. Assign to response_clean_transcript.
response_clean_transcript = chat(msgs_clean_transcript)

# Extract the content. Assign to clean_transcript.
clean_transcript = response_clean_transcript.content

# Print the cleaned transcript.
print(clean_transcript)

# Create a list of messages. Assign to msgs_summarize_transcript.
msgs_summarize_transcript = [
    SystemMessage(content="You are a helpful secretary who writes tersely."), # tersely means don't write very much at all
    HumanMessage(content=f"Create an executive summary of the following transcript.\n\n{clean_transcript}")
]

# Pass your message to GPT. Assign to response_summarize_transcript.
response_summarize_transcript = chat(msgs_summarize_transcript)

# Extract the response's contents. Assign to summarized_transcript.
summarized_transcript = response_summarize_transcript.content

# Print the summarized transcript.
print(summarized_transcript)

# Define new question. Assign to your_question.
your_question = "What's the main takeaway of this podcast in one sentence?"

# Create a list of messages. Assign to msgs_q_and_a.
msgs_q_and_a = [
    SystemMessage(content="You are a Customer Support Specialist who answers questions for customers."),
    HumanMessage(content=f"""Using the transcript to answer the question.
    Question:{your_question}
    Transcript: {summarized_transcript}""") # triple quotes allow multi line string
]

# Pass your message to GPT. Assign to response_q_and_a.
response_q_and_a = chat(msgs_q_and_a)

# Print the response's contents.
print(response_q_and_a.content)
