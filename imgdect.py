import ollama

res=ollama.chat(
    model='llava',
    messages=[
        {
            'role':'user',
            'content':'Describe this image',
            'images':['sign.png']}
    ]
)

print(res['message']['content'])