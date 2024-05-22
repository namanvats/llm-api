def query_length_error(validation_status):
    if validation_status is False:
        return {"status": "error", "message": "Query is too long to process"}
    

def llm_type_error(validation_status):
    if validation_status is False:
        return {"status": "error", "message": "LLM type is not supported"}