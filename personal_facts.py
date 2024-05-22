import ollama
import chromadb

facts = [
  "Vito Chin espouses the use of the Unix Philosophy",
  "Vito Chin likes the PHP programming language",
  "Vito Chin likes to use GitHub for version control",
]

client = chromadb.Client()
collection = client.create_collection(name='facts')

for i, fact in enumerate(facts):
  response = ollama.embeddings(model="all-minilm", prompt=fact)
  embedding = response["embedding"]
  collection.add(
    ids=[str(i)],
    embeddings=[embedding],
    documents=[fact]
  )

user_input = ''

while user_input != "bye":
  user_input = input("You: ")

  if user_input == "bye":
    break
  else:
    # Generate an embedding for the prompt and retrieve the most relevant doc
    response = ollama.embeddings(
      prompt=user_input,
      model="all-minilm"
    )

    # Query the collection for the most relevant document
    results = collection.query(
      query_embeddings=[response["embedding"]],
      n_results=1
    )

    data = results['documents'][0][0]

    output = ollama.generate(
      model="phi3",
      prompt=f"Using this data: {data}. Respond to this prompt: {user_input}"
    )

    # Print the AI's response
    print("AI: " + output['response'])