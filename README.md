[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&repo=pamelafox%2Fsimple-fastapi-azure-function)

This repository includes a very simple Python FastAPI HTTP API, made for demonstration purposes only.

## Local development: FastAPI

1. Open this repository in Github Codespaces or VS Code with Remote Dev Containers extension.
2. Open the Terminal and navigate to the `api` directory.

```console
cd api
```

2. Use [uvicorn](https://www.uvicorn.org/) to run the FastAPI app:

```console
uvicorn main:app --reload --port=8000
```

3. Click 'http://127.0.0.1:8000' in the terminal, which should open the website in a new tab.
4. Append `/generate_name` to the end of the URL.

## Local development: Azure Functions

Since this project is designed to be deployed to Azure Functions,
you can also use the local emulator from Azure Functions Core Tools
to test the function locally. 
⚠️ If you're on an Apple M1/M2, the function emulator will [probably not work](https://github.com/Azure/azure-functions-python-worker/issues/915).

1. Open this repository in Github Codespaces or VS Code with Remote Devcontainers extension.
2. Open the Terminal and make sure you're in the root folder (`simple-fastapi-azure-function`).
2. Run `func host start`
3. Click 'http://localhost:7071/{*route}' in the terminal, which should open the website in a new tab.
4. Change the URL to navigate to either the API at `/generate_name` or the docs at `/docs`.

## Deployment

This repo is set up for deployment to Azure Functions plus Azure API Management,
using `azure.yaml` and the configuration files in the `infra` folder.

Steps for deployment:

1. Sign up for a [free Azure account](https://azure.microsoft.com/free/)
2. Install the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd). (If you open this repository in Codespaces or with the VS Code Dev Containers extension, that part will be done for you.)
3. Navigate back to the root folder (the one with `azure.yaml`) if you're not already there.
2. Login to Azure:

    ```shell
    azd auth login
    ```

3. Provision and deploy all the resources:

    ```shell
    azd up
    ```

    It will prompt you to provide an `azd` environment name (like "django-app"), select a subscription from your Azure account, and select a location (like "eastus"). Then it will provision the resources in your account and deploy the latest code.

4. Once it finishes deploying, find the endpoint URL in the terminal and navigate to that URL, appending either `/generate_name` or `/docs`.

5. When you've made any changes to the app code, you can just run:

    ```shell
    azd deploy
    ```