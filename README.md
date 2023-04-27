This repository includes a very simple Python FastAPI HTTP API, made for demonstration purposes only.

## Local development

1. Open this repository in Github Codespaces or VS Code with Remote Dev Containers extension.

2. Use [uvicorn](https://www.uvicorn.org/) to run the FastAPI app:

```console
uvicorn api.main:app --reload --port=8000
```

3. Click 'http://127.0.0.1:8000' in the terminal, which should open the website in a new tab.
4. Append `/docs` or `/generate_name` to the end of the URL.
