# global_state.py

LOG_PATH = ""

START_FLAG = False
FIRST_MAIN = False


EXIT_FLAG = False
INIT_FLAG = False
# WORKFLOW_FLAG = False
# AGENTCREATE_FLAS = False

# AGENT_CREATOR_AGENT_STATE = False
# META_AGENT_LAST_QUERY = ''
# WORKFLOW_CREATOR_AGENT_STATE = False
# WORKFLOW_AGENT_LAST_QUERY = ''

# container_name = 'auto_agent'
# port = 12345
# test_pull_name = 'autoagent_mirror'
# git_clone = True
PROMPT_TOKENS = 0
COMPLETION_TOKENS = 0


def reset_token_usage() -> None:
    """Reset the global counters that track LLM token consumption."""
    global PROMPT_TOKENS, COMPLETION_TOKENS
    PROMPT_TOKENS = 0
    COMPLETION_TOKENS = 0


def get_token_usage() -> dict:
    """Return the aggregated token usage recorded so far."""
    return {
        "prompt_token_count": PROMPT_TOKENS,
        "completion_token_count": COMPLETION_TOKENS,
    }

# local_env = False
