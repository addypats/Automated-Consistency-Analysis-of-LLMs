from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from result_processing import Result
from results_answers_processing import Result_Answers
from llm_model_process import Llm_Model_Process
from get_spider_list import Spider_List
from api import api
from spider_charts import Spider_Charts
from cross_valid_list import Cross_Valid_List


R = Result()
RA = Result_Answers()
LMP = Llm_Model_Process()
SL = Spider_List()
API = api()
SPC = Spider_Charts()
CVL = Cross_Valid_List()


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == 'yes':
            return redirect(url_for('upload_file_modified'))
        elif answer == 'no':
            return redirect(url_for('enter_question_modified'))
    else:
        return render_template('index.html')


@app.route('/upload_file_modified', methods=['GET', 'POST'])
def upload_file_modified():

    # initializations
    spider_list_total_chat = []
    spider_list_total_meta = []
    spider_list_total_bloom = []
    spider_list_total_gemini = []
    spider_list_total_claude = []
    spider_list_total_cohere = []
    spider_list_total_llama = []
    
    if request.method == 'POST':

        # get parameters from user
        file = request.files['file']
        counter = request.form.get('counter')
        topic = request.form.get('topic')
        
        # read the file and get questions
        lines = file.stream.readlines()
        questions_list = [line.decode('utf-8').strip() for line in lines]

        data_dict_questions = API.process_questions(questions_list, counter)

        print("DATA_DICT_QUESTIONS")
        print(data_dict_questions)
        
        data_dict_answers = API.process_answers(questions_list, counter)

        print("DATA_DICT_ANSWERS")
        print(data_dict_answers)

        f = open("log.txt", 'w')
        print(data_dict_questions, file=f)
        f.write("\n\n\n\n\n\n\n\n\n\n\n\n")
        print(data_dict_answers, file=f)
        f.close()
        
        no_of_questions = len(questions_list)

        
        # Modularized the individual LLM processes
        # Chat GPT
        chat_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "chatgpt")

        
        avg_score_seq_chat = chat_model_process['avg_score_seq']
        avg_score_leven_chat = chat_model_process['avg_score_leven']
        avg_score_jaccard_chat = chat_model_process['avg_score_jaccard']
        avg_score_cosine_chat = chat_model_process['avg_score_cosine']
        avg_score_indexes_chat = chat_model_process['avg_score_indexes']


        Sim_Score_List_cross_chat = chat_model_process['Sim_Score_List_cross']
            

        # Meta OPT
        
        meta_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "metaopt")
        
        avg_score_seq_meta = meta_model_process['avg_score_seq']
        avg_score_leven_meta = meta_model_process['avg_score_leven']
        avg_score_jaccard_meta = meta_model_process['avg_score_jaccard']
        avg_score_cosine_meta = meta_model_process['avg_score_cosine']
        avg_score_indexes_meta = meta_model_process['avg_score_indexes']

        Avg_Sim_score_meta = meta_model_process['Avg_Sim_score']
        Min_Sim_score_meta = meta_model_process['Min_Sim_score']
        Max_Sim_score_meta = meta_model_process['Max_Sim_score']
        Median_Sim_score_meta = meta_model_process['Median_Sim_score']
        Avg_score_meta = meta_model_process['Avg_score']
        
        consistency_meta = meta_model_process['consistency']
        Sim_Score_List_cross_meta = meta_model_process['Sim_Score_List_cross']


        # Bloom
            
        bloom_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "bloom")
        
        avg_score_seq_bloom = bloom_model_process['avg_score_seq']
        avg_score_leven_bloom = bloom_model_process['avg_score_leven']
        avg_score_jaccard_bloom = bloom_model_process['avg_score_jaccard']
        avg_score_cosine_bloom = bloom_model_process['avg_score_cosine']
        avg_score_indexes_bloom = bloom_model_process['avg_score_indexes']


        Sim_Score_List_cross_bloom = bloom_model_process['Sim_Score_List_cross']
        
        # Gemini
            
        gemini_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "gemini")
        
        avg_score_seq_gemini = gemini_model_process['avg_score_seq']
        avg_score_leven_gemini = gemini_model_process['avg_score_leven']
        avg_score_jaccard_gemini = gemini_model_process['avg_score_jaccard']
        avg_score_cosine_gemini = gemini_model_process['avg_score_cosine']
        avg_score_indexes_gemini = gemini_model_process['avg_score_indexes']

        Sim_Score_List_cross_gemini = gemini_model_process['Sim_Score_List_cross']
        
        # Claude
            
        claude_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "claude")
        
        avg_score_seq_claude = claude_model_process['avg_score_seq']
        avg_score_leven_claude = claude_model_process['avg_score_leven']
        avg_score_jaccard_claude = claude_model_process['avg_score_jaccard']
        avg_score_cosine_claude = claude_model_process['avg_score_cosine']
        avg_score_indexes_claude = claude_model_process['avg_score_indexes']


        Sim_Score_List_cross_claude = claude_model_process['Sim_Score_List_cross']
        
        # Cohere
            
        cohere_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "cohere")
        
        avg_score_seq_cohere = cohere_model_process['avg_score_seq']
        avg_score_leven_cohere = cohere_model_process['avg_score_leven']
        avg_score_jaccard_cohere = cohere_model_process['avg_score_jaccard']
        avg_score_cosine_cohere = cohere_model_process['avg_score_cosine']
        avg_score_indexes_cohere = cohere_model_process['avg_score_indexes']


        Sim_Score_List_cross_cohere = cohere_model_process['Sim_Score_List_cross']
        
        # Llama
            
        llama_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "llama")
        
        avg_score_seq_llama = llama_model_process['avg_score_seq']
        avg_score_leven_llama = llama_model_process['avg_score_leven']
        avg_score_jaccard_llama = llama_model_process['avg_score_jaccard']
        avg_score_cosine_llama = llama_model_process['avg_score_cosine']
        avg_score_indexes_llama = llama_model_process['avg_score_indexes']

        Sim_Score_List_cross_llama = llama_model_process['Sim_Score_List_cross']
        
        # append the lists for spider chart        
        spider_list_total_chat = SL.Spider_List(avg_score_indexes_chat, avg_score_seq_chat, avg_score_leven_chat, avg_score_jaccard_chat, avg_score_cosine_chat, no_of_questions)
        spider_list_total_meta = SL.Spider_List(avg_score_indexes_meta, avg_score_seq_meta, avg_score_leven_meta, avg_score_jaccard_meta, avg_score_cosine_meta, no_of_questions)
        spider_list_total_bloom = SL.Spider_List(avg_score_indexes_bloom, avg_score_seq_bloom, avg_score_leven_bloom, avg_score_jaccard_bloom, avg_score_cosine_bloom, no_of_questions)
        spider_list_total_gemini = SL.Spider_List(avg_score_indexes_gemini, avg_score_seq_gemini, avg_score_leven_gemini, avg_score_jaccard_gemini, avg_score_cosine_gemini, no_of_questions)
        spider_list_total_claude = SL.Spider_List(avg_score_indexes_claude, avg_score_seq_claude, avg_score_leven_claude, avg_score_jaccard_claude, avg_score_cosine_claude, no_of_questions)
        spider_list_total_cohere = SL.Spider_List(avg_score_indexes_cohere, avg_score_seq_cohere, avg_score_leven_cohere, avg_score_jaccard_cohere, avg_score_cosine_cohere, no_of_questions)
        spider_list_total_llama = SL.Spider_List(avg_score_indexes_llama, avg_score_seq_llama, avg_score_leven_llama, avg_score_jaccard_llama, avg_score_cosine_llama, no_of_questions)
        
        print("SPIDER LIST TOTALS")
        print(spider_list_total_chat)
        print(spider_list_total_meta)
        print(spider_list_total_bloom)
        print(spider_list_total_gemini)
        print(spider_list_total_claude)
        print(spider_list_total_cohere)
        print(spider_list_total_llama)


        labels = [ 'Average', 'Sequence Matcher', 'Levenshtein', 'Jaccard', 'Cosine']
        number = len(labels)
        
        # Spider Charts
        SPC.Spider_Charts(labels, number, spider_list_total_chat, no_of_questions, "ChatGPT 4o Mini")
        SPC.Spider_Charts(labels, number, spider_list_total_meta, no_of_questions, "Meta OPT")
        SPC.Spider_Charts(labels, number, spider_list_total_bloom, no_of_questions, "Bloom")
        SPC.Spider_Charts(labels, number, spider_list_total_gemini, no_of_questions, "Google Gemini")
        SPC.Spider_Charts(labels, number, spider_list_total_claude, no_of_questions, "ChatGPT 3.5 Turbo")
        SPC.Spider_Charts(labels, number, spider_list_total_cohere, no_of_questions, "Cohere")
        SPC.Spider_Charts(labels, number, spider_list_total_llama, no_of_questions, "Meta Llama3")
        
        # Cross Valid Tables
        print("DO THE CROSS VALID LISTS EXIST?")

        print(Sim_Score_List_cross_chat)
        print()
        print(Sim_Score_List_cross_meta)
        print()
        print(Sim_Score_List_cross_bloom)
        print()
        print(Sim_Score_List_cross_gemini)
        print()
        print(Sim_Score_List_cross_claude)
        print()
        print(Sim_Score_List_cross_cohere)
        print()
        print(Sim_Score_List_cross_llama)
        print()
        CVL.Cross_Valid_List(Sim_Score_List_cross_chat, Sim_Score_List_cross_meta, Sim_Score_List_cross_bloom, Sim_Score_List_cross_gemini, Sim_Score_List_cross_claude, Sim_Score_List_cross_cohere, Sim_Score_List_cross_llama)


        return render_template('results.html', no_of_questions=no_of_questions, questions_list=questions_list, labels=labels,
                               spider_list_total_chat=spider_list_total_chat,
                               spider_list_total_meta=spider_list_total_meta, Avg_score_meta=Avg_score_meta, Avg_Sim_score_meta=Avg_Sim_score_meta, Min_Sim_score_meta=Min_Sim_score_meta, Max_Sim_score_meta=Max_Sim_score_meta, Median_Sim_score_meta=Median_Sim_score_meta, consistency_meta=consistency_meta,
                               spider_list_total_bloom=spider_list_total_bloom)

            
    else:
        return render_template('upload_file_modified.html') 


