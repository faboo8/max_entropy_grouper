# Entropy-based grouping of items with discrete features 


<p align="center">
  <img src="https://github.com/faboo8/ontology-matching/blob/master/media/0.jpg" alt="sign"/>
</p>

A general purpose module that procides the grouping of items with a set of discrete features e.g. a list of people with gender, nationality and age. It takes a pandas dataframe with a structure like: 

`{ name | feature_1 | feature_2 | ... | feature_n } `

and tries to find *N* groups with each giving maximun entropy or - in layman's terms - the most diverse groups.


## Computing 'diversity'

A measure of how 'diverse' a set *X* is, is the so-called Shannon entropy:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/CodeCogsEqn.gif" alt="eq1"/>
</p>

Shannon entropy is defined for a given discrete probability distribution; it measures how much information is required, on average, to identify random samples from that distribution. In this context in can be seen as: How can one seperate a set into *N* groups with each group trying to mimic the original's probability distibution best. 

To simplify, let's assume that *X* has 100 elements and only one feature *y* that can take 2 states. Both states are assumed equally. Thus, the entropy is:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/CodeCogsEqn%20(1).gif" alt="eq2"/>
</p>

Next, we want to seperate this set into 4 groups with 25 elements each. First, groups are assigned randomly and their individual entropy is:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/CodeCogsEqn%20(2).gif" alt="eq3"/>
</p>

To best represent the initial set, these probabilities should best approach the initial ones. The way I chose to approach this is to maximize (with one caveat) the individual entropies. 

However, one has to consider the case when a state feature in the initial set is e.g. only assumed 2 times. Thus, in the group the maximun entropy should be approached by:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/CodeCogsEqn%20(3).gif" alt="eq4"/>
</p>

The optimization algorithm is pretty straightforward. We choose two groups at random, from these two groups then we again choose one element each at random, propose a switch, check if the entropy is increasing and if so accept the change. Otherwise we start over. This is not very efficient but givenm enough iterations finds an optimal grouping. 

## How to use
