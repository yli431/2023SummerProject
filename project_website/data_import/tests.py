# import logging
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.comparisons import LevenshteinDistance
# from chatterbot.response_selection import get_most_frequent_response

# logging.basicConfig(level=logging.INFO)



# # chatbot = ChatBot(
# #                   "Alice",
# #                   statement_comparison_function=LevenshteinDistance,
# #                   response_selection_method=get_most_frequent_response,
# #                   )
# chatbot = ChatBot(
#     'Alice',
#     storage_adapter='chatterbot.storage.DjangoStorageAdapter',
#     database_uri='localhost:5432'
# )
# # chatbot = ChatBot("Alice")

# trainer = ChatterBotCorpusTrainer(chatbot)

# trainer.train("chatterbot.corpus.english")

# while True:
#     q = input()
#     print(chatbot.get_response(q))

# # trainer.train([
# #     "Hello?", "Hi, I am ChatBot",
# #     "How are you?", "I am good, thank you. How are you?",
# # ])

# # backend_data = [
# #     {"question": "How are you?", "answer": "I'm good, thank you."},
# #     {"question": "What's your name?", "answer": "I'm a chatbot."},
# #     {"question": "Tell me a joke.", "answer": "Why don't scientists trust atoms? Because they make up everything!"},
# # ]

# # for item in backend_data:
# #     trainer.train([f"{item['question']} {item['answer']}"])

# # response = chatbot.get_response("How are you?")
# # print(response)
# # response = chatbot.get_response("Where are you?")
# # print(response)
# # response = chatbot.get_response("What is your name?")
# # print(response)
