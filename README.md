# 🦸 CAPE

This guide walks you through installing and running Cape.

## Prerequisites
Make sure the following tools are installed on your system:

- [Conda](https://docs.conda.io/en/latest/miniconda.html)
- [Node.js + npm](https://nodejs.org/) (v16 or higher)
- [ollama](https://ollama.com/download)

### 1. Clone the Repository

```bash
git clone https://github.com/spetrescu/cape.git
```

```bash
cd cape/src/ui/open-webui
```

### 2. Set Up Environment Variables
```bash
cp -RPp .env.example .env
```
### 3. Install Frontend Dependencies
Install required packages (may need `--force` to resolve version issues)
```bash
npm install --force
```
Start the frontend development server:
```bash
npm run dev
```
### 4. Set Up the Backend
```bash
cd backend
```
Create and activate the Python environment (Python 3.11 required):
```bash
conda create --name open-webui python=3.11
conda activate open-webui
```

5. Install and Run Ollama
Ensure `ollama` is installed and running:
```bash
ollama serve
```
If you see this message: `Error: listen tcp 127.0.0.1:11434: bind: address already in use`, it means Ollama is already running in the background, which is exactly what you want and there is no need to run `ollama serve` again. If you want to double check that the port is indeed occupied by `ollama`, run `curl http://localhost:11434` which should return `Ollama is running`. <br>
Now, in another terminal, pull Gemma3n:e2b (5.6 GB download):
```bash
ollama pull gemma3n:e2b
```
If you have capacity on your machine you can also pull the bigger Gemma3n model, namely by running `ollama pull gemma3n:e4b` (7.5 GB download).

6. Install Python Dependencies
From the backend directory:
```bash
pip install -r requirements.txt -U
```
Make sure the Python version in use is `3.11` (check with `python --version`).

7. Start the Backend Server
```bash
sh dev.sh
```
Navigate to `http://localhost:5173/` to see the application running.

