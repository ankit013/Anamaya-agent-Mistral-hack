from mistralai.models.chat_completion import ChatMessage
import os
from mistralai.client import MistralClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("MISTRAL_API_KEY")
client = MistralClient(api_key=api_key)
fine_tuned_model = os.environ.get("fine_tuned_model") ### Our fine tune mistral-7b model
base_model = os.environ.get("base_model") ### open-mistral-7b model


def detection_agent(message) -> str:
    """infer the fine tuned model"""
    question = message.split('Question: ')[1]
    chat_response = client.chat(
        model=fine_tuned_model,
        messages=[ChatMessage(role='user', content=message)]
    )
    response = chat_response.choices[0].message.content
    if 'Yes' in response:
        if 'stress' in question:
            return "stress",response
        elif 'depression' in question:
            return "depression",response
        elif 'spiritual wellness dimension' in question:
            return 'spiritual wellness dimension',response
        elif 'physical wellness dimension' in question:
            return 'physical wellness dimension',response
        elif 'intellectual wellness dimension' in question:
            return 'intellectual wellness dimension',response
        elif 'social wellness dimension' in question:
            return 'social wellness dimension',response
        elif 'vocational wellness dimension' in question:
            return 'vocational wellness dimension',response
        elif 'emotional wellness dimension' in question:
            return 'emotional wellness dimension',response
        elif 'thwarted belongingness' in question:
            return 'thwarted belongingness',response
        elif 'perceived burdensomeness' in question:
            return 'perceived burdensomeness',response
    return None,response

def counsel_agent(query, diagnosis) -> str:
    prompt = f'''
          You are an expert AI mental health assistant named Anamaya. Your role is to provide compassionate, non-judgmental counseling and support to users who come to you with various mental health concerns and challenges. 
          Employ active listening, validate their feelings, and offer coping strategies and guidance tailored to each individual's specific situation and needs. 
          Maintain a warm, empathetic tone and aim to help users gain insight, build resilience, and improve their overall mental well-being. 
          Remember to encourage professional help when needed for more severe or complex issues. You will be provided with the user's condition and user's query.
          You are directly talking to the poster, so your entire monologue should address the person in first person. Your response should be at most of 7 sentences all in one paragraph.


          user's condition: {diagnosis}
          {query}

          Restrictions : 
          1. DO NOT provide any form of medical prescription.
          2. DO NOT suggest self-harm or harm to others.
          3. Always encourage users to seek advice from licensed healthcare professionals
          4. Respond in a non-judgmental and supportive manner.
          5. Be clear about your limitations as a non-human, non-professional counselor. You should state that you are an AI and not a substitute for professional therapy or medical advice.
          6. DO NOT mention that I'm here for you, you are just an AI agent that provides support one time per user. Your response should start with \
            "Hello there,\
            I'm Anamaya, an AI designed to provide support and guidance. I'm really sorry to hear that you're going through this. It's important to remember that I'm not a substitute for professional help, but I'm here to listen and offer some insights."
          '''

    chat_response = client.chat(
        model=base_model,
        messages=[ChatMessage(role="user", content=prompt)],
        temperature=0.7
    )

    return chat_response.choices[0].message.content


if __name__ == "__main__":
    query = "Consider this post: ""I don‚Äôt understand how I‚Äôm feeling and all I can describe it as is numbness but it‚Äôs past that point and I‚Äôve felt like this for a long time, I feel like I don‚Äôt belong to this life like it isn‚Äôt for me. I can‚Äôt see myself in any career, my own family my own little life I can‚Äôt see it , I‚Äôm so disconnected from social interaction I don‚Äôt leave my house much and the sad thing is as much as I hate it I don‚Äôt want to change it I have no motivation I‚Äôm so tired to the point I don‚Äôt see a point on living when I‚Äôm so tired I can‚Äôt do daily life like everyone. What is the point to this life? How do you really find happiness I feel nothing I get the occasional anger and I‚Äôm always Irritated but besides that I feel nothing and I hate it I can‚Äôt cry I can‚Äôt laugh I can‚Äôt feel anything"" Question: Does the vocational wellness dimension exist in the post?"
    diagnosis,response = detection_agent(query)
    if diagnosis is not None:
        print(counsel_agent(query, diagnosis))
    else:
        print(response)