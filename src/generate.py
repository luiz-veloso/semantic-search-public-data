import requests

def generate_answer(query, contexts):
    context_text = "\n\n".join(contexts)

    prompt = f"""
Você é um assistente que responde com base em contratos públicos.

Use apenas as informações abaixo para responder.

Pergunta:
{query}

Contratos:
{context_text}

Resposta objetiva:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma2",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
    )

    return response.json()["response"]