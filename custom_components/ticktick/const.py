"""Constants for the TickTick Integration integration."""

DOMAIN = "ticktick"

OAUTH2_AUTHORIZE = "https://ticktick.com/oauth/authorize"
OAUTH2_TOKEN = "https://ticktick.com/oauth/token"
DEFAULT_API_ENDPOINT = "https://api.ticktick.com"
API = "open/v1"
CONF_API_ENDPOINT = "api_endpoint"

# === Parameters === #
PROJECT_ID = "projectId"
TASK_ID = "taskId"

# === Endpoints === #

# === Task Scope ===
GET_TASK = f"{API}/project/{{{PROJECT_ID}}}/task/{{{TASK_ID}}}"
CREATE_TASK = f"{API}/task"
UPDATE_TASK = f"{API}/task/{{{TASK_ID}}}"
COMPLETE_TASK = f"{API}/project/{{{PROJECT_ID}}}/task/{{{TASK_ID}}}/complete"
DELETE_TASK = GET_TASK

# === Project Scope ===
GET_PROJECTS = f"{API}/project"
GET_PROJECTS_WITH_TASKS = f"{API}/project/{{{PROJECT_ID}}}/data"