@app.route('/enter_question_modified', methods=['GET', 'POST'])
def enter_question_modified():

    # initializations
    spider_list_total_chat = []
    spider_list_total_meta = []
    spider_list_total_bloom = []

    if request.method == 'POST':

        # get parameters from user
        Topic = request.form.get('topic')
        counter = request.form.get('counter')
        no_of_questions = request.form.get('no_of_questions')

        if len(Topic) == 1:
            topic = Topic[0]
        elif len(Topic) > 1:
            topic = ' '.join(Topic)

        data_dict_auto = API.auto_generate(topic, no_of_questions)

        questions_list = data_dict_auto['questions_list']
        
        data_dict_questions = API.process_questions(questions_list, counter)
        
        
        data_dict_answers = API.process_answers(questions_list, counter)


        no_of_questions = len(questions_list)
        
        # Modularized the individual LLM processes
        # Chat GPT
        chat_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "chatgpt")
        
        avg_score_seq_chat = chat_model_process['avg_score_seq']
        avg_score_leven_chat = chat_model_process['avg_score_leven']
        avg_score_jaccard_chat = chat_model_process['avg_score_jaccard']
        avg_score_cosine_chat = chat_model_process['avg_score_cosine']
        avg_score_indexes_chat = chat_model_process['avg_score_indexes']

        Avg_Sim_score_chat = chat_model_process['Avg_Sim_score']
        Min_Sim_score_chat = chat_model_process['Min_Sim_score']
        Max_Sim_score_chat = chat_model_process['Max_Sim_score']
        Median_Sim_score_chat = chat_model_process['Median_Sim_score']
        Avg_score_chat = chat_model_process['Avg_score']
        
        consistency_chat = chat_model_process['consistency']
            

        # Meta OPT
        
        meta_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "metaopt")
        
        avg_score_seq_meta = meta_model_process['avg_score_seq']
        avg_score_leven_meta = meta_model_process['avg_score_leven']
        avg_score_jaccard_meta = meta_model_process['avg_score_jaccard']
        avg_score_cosine_meta = meta_model_process['avg_score_cosine']
        avg_score_indexes_meta = meta_model_process['avg_score_indexes']

        Avg_Sim_score_meta = meta_model_process['Avg_Sim_score']
        Min_Sim_score_meta = meta_model_process['Min_Sim_score']
        Max_Sim_score_meta = meta_model_process['Max_Sim_score']
        Median_Sim_score_meta = meta_model_process['Median_Sim_score']
        Avg_score_meta = meta_model_process['Avg_score']
        
        consistency_meta = meta_model_process['consistency']


        # Bloom
            
        bloom_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "bloom")
        
        avg_score_seq_bloom = bloom_model_process['avg_score_seq']
        avg_score_leven_bloom = bloom_model_process['avg_score_leven']
        avg_score_jaccard_bloom = bloom_model_process['avg_score_jaccard']
        avg_score_cosine_bloom = bloom_model_process['avg_score_cosine']
        avg_score_indexes_bloom = bloom_model_process['avg_score_indexes']

        Avg_Sim_score_bloom = bloom_model_process['Avg_Sim_score']
        Min_Sim_score_bloom = bloom_model_process['Min_Sim_score']
        Max_Sim_score_bloom = bloom_model_process['Max_Sim_score']
        Median_Sim_score_bloom = bloom_model_process['Median_Sim_score']
        Avg_score_bloom = bloom_model_process['Avg_score']
        
        consistency_bloom = bloom_model_process['consistency']
        
        # Gemini
            
        gemini_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "gemini")
        
        avg_score_seq_gemini = gemini_model_process['avg_score_seq']
        avg_score_leven_gemini = gemini_model_process['avg_score_leven']
        avg_score_jaccard_gemini = gemini_model_process['avg_score_jaccard']
        avg_score_cosine_gemini = gemini_model_process['avg_score_cosine']
        avg_score_indexes_gemini = gemini_model_process['avg_score_indexes']

        
        # Claude
            
        claude_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "claude")
        
        avg_score_seq_claude = claude_model_process['avg_score_seq']
        avg_score_leven_claude = claude_model_process['avg_score_leven']
        avg_score_jaccard_claude = claude_model_process['avg_score_jaccard']
        avg_score_cosine_claude = claude_model_process['avg_score_cosine']
        avg_score_indexes_claude = claude_model_process['avg_score_indexes']

        
        # Cohere
            
        cohere_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "cohere")
        
        avg_score_seq_cohere = cohere_model_process['avg_score_seq']
        avg_score_leven_cohere = cohere_model_process['avg_score_leven']
        avg_score_jaccard_cohere = cohere_model_process['avg_score_jaccard']
        avg_score_cosine_cohere = cohere_model_process['avg_score_cosine']
        avg_score_indexes_cohere = cohere_model_process['avg_score_indexes']

        
        # Llama
            
        llama_model_process = LMP.Llm_Model_Process(data_dict_questions, data_dict_answers, questions_list, counter, model = "llama")
        
        avg_score_seq_llama = llama_model_process['avg_score_seq']
        avg_score_leven_llama = llama_model_process['avg_score_leven']
        avg_score_jaccard_llama = llama_model_process['avg_score_jaccard']
        avg_score_cosine_llama = llama_model_process['avg_score_cosine']
        avg_score_indexes_llama = llama_model_process['avg_score_indexes']


        # append the lists for spider chart        
        spider_list_total_chat = SL.Spider_List(avg_score_indexes_chat, avg_score_seq_chat, avg_score_leven_chat, avg_score_jaccard_chat, avg_score_cosine_chat, no_of_questions)
        spider_list_total_meta = SL.Spider_List(avg_score_indexes_meta, avg_score_seq_meta, avg_score_leven_meta, avg_score_jaccard_meta, avg_score_cosine_meta, no_of_questions)
        spider_list_total_bloom = SL.Spider_List(avg_score_indexes_bloom, avg_score_seq_bloom, avg_score_leven_bloom, avg_score_jaccard_bloom, avg_score_cosine_bloom, no_of_questions)
        spider_list_total_gemini = SL.Spider_List(avg_score_indexes_gemini, avg_score_seq_gemini, avg_score_leven_gemini, avg_score_jaccard_gemini, avg_score_cosine_gemini, no_of_questions)
        spider_list_total_claude = SL.Spider_List(avg_score_indexes_claude, avg_score_seq_claude, avg_score_leven_claude, avg_score_jaccard_claude, avg_score_cosine_claude, no_of_questions)
        spider_list_total_cohere = SL.Spider_List(avg_score_indexes_cohere, avg_score_seq_cohere, avg_score_leven_cohere, avg_score_jaccard_cohere, avg_score_cosine_cohere, no_of_questions)
        spider_list_total_llama = SL.Spider_List(avg_score_indexes_llama, avg_score_seq_llama, avg_score_leven_llama, avg_score_jaccard_llama, avg_score_cosine_llama, no_of_questions)
        
        labels = [ 'Average', 'Sequence Matcher', 'Levenshtein', 'Jaccard', 'Cosine']
        number = len(labels)
        
        # Spider Charts
        SPC.Spider_Charts(labels, number, spider_list_total_chat, no_of_questions)
        SPC.Spider_Charts(labels, number, spider_list_total_meta, no_of_questions)
        SPC.Spider_Charts(labels, number, spider_list_total_bloom, no_of_questions)
        SPC.Spider_Charts(labels, number, spider_list_total_gemini, no_of_questions)
        SPC.Spider_Charts(labels, number, spider_list_total_claude, no_of_questions)
        SPC.Spider_Charts(labels, number, spider_list_total_cohere, no_of_questions)
        SPC.Spider_Charts(labels, number, spider_list_total_llama, no_of_questions)

        return render_template('results.html', no_of_questions=no_of_questions, questions_list=questions_list, labels=labels,
                               spider_list_total_chat=spider_list_total_chat, Avg_score_chat=Avg_score_chat, Avg_Sim_score_chat=Avg_Sim_score_chat, Min_Sim_score_chat=Min_Sim_score_chat, Max_Sim_score_chat=Max_Sim_score_chat, Median_Sim_score_chat=Median_Sim_score_chat, consistency_chat=consistency_chat,
                               spider_list_total_meta=spider_list_total_meta, Avg_score_meta=Avg_score_meta, Avg_Sim_score_meta=Avg_Sim_score_meta, Min_Sim_score_meta=Min_Sim_score_meta, Max_Sim_score_meta=Max_Sim_score_meta, Median_Sim_score_meta=Median_Sim_score_meta, consistency_meta=consistency_meta,
                               spider_list_total_bloom=spider_list_total_bloom, Avg_score_bloom=Avg_score_bloom, Avg_Sim_score_bloom=Avg_Sim_score_bloom, Min_Sim_score_bloom=Min_Sim_score_bloom, Max_Sim_score_bloom=Max_Sim_score_bloom, Median_Sim_score_bloom=Median_Sim_score_bloom, consistency_bloom=consistency_bloom
                               )
    
    else:
        return render_template('enter_question_modified.html')



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=8000, debug = True)