from gradio_client import Client
from huggingface_hub import login
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread


def llama_3_8b_instruct(query):
    result = model_call(query)
    return {"status": "ok", "response": result}


def model_call(query):
    client = Client("namanvats/Chat_with_Meta_llama3_8b")
    job = client.submit(
            message=query,
            request=0.95,
            param_3=512,
            api_name="/chat",
    )
    return result_parser(job.result())


def result_parser(result):
    result = result.strip()
    if result.startswith("assistant"):
        result = result[len("assistant\n\n"):]
    result = result.lstrip('\n')
    return result