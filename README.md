# SOSI
### Background
This project aims to leverage semantic technologies to detect soccer offside in real time
SOSI stands for "socer offside semantic importance"
> semantic importance is a concept proposed by [Rui Yan et al.](http://events.linkeddata.org/ldow2016/papers/LDOW2016_paper_13.pdf).
It facilitates the problem of data eviction in the stream reasoning context. Semantic importance evaluates the contributions or potential contributions of the streaming data to the query execution. The semantic importance can be embodied as a priority vector, where each element is ranked by preference. The data being processed is then ranked according to their semantic importance priority vector. The data with small semantic importance priority vector will be evicted. 

The original streaming data is in csv format, for more details, please refer to this [paper](http://delivery.acm.org/10.1145/2490000/2488283/p289-mutschler.pdf?ip=128.113.243.82&id=2488283&acc=ACTIVE%20SERVICE&key=7777116298C9657D%2EAF047EA360787914%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&CFID=617127925&CFTOKEN=68145667&__acm__=1463579274_640ab246f722c5d02658a5f11df48ab3) and their [website](http://www.orgs.ttu.edu/debs2013/index.php?goto=cfchallengedetails). In order to implement this use case, we develop a [soccer offside ontology](https://tw.rpi.edu/web/Courses/Ontologies/2016/projects/soccer/ontology#onto). We also annotate the csv data into RDF, then stream it into our system.

The dataset comes with a video record of the soccer training match. One of our collaborators is a certified referee who can provide us a list of soccer offside cases. He provided 20 cases composing *sure offside offence*, *sure no offside offence* or *unsure offside offence so no flag*. We evaluate our system against his list.

### Installation
1. this system is implemented with [stardog](http://stardog.com/)v4.0-rc3, but can work with the latest stardog version 4.2.2 (as of Jan, 7, 2017), download and install it in your local machine. We use the default port as 5820.
2. start your stardog service, create a new database named "db", edit its configuration with "reasoning type - DL", and "query across graphs - true". You need to put the db offline first before hit the "edit" button. 
   * to set reasoning type as DL is very important. The new versions of stardog doesn't support to specify reasoning type in their APIs, instead, they use SL (DL + customer specified rules) as the default reasoning type. If use SL, for this use case, no correct results will be given, thus users has to manually set it to DL. Stardog developers claim that the reasoning type is set by evaluating the query, ontology and data loaded.
3. make sure your java version is 1.8 
4. make sure you have [ant](http://ant.apache.org/)
5. go to your command line and enter ant, the system will run.
