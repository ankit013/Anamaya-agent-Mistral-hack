from anamaya import detection_agent,counsel_agent
import gradio as gr

def anamaya_chatbot_func(query='"Consider this post: ""I don‚Äôt understand how I‚Äôm feeling and all I can describe it as is numbness but it‚Äôs past that point and I‚Äôve felt like this for a long time, I feel like I don‚Äôt belong to this life like it isn‚Äôt for me. I can‚Äôt see myself in any career, my own family my own little life I can‚Äôt see it , I‚Äôm so disconnected from social interaction I don‚Äôt leave my house much and the sad thing is as much as I hate it I don‚Äôt want to change it I have no motivation I‚Äôm so tired to the point I don‚Äôt see a point on living when I‚Äôm so tired I can‚Äôt do daily life like everyone. What is the point to this life? How do you really find happiness I feel nothing I get the occasional anger and I‚Äôm always Irritated but besides that I feel nothing and I hate it I can‚Äôt cry I can‚Äôt laugh I can‚Äôt feel anything"" Question: Does the vocational wellness dimension exist in the post?"',
           chat_history=''):
    diagnosis,response = detection_agent(query)
    if diagnosis is not None:
        counsel_response = counsel_agent(query, diagnosis)
        # print("Counseling agent response ---> ", counsel_response)
        final_result = f'''
            Diagnosis :: {str(response)} \n\n\n Counseling :: {counsel_response}'''
        return final_result
    else:
        print("Diagnosis agent response --> ", response)
        final_result = f'''Diagnosis :: {response} '''
        return final_result


    # Set up chat bot interface



anamaya_bot = gr.ChatInterface(
                            anamaya_chatbot_func,
                            chatbot=gr.Chatbot(height=300),
                            textbox=gr.Textbox(placeholder="Ask me a question about mental wellness", container=False, scale=7),
                            title="Anamaya",
                            description="Ask Anamaya Anything realted to Mental Health!",
                            theme="soft",
                            examples=['''Consider this post: "Who even cares anymore I’ve just learned to accept my thought and I realise things aren’t gonna get better.I have the same cycle every day just play video games mourn for death wish I had weed and listen to sad songs till the morning life has just become such a boring shit show. Even talking to random people has me fucked up cause i fuck things up tell me guys what’s the point of even living anymore" Question: Does the poster suffer from depression?''',
                                      '''Consider this post: "Anyone ever wish they were good at something? Something. Anything. Be it something innocuous or something that can get you a kickass job. Anything from which you could derive happiness and fulfillment. I've failed at everything I've tried. Good at absolutely nothing, even after years of trying. If there were even one such thing, I could just devote myself to it and use it to keep myself busy." Question: Does the poster suffer from depression?''', "low self esteem  Question: Does the poster suffer from depression?", 
                                      '''Consider this post: "The one and only thing I want to and have a will to do is to listen to the music all day and space out in it. Everything else is boring, draining and dull. And I receive no mental pleasure from doing anything else." Question: Does the poster suffer from depression?''', "umm.. I'm feeling down  Question: Does the poster suffer from depression?"],
                            cache_examples=False,
                            retry_btn=None,
                            undo_btn=None,
                            clear_btn=None,
                            stop_btn="Interrupt",
                            submit_btn="Ask"
                        )
if __name__ == "__main__":
    anamaya_bot.launch(share=True, debug=True)