from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    "Artificial Intelligence is the simulation of human intelligence by machines.",
    "Machine Learning is a subset of AI that learns from data without being explicitly programmed.",
    "Deep Learning uses neural networks with many layers to learn complex patterns.",
    "Natural Language Processing enables machines to understand and generate human language.",
    "Computer Vision allows machines to interpret and understand visual information from images.",
    "Reinforcement Learning trains agents to make decisions by rewarding correct actions.",
    "LangChain is a framework for building applications powered by large language models.",
    "Vector databases store embeddings and enable fast similarity search.",
    "Transformers are deep learning models that use attention mechanisms for NLP tasks.",
    "RAG stands for Retrieval Augmented Generation, combining search with text generation.",
]

vectors=embeddings.embed_documents(docs)
query="What is RAG?"
query_vector=embeddings.embed_query(query)


score=cosine_similarity([query_vector], vectors)[0]    # we [query_vector] did this bcz cosine_similarity demands 2D list, the vectors is already 2d, so our query needs: []
                                                        # And the [0] we add at the end bcz we want response in 1D list otherwise it would provide us a 2D list which is awkward and difficult to work with
index, score=sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print('similarity score: ', score)
