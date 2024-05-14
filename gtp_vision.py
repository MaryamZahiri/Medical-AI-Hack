from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def image_content(img_url):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Do you reccomed this food to a diabetes person? Just Answer ```YES``` or ```NO```. \
                    If there are more than one foods, name each one and for each put your reccomendation, like food1: ```YES``, food2: ```NO``."},
            {
            "type": "image_url",
            "image_url": {
                "url": img_url,
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    print(response.choices[0])