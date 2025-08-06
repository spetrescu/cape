import requests
import base64

def encode_image_to_base64(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
        if path.lower().endswith(".png"):
            mime_type = "image/png"
        else:
            mime_type = "image/jpeg"
        return f"data:{mime_type};base64,{encoded}"

image_paths = ["images_health_check/controller_1.jpg", "images_health_check/controller_2.jpg"]

encoded_images = [encode_image_to_base64(path) for path in image_paths]

url = "http://localhost:5005/query"
headers = {"Content-Type": "application/json"}
data = {
    "text": "Briefly describe each attached image espectially for potential debugging and system diagnosis.",
    "images": encoded_images
}

response = requests.post(url, headers=headers, json=data)

if response.ok:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
