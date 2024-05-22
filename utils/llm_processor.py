import llm.llama3_8b_instruct
from utils import error_response
import llm

supported_llm_types = ["llama3"]


def query_length_validation(query):
    if len(query) > 400:
        return False
    else:
        return True


def llm_type_validation(llm_type):
    if llm_type not in supported_llm_types:
        return False
    else:
        return True


def llm_factory(llm_type, query):
    if llm_type == "llama3":
        return llm.llama3_8b_instruct.llama_3_8b_instruct(query)


def llm_common_processor(llm_type, query):
    if query_length_validation(query):
        if llm_type_validation(llm_type):
            # Process the query
            result = llm_factory(llm_type, query)
            return result
        else:
            return error_response.llm_type_error(False)
    else:
        return error_response.query_length_error(False)