# -*- coding: utf-8 -*-
"""
Created on Mon Lun 20 15:58:41 2023

@author: hp
"""
#installation section 

#pip install gradio
#pip install openai
#pip install gtts
#pip install ffmpeg
#ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 10 -q:a 9 -acodec libmp3lame Temp.mp3

#import section

import gradio as gr 
import openai
from gtts import gTTS
#https://platform.openai.com/account/api-keys
with open("api_key.txt",'r') as f:
    openai.api_key=f.readline();
messages = [
    {"role": "system", "content": "give a possible solution to the person's problem and cheer them up"},
]
def chatgpt_api(input):    
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
def dall_e_api(dalle_prompt):

    dalle_response = openai.Image.create(
            prompt = dalle_prompt,
            size="512x512"
        )
    image_url = dalle_response['data'][0]['url']
    return image_url

def f(input):
    
    out_result = chatgpt_api(input)
    image_url=dall_e_api(input)
    audioobj = gTTS(text = out_result, 
                    lang = "en-uk", 
                    slow = False)
    audioobj.save("Temp.mp3")
    return [ out_result, "Temp.mp3",image_url]


output_1 = gr.Textbox(label="Answer")
output_2 = gr.Audio("Temp.mp3",label="The audio version")
output_3= gr.Image(label="AI image")
inputs = gr.inputs.Textbox(lines=7,placeholder="Type your question here...", label="Chat with AI")
outputs=[output_1, output_2, output_3]

gr.Interface(fn=f, inputs=inputs, outputs=outputs, title="AI Chatbot to help you and cheer you up 😊💕",
             description="Ask anything you want!",
             theme=gr.themes.Soft(),css="body {background-image: url('file=clouds.jpg')}").launch(share=True)
