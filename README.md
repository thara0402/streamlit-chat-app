# Streamlit Chat App

## Setup
### .env
```json
AZURE_OPENAI_API_KEY="xxx"
AZURE_OPENAI_ENDPOINT="https://xxx.openai.azure.com/"
AZURE_OPENAI_API_VERSION="yyyy-mm-dd-preview"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
```

## Development
### Create an environment using venv
```shell-session
$ cd stream-chat-app
$ python -m venv .venv
```

### Activate environment
```shell-session
$ .venv\Scripts\activate.bat
```

### Install Streamlit in environment
```shell-session
$ pip install streamlit
```

### Run Streamlit app
```shell-session
$ streamlit run app.py
```

### Return to normal shell
```shell-session
$ deactivate
```
