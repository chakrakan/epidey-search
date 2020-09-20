<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/chakrakan/epidey/">
    <img src="https://github.com/chakrakan/epidey-search/blob/master/docs/epidey-logo.png" alt="Logo" width="350" height="200">
  </a>


  <p align="center">
    <a href="https://github.com/chakrakan/epidey/wiki">
    <img alt="Project Wiki" src="https://img.shields.io/badge/-project%20wiki-blue"></a>
    <a href="https://github.com/chakrakan/epidey/projects">
    <img alt="Kanban Board" src="https://img.shields.io/badge/-kanban%20board-orange"></a>
  </p>
</p>


### Who am I?

👋	Hi I am Kanisk, a software engineering student from Canada!

### The Problem

-	In today’s world, there is information overload, not just in the realms of the internet, but in the field of research
-	Given we are currently in a pandemic, I decided to focus specifically within the domains of health-based research
-	There are many research labs and researchers who come up with creative ways to treat complex diseases such as cancers, dementias (Alzheimers, Parkinson's, etc.), and even Mental health issues. Results from these labs are opinions based upon genetics and environmental factors. It is inevitable there is overlap in the research. 
-	But, it also makes it impossible for any one clinician to be up-to-date on all these opinions. Finding the most effective initial treatment option as well as planning treatment is a monumental task which involves scouring through numerous research papers with trial and error, but is critical to improve patient outcome.
-	According to a study by Velo and Minuz, 2009 – Inadequate knowledge of competence and incomplete info about clinical characteristics result in prescribing faults, including the use of potentially inappropriate medications

### The Solution

-	This process of finding the most relevant research papers or resources can be automated using Jina to enable healthcare practitioners the ability to provide the best patient care.

#### Introducing Epidey

-	Epidey is an initial stage MVP built using Python and Vue, leveraging the Jina AI framework to perform searches for relevant resources as needed for clinicians and researchers alike
-	It works by creating an opinion of both – the query being input by the user, and the data being indexed by Jina
-	To demonstrate what I mean, let’s see an example...

The example isn’t based in healthcare, however, it’s easy to see how this would translate over into topics within health care based on the data-set  

![](https://github.com/chakrakan/epidey-search/blob/master/docs/epidey-demo.gif)

-	Here, I already have an initial topic that I want to work with which is regarding `COMET`, a single pass MapReduce algorithm.
- Then I create my hypothesis about this topic – that this approach is appropriate when learning from massive-scale data that is too large to fit on a single-machine.
- The results get populated! 🎉

-	From a researcher standpoint, I have been pointed at the relevant article which I can continue reading to further perform trial and error
-	Or, based on the cosine similarity of the search and the sentiment of the articles in relation to it, I can continue to look at the top-k articles recommended to me by Jina

> NOTE: this demo is a very rough MVP of what the project can become eventually with more time and research into this topic. As a beginner, I was able to share this idea, and if I had more time, I would like to actually implement the bi-directional sentiment analysis with the query and also create a cluster of similar research papers based on their sentiments and vector distance which the researcher could further choose to dive into.

I thank Jina for the wonderful opportunity to let me explore the world of ML and hope everyone is well and safe during the pandemic.

Thanks!

### Some more screenshots

![](https://github.com/chakrakan/epidey-search/blob/master/docs/sc1.png)  

![](https://github.com/chakrakan/epidey-search/blob/master/docs/sc2.png)     

![](https://github.com/chakrakan/epidey-search/blob/master/docs/sc3.png)  

![](https://github.com/chakrakan/epidey-search/blob/master/docs/sc4.png)



