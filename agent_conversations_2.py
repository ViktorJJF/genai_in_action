from config import Config

import os
from autogen import ConversableAgent

Oliver = ConversableAgent(
    "Oliver",
    system_message="Your name is Oliver and you are a cat lover. Speak in spanish",
    llm_config={"config_list": [{"model": Config.MODEL, "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

Maria = ConversableAgent(
    "Maria",
    system_message="Your name is Maria and you are a dog lover. Speak in spanish",
    llm_config={"config_list": [{"model": Config.MODEL, "temperature": 0.7, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.

)

result = Oliver.initiate_chat(Maria, message="Hey Maria! los gatos son mejores mascotas", max_turns=3)