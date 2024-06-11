# LLM API Integrator

## Introduction

Welcome to the LLM API repository! This project is designed to facilitate the deployment and interaction with multiple large language models (LLMs) from industry leaders such as OpenAI, Meta (Llama), Microsoft (Phi-3), and MistralAI. By leveraging Hugging Face's deployment integrations, this API allows you to query different LLMs without the need to manage deployments or invest in costly GPU resources.

## Features

- **Multiple LLM Support**: Easily switch between different models like OpenAI's GPT, Meta's Llama, Microsoft's Phi-3, and MistralAI.
- **Simple API Interface**: A unified API endpoint to send queries and receive responses from the selected LLM.
- **No Infrastructure Hassle**: All backend processes, including model management and scaling, are handled automatically.
- **Rapid Integration**: Integrate with existing systems or applications quickly through our straightforward API endpoints.

## API Documentation

### Base URL

All API requests should be made to the following base URL (Present on Rapid API):

- https://llm-api1.p.rapidapi.com


### Endpoints

#### LLM Chat

- **Endpoint**: `/v0/llmchat`
- **Method**: POST
- **Description**: Send a text query to a specified LLM and receive a generated text response.

##### Request Headers

- `Content-Type`: application/json
- `x-rapidapi-key`: `Your-RapidAPI-Key`

##### Request Body

| Parameter | Type   | Description                                          |
|-----------|--------|------------------------------------------------------|
| llm_model | string | The name of the language model to use (e.g., llama3). |
| query     | string | The text query you want to send to the model.         |

##### Example Request

```bash
curl --location 'https://llm-api1.p.rapidapi.com/v0/llmchat' \
--header 'Content-Type: application/json' \
--header 'x-rapidapi-key: Your-RapidAPI-Key' \
--data '{
    "llm_model": "llama3",
    "query": "Give me a story of Batman and Robin set in 1994 in 2 lines"
}'
```

##### Response

The response will be in JSON format containing the generated text based on the provided query.

| Parameter | Type   | Description                                |
|-----------|--------|--------------------------------------------|
| status    | string | Status of the response (e.g., ok, error)    |
| response  | string | The generated text response from the model.|

##### Example Response

```json
{
    "status": "ok",
    "response": "It was a hot summer night in 1994 when Batman and Robin received a distress call from the Gotham City Police Department, alerting them to a massive rave party being held in an abandoned warehouse on the waterfront, with rumors of a mysterious DJ known only as 'The Darkstar' spinning tracks that were making the crowd go wild. As they swooped in to shut down the party, they were met with a sea of glow sticks and flannel shirts, and Robin's eyes widened in surprise as he spotted a familiar face in the crowd - none other than his nemesis, the Riddler, spinning tracks behind the decks."
}
```

#### Supported LLMs in v1

    llama3

#### Upcoming LLMs in v1.1

    MistralAI
    MicrosoftPhi
    OpenAI

Getting Started

To begin using the LLM API, you'll need to sign up for a RapidAPI account and subscribe to our service to obtain your API key. Once you have your API key, you can start making requests to the API using the provided endpoints.
Thank You

Thank you for choosing LLM API! We are committed to providing you with a high-quality service that meets your needs and exceeds your expectations. If you have any questions or feedback, please do not hesitate to contact or raise an issue.
