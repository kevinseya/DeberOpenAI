import openai
from pydantic import BaseModel

class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:
    openai.organization = 'org-PYELIbA8LxpnGFiTsMHVkbOV'
    openai.api_key = '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'

    print('[PROCESANDO]'.center(40,'-'))
    completion = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Profesor de programación a nivel universitario"""},
            {"role": "user", "content": prompt}
        ]
    )

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print('[SE TERMINO DE PROCESAR]'.center(40, '-'))
    print('[RESULTADO]'.center(40, '-') + content +
          "\n***El número de token es: " + str(total_tokens)+
          "\n***El prompt introducido es: "+prompt)
    return [content, total_tokens]