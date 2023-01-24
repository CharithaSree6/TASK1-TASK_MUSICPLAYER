from playsound import playsound
print('no.of avalible song\n1.I Phone Rintone\n2.Believer\n3.Guitar Nice Tone')
order= input('enter the music which you want to play:')
if 'I Phone Rintone' in order:
    playsound('C:\\Users\\lenovo\\Downloads\\I Phone Rintone.mp3 ')
elif'Believer'in order:
    playsound('C:\\Users\\lenovo\\Downloads\\Believer.mp3 ')
elif'Guitar Nice Tone'in order:
    playsound('C:\\Users\\lenovo\\Downloads\\Guitar Nice Tone.mp3 ')
