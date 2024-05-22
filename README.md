# A local language model AI with embeddings in 50 lines

Couple of weeks ago, I conducted an improvised coding demonstration where I ask about 50 engineers at NCS what I should code in the session itself. The idea was to demonstrate how they can use GitHub Copilot to get things done.

We settled on coding up a personal AI that I can add facts to and converse with. If the conversation turns up to be about the facts added (embeddings), the AI will answer based on those facts.

I really enjoyed the session because it forces us to get to the essence of what we're trying to achieve. Given time, we'll take a couple of days to choose the model, a few more to evaluate how we want to do embeddings, a few more to debate which language to go with, etc. 

Not in our session. Because we have around 50 people waiting around for each other, wondering what's going to happen next, things got to happen right now. And the brain works in mysterious ways when dopamine kicks in. Nevertheless, we were also blessed by the wonderful machinery called innovation that in turn drives the beautiful abstraction that wasn't there just a month ago (yes, I am referring to ollama.embeddings()).

This repository contains the code demo-ed in the session

# Pre-requisites

* Ollama
* Python 3.11

```
pip install ollama chromadb
```

# Run

```
$ python personal_facts.py
```
