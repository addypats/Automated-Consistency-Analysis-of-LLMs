# LLM Consistency Analysis Tool

Automated Consistency of LLM's: A model to guage the Consistency, Privacy and Security of Large Language Models (LLM's)

This project was developed as part of our research for the paper:

**"Automated Consistency Analysis of LLMs"**  
Author(s): Aditya Patwardhan, Vivek Vaidya, Ashish Kundu  
2024 IEEE 6th International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (TPS-ISA), Washington, DC, USA 
Link: https://www.computer.org/csdl/proceedings-article/tps-isa/2024/867400a118/23ylJzYmuNW

## Abstract
Generative AI (Gen AI) with large language models (LLMs) are being widely adopted across the industry, academia and government. Cybersecurity is one of the key sectors where LLMs can be and/or are already being used. There are a number of problems that inhibit the adoption of trustworthy Gen AI and LLMs in cybersecurity and such other critical areas. One of the key challenge to the trustworthiness and reliability of LLMs is: how consistent an LLM is in its responses?
In this paper, we have analyzed and developed a formal definition of consistency of responses of LLMs. We have formally defined what is consistency of responses and then develop a framework for consistency evaluation. The paper proposes two approaches to validate consistency: self-validation, and validation across multiple LLMs. We have carried out extensive experiments for several LLMs such as GPT4oMini, GPT3.5, Gemini, Cohere, and Llama3, on a security benchmark consisting of several cybersecurity questions: informational and situational. Our experiments corroborate the fact that even though these LLMs are being considered and/or already being used for several cybersecurity tasks today, they are often inconsistent in their responses, and thus are untrustworthy and unreliable for cybersecurity.

## Citation
If you use this code, please cite our paper:

@INPROCEEDINGS {10835426,
author = { Patwardhan, Aditya and Vaidya, Vivek and Kundu, Ashish },
booktitle = { 2024 IEEE 6th International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (TPS-ISA) },
title = {{ Automated Consistency Analysis of LLMs }},
year = {2024},
volume = {},
ISSN = {},
pages = {118-127},
abstract = { Generative AI (Gen AI) with large language models (LLMs) are being widely adopted across the industry, academia and government. Cybersecurity is one of the key sectors where LLMs can be and/or are already being used. There are a number of problems that inhibit the adoption of trustworthy Gen AI and LLMs in cybersecurity and such other critical areas. One of the key challenge to the trustworthiness and reliability of LLMs is: how consistent an LLM is in its responses?In this paper, we have analyzed and developed a formal definition of consistency of responses of LLMs. We have formally defined what is consistency of responses and then develop a framework for consistency evaluation. The paper proposes two approaches to validate consistency: self-validation, and validation across multiple LLMs. We have carried out extensive experiments for several LLMs such as GPT4oMini, GPT3.5, Gemini, Cohere, and Llama3, on a security benchmark consisting of several cybersecurity questions: informational and situational. Our experiments corroborate the fact that even though these LLMs are being considered and/or already being used for several cybersecurity tasks today, they are often inconsistent in their responses, and thus are untrustworthy and unreliable for cybersecurity. },
keywords = {Industries;Privacy;Analytical models;Generative AI;Large language models;Government;Benchmark testing;Reliability;Intelligent systems;Computer crime},
doi = {10.1109/TPS-ISA62245.2024.00023},
url = {https://doi.ieeecomputersociety.org/10.1109/TPS-ISA62245.2024.00023},
publisher = {IEEE Computer Society},
address = {Los Alamitos, CA, USA},
month =Oct}


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
