import requests
import threading

def d_d_d(url, results, index):
    try:
        response = requests.get(url)
        results[index] = f"{url} -> {response.status_code}"
    except Exception as e:
        results[index] = f"{url} -> Fehler: {e}"

def main():
    url = "https://www.wilhelm-fredemann-obs.de/"
    num_threads = 250
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=d_d_d, args=(url, results, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results
