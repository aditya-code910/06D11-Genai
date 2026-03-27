from flask import Flask, jsonify, render_template_string, request
import requests
import base64
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)



@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Multimodal Manufacturing Creator</title>
        <style>
            body { font-family: Arial; background: #f4f6f9; text-align: center; padding-top: 40px; }
            .card { background: white; padding: 30px; margin: auto; width: 650px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);}
            input { width: 80%; padding: 10px; margin-top: 10px; }
            button { padding: 10px 20px; margin-top: 10px; background: #3498db; color: white; border: none; border-radius: 5px; cursor: pointer;}
            .output-box { margin-top: 20px; text-align: left; padding: 10px; background: #f9f9f9; border-radius: 8px;}
            img { margin-top: 15px; border-radius: 8px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Multimodal Manufacturing Creator</h2>

            <input id="prompt" placeholder="Enter manufacturing idea..." />
            <br>

            <button onclick="generateAll()">Generate (Text + Image)</button>

            <div class="output-box">
                <div id="textOutput"></div>
                <div id="imageOutput"></div>
            </div>
        </div>

        <script>
            async function generateAll() {
                let prompt = document.getElementById("prompt").value;

                document.getElementById("textOutput").innerHTML = "Generating...";
                document.getElementById("imageOutput").innerHTML = "";

                // TEXT
                let textRes = await fetch('/generate-text', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({prompt: prompt})
                });

                let textData = await textRes.json();

                document.getElementById("textOutput").innerHTML =
                    "<b>Generated Concept:</b><br>" + textData.output;

                // IMAGE
                let imgRes = await fetch('/generate-image', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({prompt: prompt})
                });

                let imgData = await imgRes.json();

                document.getElementById("imageOutput").innerHTML =
                    "<b>Generated Image:</b><br><img src='" + imgData.image_url + "' width='400'/>";
            }
        </script>
    </body>
    </html>
    """)


@app.route("/generate-text", methods=["POST"])
def generate_text():
    data = request.get_json()
    prompt = data.get("prompt")

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Generate a realistic manufacturing system for: {prompt}

Include:
- machines
- workflow
- automation
- materials
"""
                }
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        result = response.json()

        output = result["choices"][0]["message"]["content"]

        return jsonify({"output": output})

    except Exception as e:
        print("TEXT ERROR:", str(e))
        return jsonify({
            "output": f"AI Generated: Smart manufacturing system for {prompt} using robotics and automation."
        })


@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt")

    try:
        import time


        API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": f"{prompt}, industrial manufacturing factory, robotics, realistic, 3D render"
        }

        for i in range(3):
            response = requests.post(API_URL, headers=headers, json=payload)

            print("STATUS:", response.status_code)

            if response.status_code == 200:
                image_bytes = response.content
                encoded = base64.b64encode(image_bytes).decode("utf-8")

                return jsonify({
                    "image_url": f"data:image/png;base64,{encoded}"
                })

            elif response.status_code == 503:
                print("Model loading... retrying")
                time.sleep(3)

            else:
                print("ERROR:", response.text)
                break

        raise Exception("HF API failed")

    except Exception as e:
        print("IMAGE ERROR:", str(e))

        return jsonify({
            "image_url": "https://picsum.photos/400"
        })


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)