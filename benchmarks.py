import time
import requests
import psutil

url = "http://127.0.0.1:8080/completion"

payload = {
    "prompt": "Explain what cybersecurity is in one paragraph.",
    "n_predict": 200,
    "temperature": 0.7
}

start = time.time()

try:
    response = requests.post(url, json=payload)
    elapsed = time.time() - start

    print("Status Code:", response.status_code)
    print("\nRaw Response:")
    print(response.text)
    print("-" * 60)

    response.raise_for_status()

    data = response.json()

    text = data.get("content", "")
    timings = data.get("timings", {})

    tokens = timings.get("predicted_n", 0)

    if tokens == 0 and text:
        tokens = len(text.split())

    tps = tokens / elapsed if elapsed > 0 else 0
    ram = psutil.virtual_memory().used / (1024 ** 3)

    print("\n===== Benchmark Results =====")
    print(f"Generated Text  : {text}")
    print(f"Generated Tokens: {tokens}")
    print(f"Elapsed Time    : {elapsed:.2f} s")
    print(f"Tokens / Second : {tps:.2f}")
    print(f"RAM Used        : {ram:.2f} GB")

    if timings:
        print("\n===== Timings =====")
        for key, value in timings.items():
            print(f"{key}: {value}")

except requests.exceptions.RequestException as e:
    print("Request Error:")
    print(e)
except ValueError:
    print("The server did not return valid JSON.")