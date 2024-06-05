# **Store-API**

![License](https://img.shields.io/github/license/Henrique-BL/dio-store-api) ![Version](https://img.shields.io/github/v/release/Henrique-BL/dio-store-api)

## **Description**

This projects it's a basic API to register products. Following the Test Driven Development, the API was developed with total focus on minimize the possible erros and exceptions it could generate.


## **Technologies Used**

- **Programming Language:** ![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **Frameworks:** ![FastAPI](https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white)
- **Libraries:** ![Pydantic](https://img.shields.io/badge/pydantic-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Motor](https://img.shields.io/badge/motor-013243?style=for-the-badge&logo=mongodb&logoColor=white) ![HTTPX](https://img.shields.io/badge/httpx-61DAFB?style=for-the-badge&logo=http&logoColor=black)
- **Tools:** ![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white) ![Pre-commit](https://img.shields.io/badge/pre--commit-00BFFF?style=for-the-badge&logo=pre-commit&logoColor=white)
- **Testing:** ![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white) ![Pytest-Asyncio](https://img.shields.io/badge/pytest--asyncio-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
- **Server:** ![Uvicorn](https://img.shields.io/badge/uvicorn-009688?style=for-the-badge&logo=python&logoColor=white)


## **Main Features**
**TESTS**
- **USECASES:** Unit usecases test of CreateSucess, UpdateSucess, DeleteSucess, DeleteFailed, QuerySucess, and GetSucess tests .
- **CONTROLLER:** Integration Tests using FastAPI and Uvicorn.
- **SCHEMAS:** Unit schemas tests of sucess and error.

## **How to Use**

This project depends on **pyenv** and **poetry** to work properly, for that it'll be necessary to use a virtual machine that runs Linux, if you're using Windows I recommend WSL.

1. **Install Packages:**

   **Pyenv**
     Follow instructions: https://github.com/pyenv/pyenv?tab=readme-ov-file#unixmacos

   **Poetry**

    ```bash
    pip install poetry

2. **Install Dependencies**

    ```bash
    pyenv local 3.12
    poetry env use 3.12
    poetry install

3. **Run Tests**

    The following command will run all tests
    ```bash

    make test

    ```

    The following command will run only the test passed as argument to K

    ```bash

    make test-matching K=test_schemas_sucess



## **Makefile commands**

1.  The following command will install pre-commit it's useful to maintain some coding pattern

    ```bash

    make  pre-commit install

    ```
2.  The following command will put the server up, you can acess it with localhost/8000/docs

    ```bash

    make  run

    ```
