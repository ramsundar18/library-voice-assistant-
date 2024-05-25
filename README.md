Python Voice Assistant with Book Availability and News Reporting

This Python script implements a virtual assistant named Max that can perform various tasks upon user interaction:

    Audio Playback: Plays songs or videos on YouTube using pywhatkit.
    Web Search: Searches the web for user-specified queries using pywhatkit.
    Wikipedia Search: Fetches information from Wikipedia using the wikipedia library and reads it aloud.
    Time Announcement: Provides the current time in a human-readable format.
    Book Availability: Checks the availability of specific textbooks relevant to Electronics and Communication Engineering (ECE) courses:
        Circuit Analysis (Author: Naagoor Kani)
        Control System (Authors: Katsuhiko Ogata, A. Naagoor Kani)
        Signals and Systems (Author: Alan V. Oppenheim)
        Linear Integrated Circuits (Author: Leena Jasmine)
        Digital Signal Processing (Author: John G. Proakis)
        Electromagnetic Field (Author: Nancy Forbes)
        Environmental Science (Author: Vishali Anand)
        Communication System (Author: Simon S. Haykin)
    News Reporting: Fetches and reads aloud top headlines from BBC News using the News API (requests).

Key Features:

    User-Friendly Interface: Accepts voice commands using speech recognition (speech_recognition) and provides audio feedback using text-to-speech (pyttsx3).
    Dynamic Book Availability: Tracks book availability to inform users if a book is already taken.
    News Integration: Delivers up-to-date news from a reputable source.

Requirements:

    Python 3
    speech_recognition library (pip install speech_recognition)
    pywhatkit library (pip install pywhatkit)
    wikipedia library (pip install wikipedia)
    pyttsx3 library (pip install pyttsx3)
    requests library (pip install requests)
    A News API key (obtainable from https://newsapi.org/)

Installation:

    Install the required libraries using pip.
    Save the script as a Python file (e.g., max_assistant.py).
    Obtain a News API key and replace '1062540632fb4aadb423460c994d9ec5' (placeholder) in the code with your key.

Usage:

    Run the script from the command line using python max_assistant.py.
    Follow the prompts and speak your commands clearly.
    Max will respond to your requests using spoken audio and text output (optional).

Additional Notes:

    The script can be further customized to interact with other services or perform different tasks as needed.
    Consider error handling and exception management to make the assistant more robust.
    Explore advanced features like natural language processing (NLP) for more complex interactions.

This script provides a solid foundation for building a versatile virtual assistant with valuable functionalities for students, researchers, or anyone desiring a helpful AI companion.
