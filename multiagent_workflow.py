import os
import autogen

# Ensure your OpenAI API key is set in the environment variables
api_key = os.environ.get("OPENAI_API_KEY")
model="gpt-4o"

if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

gpt4_config = {
    "cache_seed": 43,  # Change the cache_seed for different trials
    "temperature": 0,
    "config_list": [
        {
            "model": model,
            "api_key": api_key,
        }
    ],
    "timeout": 120,
}

# Define the agents
initializer = autogen.UserProxyAgent(
    name="Init",
    system_message="You are the Initializer. Start the workflow by providing a topic for research.",
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=gpt4_config,
    system_message=(
        "You are the Coder. Given a topic, write Python code to retrieve related papers from the arXiv API. "
        "Print their title, authors, abstract, and link. Ensure the code is complete and executable without "
        "requiring modifications."
    ),
)

executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="You are the Executor. Execute the code provided by the Coder and report the results.",
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "paper",
        "use_docker": True,  # Set to True if Docker is available for safer code execution
    },
)

scientist = autogen.AssistantAgent(
    name="Scientist",
    llm_config=gpt4_config,
    system_message=(
        "You are the Scientist. After receiving the paper details, categorize them and create a markdown table "
        "with the following columns: Domain, Title, Authors, Summary, and Link."
    ),
)

# Define the custom speaker selection function
def custom_speaker_selection_func(
    last_speaker: autogen.Agent,
    groupchat: autogen.GroupChat
):
    """Determine the next speaker based on the last speaker and the current state of the group chat."""
    if last_speaker is initializer:
        return coder
    elif last_speaker is coder:
        return executor
    elif last_speaker is executor:
        # Check the last message content to determine if execution was successful
        last_message = groupchat.messages[-1]["content"].lower()
        if "error" in last_message or "failed" in last_message:
            return coder  # Retry coding if execution failed
        else:
            return scientist
    elif last_speaker is scientist:
        # Write the Scientist's final output to a file
        final_result = groupchat.messages[-1]["content"]
        with open("scientist_final_result.md", "w") as file:
            file.write(final_result)
        print("Final result written to scientist_final_result.md")
        return None  # End the workflow
    else:
        return 'auto'  # Default to automatic selection

# Initialize the group chat with the agents and custom speaker selection function
groupchat = autogen.GroupChat(
    agents=[initializer, coder, executor, scientist],
    messages=[],
    max_round=20,
    speaker_selection_method=custom_speaker_selection_func,
)

# Create a manager for the group chat
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

# Start the conversation by having the initializer provide a topic

topic=input("¿Sobre que quieres investigar?: ")

initializer.initiate_chat(
    manager,
    message=f"Topic: {topic}",
)
