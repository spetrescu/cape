# 🦸 CAPE

This guide walks you through installing and running Cape. There are essentially three main stages for fully deploying Cape:
1. Configuring the OpenWebUI-based Frontend (step 1/3) - by this point you'll not be able to interface yet locally with Gemma3n
2. Configuring the UI OpenWebUI Backend and Ollama (step 2/3) - by this point you'll be able to interface locally with Gemma3n (text only)
3. Configuring a custom inference server that hosts Gemma3n in full precision via HuggingFace (step 3/3) - at this point Cape will be able to use Gemma3n locally to process images and videos

## Prerequisites
Make sure the following tools are installed on your system:

- [Conda](https://docs.conda.io/en/latest/miniconda.html)
- [Node.js + npm](https://nodejs.org/) (v16 or higher)
- [ollama](https://ollama.com/download)

## 1. Configuring the OpenWebUI-based Frontend (step 1/3)
### 1.1 Clone the Repository

```bash
git clone https://github.com/spetrescu/cape.git
```

```bash
cd cape/src/ui/open-webui
```

### 1.2 Set Up Environment Variables
```bash
cp -RPp .env.example .env
```
### 1.3 Install Frontend Dependencies
Install required packages (may need `--force` to resolve version issues)
```bash
npm install --force
```
Start the frontend development server:
```bash
npm run dev
```

## 2. Configuring the UI OpenWebUI Backend and Ollama (step 2/3)
### 2.1 Set up the OpenWebUI backend
```bash
cd backend
```
Create and activate the Python environment (Python 3.11 required):
```bash
conda create --name open-webui python=3.11
conda activate open-webui
```

### 2.2 Install and make sure Ollama is running
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

### 2.3 Install Python Dependencies
From the backend directory:
```bash
pip install -r requirements.txt -U
```
Make sure the Python version in use is `3.11` (check with `python --version`).

### 2.4 Start the Backend Server
```bash
sh dev.sh
```
Navigate to `http://localhost:5173/` to see the application running. At this stage you should be able to see the following image (after you have created a user and a password):
<div align="left">
   <p>
    <img width="400" alt="mist" src="https://github.com/user-attachments/assets/fddb9c2d-6e29-4f4e-aee0-00f0380ef98a">
   </p>
 </div>

## 3. Configuring a custom inference server that hosts Gemma3n in full precision via HuggingFace (step 3/3)
- Make sure you have a working Hugging Face token (in order to download models), and that also you have applied to get access to Gemma3n models (link here: [https://huggingface.co/google/gemma-3n-E2B-it](https://huggingface.co/google/gemma-3n-E2B-it))

