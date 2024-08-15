#@title DEFAULT ONE
prompt_template = """Answer the Question as Detailed as possible from the provided context. 
                    If the answer is not in the provided context, just say "answer is not available in the context". 
                    Do not provide a wrong answer.

                    Context : \n{context}\n
                    Question: \n{question}\n

                    Answer:
                    """

#@title Graph of Thought implementation
prompt_template_1 = """Construct a graph where nodes represent key ideas, and edges represent the relationships between these ideas. 
                      How can these ideas be connected to form a coherent understanding?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      Graph of Thought:
                      """

#@title Tree of Thought implementation
prompt_template_2 = """Create a tree structure where each branch represents a possible expansion of a core concept. 
                      How can this hierarchy help in understanding the overall content?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      Tree of Thought:
                      """

#@title Graph of Verification implementation
prompt_template_3 = """Construct a graph to verify the relationships between key ideas. 
                      How does this verification impact the overall understanding of the content?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      Graph of Verification:
                      """

#@title Chain-of-Thought (COT) Prompting implementation
prompt_template_4 = """Break down the process of summarizing this content into a chain of logical steps. 
                      What are the intermediate steps required to generate a concise summary?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      Chain of Thought:
                      """

#@title XOT (Everything of Thought) implementation
prompt_template_5 = """Consider every possible thought or interpretation of this text. 
                      How can multiple perspectives be integrated to form a comprehensive understanding?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      XOT of Thought:
                      """

#@title KD-CoT (Knowledge Driven COT) implementation
prompt_template_6 = """Apply domain-specific knowledge to enhance the chain-of-thought process. 
                      How does expert knowledge shape the interpretation and summarization of the text?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      KD-CoT:
                      """

#@title COT-SC (Self-Consistency with COT) implementation
prompt_template_7 = """Ensure that the chain-of-thought process remains consistent throughout the summarization. 
                      How can internal consistency be maintained in the logical flow?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      COT-SC:
                      """

#@title Self-Ask implementation
prompt_template_8 = """Generate questions that the text answers. 
                      What questions arise from the content, and how can answering them clarify the material?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      Self-Ask:
                      """

#@title Self-Critique implementation
prompt_template_9 = """Critically evaluate the generated summary. 
                      What aspects might be inaccurate or misleading, and how can they be corrected?

                      Context : \n{context}\n
                      Question: \n{question}\n

                      Self-Critique:
                      """

#@title Self-Refine implementation
prompt_template_10 = """Iteratively refine the summary by incorporating feedback. 
                       What improvements can be made in each iteration to enhance clarity and accuracy?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Self-Refine:
                       """

#@title Self-Refinement implementation
prompt_template_11 = """Continuously improve the generated content. 
                       How can the content be polished to better align with the original text's intent?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Self-Refinement:
                       """

#@title Iterative Prompting implementation
prompt_template_12 = """Engage in multiple rounds of prompting to gradually refine the output. 
                       How does each iteration improve the quality of the summary?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Iterative Prompting:
                       """

#@title Analogical Prompting implementation
prompt_template_13 = """Use analogies to relate the content to familiar concepts. 
                       How can drawing parallels help in understanding complex ideas?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Analogical Prompting:
                       """

#@title Input-Output Prompting implementation
prompt_template_14 = """For each input (text), specify the expected output (summary). 
                       How can clear examples of input-output pairs guide the generation process?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Input-Output Prompting:
                       """

#@title Least-to-Most Prompting implementation
prompt_template_15 = """Start with the simplest possible summary and progressively add more details. 
                       How does gradually increasing complexity enhance the summary?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Least-to-Most Prompting:
                       """

#@title Plan-and-Solve Prompting implementation
prompt_template_16 = """Develop a plan to tackle the summarization problem and then execute it. 
                       What steps need to be followed to achieve the desired outcome?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Plan-and-Solve Prompting:
                       """

#@title Sequential Prompting implementation
prompt_template_17 = """Break down the summarization into sequential tasks. 
                       How can each step logically follow the previous one to build a coherent summary?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Sequential Prompting:
                       """

#@title Step-Back Prompting implementation
prompt_template_18 = """Take a step back and reassess the current summary. 
                       What broader perspective can be gained by reevaluating the previous steps?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Step-Back Prompting:
                       """

