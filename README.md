# **<p align="justify">Data Science 4 Covid19</p>**  

<p align="justify">
What is Text Mining? Text Mining is the process of deriving meaningful information from natural language text. Natural Language Processing (NLP) is a part of computer science and artificial intelligence which deals with human languages. In other words, NLP is a component of text mining that performs linguistic analysis that essentially helps a machine to “read” text. Sentiment analysis uses NLP and is a powerful tool that allows computers to understand the underlying subjective tone of a piece of writing.
</p>

<p align="justify">
Covid-19 epidemic had a high impact on social media usage worldwide with comments and information being spread from multiple sources. Some sources may be credible entities and experts, while others may be merely opinions and emotions originated by the users. In this scenario, text mining analysis may prove an important tool in order to identify what drives the public conversation and the impact of Covid-19 in our lives and to identify changing emotions and sentiments during this difficult time. A tool capable to detect fake news would make social media a more secure place.<br/>

For this work we plan to use the following dataset:<br/>
https://www.kaggle.com/gpreda/covid19-tweets<br/>
https://github.com/cuilimeng/CoAID  
</p>

Our objectives are:  
* Visualize the data and perform an exploratory analysis.  
* Analyze Covid-19 related tweets using text mining tools.  
* Train a deep learning model to classify fake and real news.  

---
Exploratory_data_analysis.ipynb - jupyter file containing the exploratory data analysis of our dataset.<br/>
Modelos (3).ipynb - jupyter file containing the models created.<br/>
processing.py - Class created to apply pre-processing functions, in order to clean the dataset text.<br/>

<details>
<summary>"processing.py"</summary>
<font size="5">
<p align="justify">
It transforms text into amore digestible form so that deep learning algorithms can perform better.<br/>
There are the main componentsabout doing text pre-processing:<br/>

* Remove extra whitespaces
* Convert accented characters
* Remove special characters and numbers•  Lowercase the text
* Remove common words that have no impact in the process of classification (’stopwords’)
* Apply stemming, reducing inflected/derived words to their word stem, base or root form.
* Tokenization - splitting strings of text into smaller pieces, or “tokens”. Paragraphs can be tokenizedinto sentences and sentences can be tokenized into words
* Encoding - Assign a numerical character to each token, a applying a process a post padding, to fillwith zeros, the vectors under the length of 30 tokens.
* Assign the respective dimensions of the pre-trained Embedding, to each word (represented bynumbers after the encoding). In this case we tested with two different Embeddings from Glove. Theglove.twitter.27b, an embbeding oriented to twitter text mining and glove.6B, developed for newscontent. Since we are working directly with the content and titles of the news shared on Twitter andnot with the posts per say shared on the platform, the second one should provide better results.
</p>
</font>
</details>

























