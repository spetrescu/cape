from flask import Flask, request, jsonify
from transformers import pipeline
import torch
import time
import threading
import sys

app = Flask(__name__)

print("Loading Gemma 3n...")
pipe = pipeline(
    "image-text-to-text",
    model="google/gemma-3n-E2B-it",
    device="cpu",
    torch_dtype=torch.bfloat16
)

# Progress bar function (~400s max fill time)
def progress_bar(stop_event, total_duration=400):
    bar_length = 40
    start_time = time.time()
    while not stop_event.is_set():
        elapsed = time.time() - start_time
        progress = min(elapsed / total_duration, 1.0)
        filled_len = int(bar_length * progress)
        bar = "=" * filled_len + "-" * (bar_length - filled_len)
        percent = int(progress * 100)
        print(f"\r⏳ Processing... [{bar}] {percent}%", end="", flush=True)
        if progress >= 1.0:
            break
        time.sleep(0.5)
    if stop_event.is_set():
        bar = "=" * bar_length
        print(f"\rProcessing... [{bar}] 100%", flush=True)

@app.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        text = data.get("text")
        image_urls = data.get("images", [])

        if not text or not image_urls:
            return jsonify({"error": "'text' and 'images' fields are required"}), 400

        print("\n🕒 Processing started...", flush=True)
        start_time = time.time()

        stop_event = threading.Event()
        thread = threading.Thread(target=progress_bar, args=(stop_event,))
        thread.start()

        content = [{"type": "image", "url": url} for url in image_urls]
        content.append({"type": "text", "text": text})
        messages = [{"role": "user", "content": content}]

        output = pipe(text=messages, max_new_tokens=256)
        result = output[0]["generated_text"][-1]["content"]

        elapsed = time.time() - start_time

        stop_event.set()
        thread.join()

        print(f"\nProcessing completed in {elapsed:.2f} seconds", flush=True)

        return jsonify({
            "response": result,
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5005)
