from config import OPENAI_API_KEY,GPT_MODEL,TEMPERATURE,MAX_TOKENS
from openai import OpenAI

class ModelService:
    def __init__(self) -> None:
        self.client=OpenAI(api_key=OPENAI_API_KEY)
    """
        crear una funcion text input y text output
    """
    def predict(self,prompt):
        temperatura=TEMPERATURE
        max_tokens=MAX_TOKENS
        model=GPT_MODEL
        r=self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "tu eres un asistente virtual"},
                {"role": "user", "content": prompt}
            ],
            temperature=temperatura,
            max_tokens=max_tokens
        )
        response={
            "result":r.choices[0].message.content,
            "model":model,
            "max_tokens":max_tokens,
            "temperature":temperatura
        }
        return response
        


    """
        crear una funcion text input y image output
    """

    def image(self, prompt):
        size="1024x1024"
        #client_image=OpenAI(api_key="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")

        r=self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size=size
        )
        return {
            "url":r.data[0].url,
            "n":1,
            "size":size
        }




