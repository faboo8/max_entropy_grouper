# Entropy-based grouping of items with discrete features 


<p align="center">
  <img src="https://github.com/faboo8/ontology-matching/blob/master/media/0.jpg" alt="sign"/>
</p>

A general purpose module that procides the grouping of items with a set of discrete features e.g. a list of people with gender, nationality and age. It takes a pandas dataframe with a structure like: 

`{ name | feature_1 | feature_2 | ... | feature_n } `

and tries to find *N* groups with each giving maximun entropy or - in layman's terms - the most diverse groups.


## Computing 'diversity'

A measure of how 'diverse' a set is, is the so-called Shannon entropy:

Shannon entropy is defined for a given discrete probability distribution; it measures how much information is required, on average, to identify random samples from that distribution. In this context in can be seen as: How can one seperate a set into *N* groups with each group trying to mimic the original's probability distibution best. 


## How to use
