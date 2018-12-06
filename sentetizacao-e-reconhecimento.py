#RECONHECIMENTO DE VOZ
import speech_recognition as sr #importamos o modúlo

rec = sr.Recognizer() #instanciamos o modúlo do reconhecedor

with sr.Microphone() as fala: #chamos a gravação do microphone de fala
	frase = rec.listen(fala) #o metodo listen vai ouvir o que a gente falar e gravar na variavel frase

print(rec.recognize_google(frase, language='pt')) #transformando nossa fala em texto


#TRANSFORMANDO TEXTO EM FALA
import pyttsx # importamos o modúlo
en = pyttsx.init() # meotodo init seleciona um ending de sintetização, no caso o espeak
en.say("Hello, I am Ronan") # o metodo say para dizer o que queremos
en.say(Nice to meet you) 
en.runAndWait() # para ouvir o que foi escrito
en.setProperty('voice', b'brazil') # mudamos a propriedade setando pelo id para pt-br, o lemento b diz que a string está em bytes
en.say('Olá, tudo bem?')
en.runAndWait()

#TRANSFORMANDO TEXTO EM FALA - USANDO API DO GOOGLE
from gtts import gTTS # importamos o modúlo gTTS
voz = gTTS("Olá, tudo bem?", lang ="pt") # guardamos o nosso texto na variavel voz
voz.save("voz.mp3") #salvamos com o comando save em mp3

import subprocess as s #importamos o subprocess e renomeamos a s
s.call(['MPC-HC', 'voz.mp3']) #com o comando call roda nosso comando de voz no player escolhido
