## THIS FILE CONTAINS ALL DIFFERENT PROMPT TECHNIQUES FOR THE IMPLEMENTATION IN OUR Q/A SYSTEM


#@title  DEFAULT ONE
prompt_template = """Answer the Question as Detailed as possible from the provided context, 
                         make sure to provide all the details, if the answer not in the provided context just say "answer is not available in the context", 
                         don't provide the wrong answer\n\n
                         Context : \n {context}?\n
                         Question: \n{question}\n

                        Answer:
                        """

#@title  Graph of Thought implementation
prompt_template_1 = """
                    Consider the information extracted from the PDF. Construct a graph where nodes represent key ideas, and edges represent the relationships between these ideas.
                    How can these ideas be connected to form a coherent understanding?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Graph of Thought:
                    """

#@title Tree of Thought implementation
prompt_template_2 = """
                    Given the text from the PDF, create a tree structure where each branch represents a possible expansion of a core concept.
                    How can this hierarchy help in understanding the overall content?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n


                    Tree of Thought:
                    """

#@title Graph of Verification implementation
prompt_template_3 = '''
# Graph of Verification prompt template goes here
'''

#@title Chain-of-Thought (COT) Prompting implementation
prompt_template_4 = '''Consider the information extracted from the PDF.
                    Break down the process of summarizing this content into a chain of logical steps.
                    What are the intermediate steps required to generate a concise summary?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Chain of Thought:
                    '''

#@title XOT (Everything of Thought) implementation
prompt_template_5 = '''Consider the information extracted from the PDF.
                    Consider every possible thought or interpretation of this text. How can multiple perspectives be integrated to form a comprehensive understanding?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    XOT of Thought:
                    '''

#@title KD-CoT (Knowledge Driven COT) implementation
prompt_template_6 = '''Consider the information extracted from the PDF.
                    Apply domain-specific knowledge to enhance the chain-of-thought process. How does expert knowledge shape the interpretation and summarization of the text?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    XOT of Thought:
                    '''

#@title COT-SC (Self-Consistency with COT) implementation
prompt_template_7 = '''Consider the information extracted from the PDF.
                    Ensure that the chain-of-thought process remains consistent throughout the summarization. How can internal consistency be maintained in the logical flow?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n


                    COT-SC of Thought:
                    '''

#@title Self-Ask implementation
prompt_template_8 = '''Consider the information extracted from the PDF.
                    Generate questions that the text answers. What questions arise from the content, and how can answering them clarify the material?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n


                    COT-SC of Thought:
                    '''

#@title Self-Critique implementation
prompt_template_9 = '''Consider the information extracted from the PDF.
                    Critically evaluate the generated summary. What aspects might be inaccurate or misleading, and how can they be corrected?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n


                    Self-Critique :
                    '''

#@title Self-Refine implementation
prompt_template_10 = '''Consider the information extracted from the PDF.
                    Iteratively refine the summary by incorporating feedback. What improvements can be made in each iteration to enhance clarity and accuracy?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n


                    Self-Refine :
                    '''

#@title Self-Refinement implementation
prompt_template_11 = '''Consider the information extracted from the PDF.
                    Continuously improve the generated content. How can the content be polished to better align with the original text's intent?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n


                    Self-Refinement :
                    '''

#@title Iterative Prompting implementation
prompt_template_12 = '''Consider the information extracted from the PDF.
                    Engage in multiple rounds of prompting to gradually refine the output. How does each iteration improve the quality of the summary?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Iterative Prompting :
                    '''

#@title Analogical Prompting implementation
prompt_template_13 = '''Consider the information extracted from the PDF.
                    Use analogies to relate the content to familiar concepts. How can drawing parallels help in understanding complex ideas?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Analogical Prompting :
                    '''

#@title Input-Output Prompting implementation
prompt_template_14 = '''Consider the information extracted from the PDF.
                    For each input (text), specify the expected output (summary). How can clear examples of input-output pairs guide the generation process\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Input-Output Prompting :
                    '''

#@title Least-to-Most Prompting implementation
prompt_template_15 = '''Consider the information extracted from the PDF.
                    Start with the simplest possible summary and progressively add more details. How does gradually increasing complexity enhance the summary?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Least-to-Most Prompting :
                    '''

#@title Plan-and-Solve Prompting implementation
prompt_template_16 = '''Consider the information extracted from the PDF.
                    Develop a plan to tackle the summarization problem and then execute it. What steps need to be followed to achieve the desired outcome?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Plan-and-Solve Prompting :
                    '''

#@title Sequential Prompting implementation
prompt_template_17 = '''Consider the information extracted from the PDF.
                    Break down the summarization into sequential tasks. How can each step logically follow the previous one to build a coherent summary?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Sequential Prompting Prompting :
                    '''

#@title Step-Back Prompting implementation
prompt_template_18 = '''Consider the information extracted from the PDF.
                    Take a step back and reassess the current summary. What broader perspective can be gained by reevaluating the previous steps?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Step-Back Prompting :
                    '''