#@title MemPrompt implementation
prompt_template_19 = """Leverage memory of previous prompts to inform the current task. 
                       How can recalling past interactions help improve the summary?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       MemPrompt:
                       """

#@title Chain of Density (CoD) Prompt implementation
prompt_template_20 = """Focus on creating a dense, information-rich summary. 
                       How can the most important details be packed into a concise form?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Chain of Density:
                       """

#@title Reverse JSON Prompt implementation
prompt_template_21 = """Generate a summary in a structured format, such as JSON, that can be easily reversed into the original content. 
                       How does this structure aid in understanding?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Reverse JSON Prompting:
                       """

#@title Symbolic Reasoning implementation
prompt_template_22 = """Apply symbolic logic to the content. 
                       How can formal reasoning techniques help clarify the underlying arguments?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Symbolic Reasoning:
                       """

#@title Generated Knowledge implementation
prompt_template_23 = """Use the text to generate new knowledge or insights. 
                       What novel ideas can be derived from the content?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Generated Knowledge:
                       """

#@title PAL (Program-Aided Language Models) implementation
prompt_template_24 = """Use programmatic aids to enhance the summarization process. 
                       How can algorithms assist in generating more accurate summaries?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       PAL:
                       """

#@title Meta-Ask Self-Consistency implementation
prompt_template_25 = """Ensure that multiple summaries of the same content are consistent with each other. 
                       How can consistency across different iterations be achieved?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       Meta-Ask Prompting:
                       """

#@title ReAct implementation
prompt_template_26 = """React to the generated content by providing immediate feedback. 
                       How can interactive responses guide the improvement of the summary?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       ReAct:
                       """

#@title ART (Automatic Reasoning & Tool-Use) implementation
prompt_template_27 = """Utilize automatic reasoning tools to enhance the summary. 
                       What tools can assist in analyzing and condensing the content?

                       Context : \n{context}\n
                       Question: \n{question}\n

                       ART:
                       """

# Few-Shot Prompting
prompt_template_28 = """Provide a few examples of how to analyze and summarize the content from a PDF document. 
                        Based on these examples, analyze and summarize the following PDF content.

                        Context:\n{context}\n
                        Question: \n{question}\n

                        Response:
                        """

# Zero-Shot Prompting
prompt_template_29 = """
                      Analyze the content from the provided context and generate a summary without any specific examples.

                      Context:\n{context}\n
                      Question: \n{question}\n
                      
                      Summary:
                      """

# Chain of Thought Prompting
prompt_template_30 = """
                      Break down the process of summarizing this content into a series of logical steps. 
                      Consider the structure of the content and the key points to cover.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Chain of Thought:
                      """

# Step-by-Step Instructions
prompt_template_31 = """
                      Follow these explicit instructions to summarize the content:
                      1. Identify the main sections.
                      2. Extract key information from each section.
                      3. Combine the extracted information into a coherent summary.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Summary:
                      """

# Professional PDF Analyst Perspective
prompt_template_32 = """
                      Respond as if you are a professional analyst with expertise in summarizing complex documents. 
                      Adopt their style and perspective to summarize the provided content.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Summary:
                      """

# Detailed Summary
prompt_template_33 = """
                      Use the context provided to generate a detailed summary. 
                      Ensure that the summary reflects the key themes and information presented.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Summary:
                      """

# Researcher Perspective
prompt_template_34 = """
                      Assume the role of a researcher who needs to prepare a summary of the provided content. 
                      Address the key findings and implications based on this role.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Summary:
                      """

# Comparison
prompt_template_35 = """
                      Compare the following aspects of the content:
                      1. The primary arguments presented.
                      2. The evidence supporting these arguments.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Comparison:
                      """

# Iterative Analysis
prompt_template_36 = """
                      Engage in multiple rounds of analysis to summarize the content. 
                      In each turn, refine the summary based on feedback and additional insights.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Turn 1 Summary:
                      """

# Refined Summary
prompt_template_37 = """
                      Refine the initial summary based on detailed feedback. 
                      Iterate to improve the clarity and accuracy of the summary.

                      Context: \n{context}\n
                      Question: \n{question}\n

                      Refined Summary: 
                      """

