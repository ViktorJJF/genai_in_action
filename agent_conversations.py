from config import Config

import os
from autogen import ConversableAgent

Oliver = ConversableAgent(
    "Oliver",
    system_message="Your name is Oliver and you are a part of a duo of comedians. Speak in spanish",
    llm_config={"config_list": [{"model": Config.MODEL, "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

Juan = ConversableAgent(
    "Juan",
    system_message="Your name is Juan and you are a part of a duo of comedians. Speak in spanish",
    llm_config={"config_list": [{"model": Config.MODEL, "temperature": 0.7, "api_key": os.environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",  # Never ask for human input.
)

result = Juan.initiate_chat(Oliver, message="Oliver, cuentame un chiste", max_turns=3)