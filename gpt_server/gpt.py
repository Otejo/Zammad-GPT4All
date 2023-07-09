from gpt4all import GPT4All

#choose the model you want to use
model = GPT4All('nous-hermes-13b.ggmlv3.q4_0.bin')

def get_answer(prompt):
    with model.chat_session():
        tokens = list(model.generate(prompt=prompt, streaming=True))
        model.current_chat_session.append({'role': 'assistant', 'content': ''.join(tokens)})
        answer = model.current_chat_session[1].get('content')
    return answer
