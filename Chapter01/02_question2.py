# Install a external module and use it to perform an operation of your interest.
# Install module pyjokes using command "pip install pyjokes"

# import pyjokes module
import pyjokes

jokes = pyjokes.get_joke()

print(jokes)
