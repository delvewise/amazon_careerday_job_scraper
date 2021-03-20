# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:32:15 2021

@author: nickd
"""
import spacy
import pandas as pd
from spacy.matcher import Matcher
import re
from collections import defaultdict
import numpy as np


def create_versioned(name):
    return [
        [{'LOWER': name}], 
        [{'LOWER': {'REGEX': f'({name}\d+\.?\d*.?\d*)'}}], 
        [{'LOWER': name}, {'TEXT': {'REGEX': '(\d+\.?\d*.?\d*)'}}],
    ]

# def Extract(lst): 
#     return [item[1:] for item in lst]

def part(matches):
    match = defaultdict(list)
    almost = []
    for num, first  in matches:
        match[num].append(first)
    for key, value in match.items():
        value=' '.join(map(str, value))
        almost.append(value)
    matches = almost
    return(matches)

def boo(there):
    coding=[]
    for i in range(len(there)):
        if str(there[i]) == '0':
            coding.append(0)
        else:
            coding.append(1)
    return coding

def job(x, w):
    titles = (_ for _ in df[w])
    matches=[]
    match_count=[]
    for i in range(len(df[w])):
        doc = nlp(next(titles))
        if len(matcher(doc)) == 0:
            matches.append([i,0])
            match_count.append([i,0])
        
        else:
            c=0
            for match_id, start, end in matcher(doc):
                c += 1
                # string_id = nlp.vocab.strings[match_id]
                spaz= [t.text for t in doc[start: end]]
                add= ' '.join(spaz)
                matches.append([i, add])
            match_count.append([i, c])
    xx = part(matches)
    yy = part(match_count)
    zz = boo(xx)
    y= x + '_count'
    z= x + '_bool'
    df[x]= xx
    df[y]= yy
    df[z] = zz


def max_str(input):
     num = re.findall('\d+',input) 
     numbers = map(int,num) 
     if len(num) == 0:
         return(0)
     else:
         return(max(numbers))

nlp = spacy.load("en_core_web_sm")

js_pattern     = [{'LOWER': {'IN': ['js', 'javascript']}}]
r_pattern     = [{'LOWER': {'IN': ['r']}}]


#bus admin
mba_pattern    = [{'LOWER': {'IN': ['mba','master_s', 'masters in business administraion', 'master of business admin', 'masters of business administration']}}]
mba_pattern1 = [{'LOWER': 'master'},
                {'IS_PUNCT': True, 'OP': '?'},
                 {'LOWER': 's'}]


data_analytic_pattern= [{'LOWER': {'IN': ['certificate in data analytics', 'certification in data analytics', 'business analytics', 'data visualization', 'statistical analysis']}}]
flask_pattern= [{'LOWER': 'flask'}]

bachelor_pattern = [{'LOWER': {'IN': ['ba', 'bachelors', 'bachelors of', 'bs', 'b.a.', 'b.s.', 'ba']}}] 

#datamining
data_mining_pattern = [{'LOWER': {'IN': ['data mining', 'scraping', 'extraction']}}]

#make machine learning / statistic one
ml_pattern = [{'LOWER': {'IN': ['ml', 'nlp', 'machine learning', 'natural language processing']}}]
      

#analytic software
analytic_software_pattern = [{'LOWER': {'IN': ['power bi', 'tableau', 'quicksight', 'salesforce', 'excel','pandas']}}]

experience_pattern1 = [{'DEP': 'compound', 'OP': '*'},
        {'LEMMA': {'IN': ['experience', 'work', 'produce','participate' 'perform']}}]
#maybe make list of sentences that has experince and then find list of noun entities??? for list of what post need experience in. while other has


#nommod for amount of years
#trying with must have num 
years_pattern1 = [{'DEP': 'nummod', 'OP': '+'},{'LEMMA': 'or more', 'OP': '?'},
        {'LEMMA': {'IN': ['year']}}]

# num years of work in progress pattern
# pattern = [{'DEP': 'nummod', 'OP': '?'},
#            {'LEMMA': 'year'},
#            {'DEP': 'prep'},
#            {'LEMMA': 'experience'},
#            {'DEP': 'prep'},
#            {'DEP': 'pobj', 'OP': '*'}]

#uses above function to understand verisions
versioned_languages = ['python', 'html', 'css', 'sql', 'bash', 'django']
flatten = lambda l: [item for sublist in l for item in sublist]
versioned_patterns = flatten([create_versioned(lang) for lang in versioned_languages])



df = pd.read_csv('CSV oh joblisting')
#must make sure you have no missing data or it doesn't work
#df = df.dropna(how='any',axis='rows')
df = df.fillna(0)
df.head

#set up matcher prior to run 
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("PROG_LANG", None, 
            flask_pattern, js_pattern,r_pattern,
            *versioned_patterns)
# test string is name that will be given into dataframe
job('programming', 'Description')


#check
df['programming']
df['programming_count']
df['programming_bool']

df.info()
####################
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("MBA_TAG", None, mba_pattern, mba_pattern1)
# test string is name that will be given into dataframe
job('mba', 'Description')

#############################
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("BA_TAG", None,  data_analytic_pattern, data_mining_pattern, analytic_software_pattern)
# test string is name that will be given into dataframe
job('ba', 'Description')
############
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("YR_SKILL", None, years_pattern1)
# test string is name that will be given into dataframe
#add row for the max year

job('years', 'Description')
df['yearyear'] = df['Description'].apply(lambda x: list(nlp(x).ents)) 

max_year=[]
for i in range(len(df['years'])):
    y = max_str(df['years'][i])
    max_year.append(y)
    
df['max_year']= max_year


##################################
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("MBA_TAG", None, mba_pattern, mba_pattern1)
matcher.add("PROG_LANG", None, 
            flask_pattern, js_pattern,r_pattern,
            *versioned_patterns)
matcher.add("BA_TAG", None,  data_analytic_pattern, data_mining_pattern, analytic_software_pattern)
# test string is name that will be given into dataframe
job('total', 'Description')

job('m_description', 'Description')

df['q_new_text'] = df['Description'].apply(lambda x: list(nlp(x).ents)) 


#export after done
df.to_csv('2021_da_jobs_nlp.csv')