#@title MemPrompt implementation
prompt_template_19 = '''Consider the information extracted from the PDF.
                    Leverage memory of previous prompts to inform the current task. How can recalling past interactions help improve the summary?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    MemPrompt Prompting :
                    '''

#@title Chain of Density (CoD) Prompt implementation
prompt_template_20 = '''Consider the information extracted from the PDF.
                    Focus on creating a dense, information-rich summary. How can the most important details be packed into a concise form?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Chain of Density Prompting :
                    '''

#@title Reverse JSON Prompt implementation
prompt_template_21 = '''Consider the information extracted from the PDF.
                    Generate a summary in a structured format, such as JSON, that can be easily reversed into the original content. How does this structure aid in understanding?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Reverse JSON Prompting :
                    '''

#@title Symbolic Reasoning implementation
prompt_template_22 = '''Consider the information extracted from the PDF.
                    Apply symbolic logic to the content. How can formal reasoning techniques help clarify the underlying arguments?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Symbolic Reasoning Prompting :
                    '''

#@title Generated Knowledge implementation
prompt_template_23 = '''Consider the information extracted from the PDF.
                    Use the text to generate new knowledge or insights. What novel ideas can be derived from the content?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Generated Knowledge Prompting :
                    '''

#@title PAL (Program-Aided Language Models) implementation
prompt_template_24 = '''Consider the information extracted from the PDF.
                    Use programmatic aids to enhance the summarization process. How can algorithms assist in generating more accurate summaries?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    PAL  Prompting :
                    '''

#@title Meta-Ask Self-Consistency implementation
prompt_template_25 = '''Consider the information extracted from the PDF.
                    Ensure that multiple summaries of the same content are consistent with each other. How can consistency across different iterations be achieved?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    Meta-Ask Prompting :
                    '''

#@title ReAct implementation
prompt_template_26 = '''Consider the information extracted from the PDF.
                    React to the generated content by providing immediate feedback. How can interactive responses guide the improvement of the summary?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    ReAct  Prompting :
                    '''
#@title ART (Automatic Reasoning & Tool-Use) implementation
prompt_template_27 = '''Consider the information extracted from the PDF.
                    Utilize automatic reasoning tools to enhance the summary. What tools can assist in analyzing and condensing the content?\n\n
                    Context : \n {context}?\n
                    Question: \n{question}\n

                    ART  Prompting :
                    '''
# Few-Shot Prompting
prompt_template_28 = """
Provide a few examples of how to analyze and summarize the content from a PDF document. 
Here are some examples:
1. Example 1: Summary of a financial report PDF.
2. Example 2: Analysis of a research paper PDF.

Now, based on these examples, analyze and summarize the following PDF content.

Context:
{context}

Response:
"""

# Zero-Shot Prompting
prompt_template_29 = """
Analyze the content from the provided PDF and generate a summary without any specific examples. 
Use your general understanding of how to process and interpret PDF content.

Context:
{context}

Response:
"""

# Chain-of-Thought Prompting
prompt_template_30 = """
Break down the process of summarizing this PDF document into a series of logical steps. 
Consider the structure of the document and the key points to cover. What steps should be taken to create an effective summary?

Context:
{context}

Chain of Thought:
"""

# Instruction-Based Prompting
prompt_template_31 = """
Follow these explicit instructions to summarize the content of the PDF. 
1. Identify the main sections of the document.
2. Extract key information from each section.
3. Combine the extracted information into a coherent summary.

Context:
{context}

Instructions:
{instructions}

Summary:
"""

# Persona-Based Prompting
prompt_template_32 = """
Respond as if you are a professional PDF analyst with expertise in summarizing complex documents. 
Adopt their style and perspective to summarize the provided PDF content.

Context:
{context}

Response:
"""

# Contextual Prompting
prompt_template_33 = """
Use the context provided from the PDF to generate a detailed summary. 
Ensure that the summary reflects the key themes and information presented in the document.

Context:
{context}

Summary:
"""

# Role-Playing Prompting
prompt_template_34 = """
Assume the role of a researcher who needs to prepare a summary of the provided PDF document. 
Address the key findings and implications based on the role.

Context:
{context}

Summary:
"""

# Comparison Prompting
prompt_template_35 = """
Compare the following aspects of the PDF content:
1. The primary arguments presented.
2. The evidence supporting these arguments.

Context:
{context}

Comparison:
"""

# Multi-Turn Prompting
prompt_template_36 = """
Engage in multiple rounds of analysis to summarize the PDF content. 
In each turn, refine the summary based on the feedback and additional insights from previous turns.

Context:
{context}

Turn 1 Summary:
"""

# Refinement Prompting
prompt_template_37 = """
Refine the initial summary of the PDF document based on detailed feedback. 
Iterate to improve the clarity and accuracy of the summary.

Context:
{context}

Initial Summary:
{initial_summary}

Refined Summary:
"""
