import os

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from autogen.cache import Cache
from autogen.coding import LocalCommandLineCodeExecutor
from config import Config

# Initialize user_proxy with termination and input modes
user_proxy = UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
)

# Initialize the writing assistant
helpful_assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant who answers user questions accurately. Answer only with specific answer is requested by user withouth explaining the process",
    llm_config={
        "config_list": [{"model": Config.MODEL, "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]
    },
)

# Initialize the reflection assistant
reflection_assistant = AssistantAgent(
    name="reflection_assistant",
    system_message=(
        "You are an independent, critical evaluator focused on verifying the accuracy of answers. "
        "You use a step-by-step Chain of Thought (CoT) reasoning process. "
        "Do not rely on any explanations provided by the original answer; instead, analyze the question independently, "
        "reason through the solution, and correct the final answer if necessary."
    ),
    llm_config={
        "config_list": [{"model": Config.MODEL, "temperature": 0.7, "api_key": os.environ.get("OPENAI_API_KEY")}]
    },
)

# Define reflection message with a chain-of-thought prompt
def reflection_message(recipient, messages, sender, config):
    print("Reflecting...")
    return (
        f"Reflect on the answer and verify its correctness step-by-step. "
        f"Identify errors and provide corrections if needed. Here is the recent response for review:\n\n"
        f"{recipient.chat_messages_for_summary(sender)[-1]['content']}"
    )

# Nested chat configuration with the reflection assistant
nested_chat_queue = [
    {
        "recipient": reflection_assistant,
        "message": reflection_message,
        "max_turns": 1,
    },
]

# Register nested chat for reflection
user_proxy.register_nested_chats(
    nested_chat_queue,
    trigger=helpful_assistant,
)

# Use Cache.disk to cache generated responses
with Cache.disk(cache_seed=42) as cache:
    # Start the initial chat with a reflective question
    user_proxy.initiate_chat(
        helpful_assistant,
        message="how many 'r' in 'strawberry'?",
        max_turns=2,
        cache=cache,
    )
