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
### create a text file named api_key.txt and write in it the api key you got
## How it does look like
<img width="344" alt="1" src="https://user-images.githubusercontent.com/132129226/235297602-faccade8-14ea-4a1e-b1de-ff32221dded5.png">
<img width="357" alt="2" src="https://user-images.githubusercontent.com/132129226/235297613-ba3dff1e-41f1-408d-ad9a-cff9df8efb9b.png">
<img width="360" alt="3" src="https://user-images.githubusercontent.com/132129226/235297620-a54e84ba-6b3d-4acc-89b3-2eb4a952cfbc.png">

