from setuptools import setup
setup(
    name = "Speech_To_Text",
    version = "0.0.1",
    author = "Pranay Joshi",
    author_email = "pranayjoshi466@gmail.com",
    description = ("Wanna find a simple and customized speech to text convertor."
                   "then this is the right choise"),
    license = "BSD",
    packages=['Speech_To_Text'],
    install_requires=['SpeechRecognition',
                     'pyttsx3']
)