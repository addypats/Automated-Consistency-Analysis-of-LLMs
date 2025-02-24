# LLM Consistency Analysis Tool

Automated Consistency of LLM's: A model to guage the Consistency, Privacy and Security of Large Language Models (LLM's)

## Installation

When in Consistency of LLM's/, run

```bash
pip install -r requirements.txt
```

When in Consistency of LLM's/, run

```bash
python app.py
```

The Flask webpage will run on port 8000.

## Providing Questions:

If you have a file containing the list of questions, then choose the 'yes' on the upload file page. It will then take you to the page where you have to upload the file contining your questions for testing the model, and the count for each question.
For the questions in a file, create a .txt file with each question on a separate line.

If you don't have a file containing the list of questions, then choose the 'no' on the upload file page. It will then take you to the page where you have to select the topics that you want to test the model on, and the count for each question.

After uploading/submitting topics, follow the prompts.

## Microservices and Modules:

### app.py:

This is the main flask server which calls all other modules, gets results, and sends the results to the html page.

### api.py:

This module makes all the API calls

### cal_score.py

This module calculates the similarity scores for the various techniques.

### generate_responses.py

This module contains the invocation of different api's for the LLM's. Include your API keys in .env

### get_similarity_score.py

This takes the scores from the techniques used and assigns a similarity score based on the weights.

### get_sim_list.py

This file contains code to get similarity score lists and other measures.

### get_score_n_graph.py

This module converts the scores into list to be passed to the graph.

### result_processing.py

This module processes the results of the response cross checking and returns the number of correct questions.

### result_answer_processing.py

This file runs the answers derived from the model and finds the average, minimum, etc of the answers.

## Exit

Use "Ctrl + C" in the terminal and exit the webpage.
