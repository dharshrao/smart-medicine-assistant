from language_engine import translate_telugu, generate_voice_english, generate_voice_telugu

text = "This medicine reduces fever"

telugu = translate_telugu(text)
print("Telugu:", telugu)

generate_voice_english(text)
generate_voice_telugu(telugu)

print("Audio files created successfully")
