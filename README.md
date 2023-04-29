# A chatbot with audio and image generator 

## This program creates a Gradio interface that allows users to interact with the chatbot by entering text and displays the response, audio player, and image.

## the code explained 
* Define two API functions, one for generating responses and another for generating images.
* Create a main function that generates an audio response using gTTS, calls the API functions for generating the response and image, and returns the response, audio file, and image URL.
* Train the AI chatbot using the GPT-3.5 model from OpenAI.
* Create a Gradio interface that allows users to interact with the chatbot.

## installation section
* pip install gradio
* pip install openai
* pip install gtts
* pip install ffmpeg

## How to create the temporary audio file
### run this command in the terminal 
ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 10 -q:a 9 -acodec libmp3lame Temp.mp3

## Get the api_key from https://platform.openai.com/account/api-keys
## How it does look like
<img width="402" alt="1" src="https://user-images.githubusercontent.com/132129226/235297476-4c076e85-462b-4eb2-8dc4-e1a3ad33d0e0.png">
<img width="408" alt="2" src="https://user-images.githubusercontent.com/132129226/235297500-c6cb1e59-4fed-4d67-9613-4be9a2f6d70c.png">
<img width="404" alt="3" src="https://user-images.githubusercontent.com/132129226/235297512-6cbd8bc0-573c-499c-a32f-2cc2a7d4bad4.png">


