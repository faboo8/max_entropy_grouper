# Entropy-based grouping of items with discrete features 


<p align="center">
  <img src="https://github.com/faboo8/ontology-matching/blob/master/media/0.jpg" alt="sign"/>
</p>

A general purpose module that provides grouping of items with a set of discrete features e.g. a list of people with gender, nationality and age. It takes a pandas dataframe with a structure like: 

`{ name | feature_1 | feature_2 | ... | feature_n } `

and tries to find *N* groups with each giving maximun entropy or - in layman's terms - the most diverse groups.


## Computing 'diversity'

A measure of how 'diverse' a set *X* is, is the so-called Shannon entropy:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/entropy_general.gif" alt="eq1"/>
</p>

Shannon entropy is defined for a given discrete probability distribution; it measures how much information is required, on average, to identify random samples from that distribution. In this context in can be seen as: How can one seperate a set into *N* groups with each group trying to mimic the original's probability distibution best?** From the definition of entropy, it follows that different systems' entropy combine additively thus, the maximum entropy of a group is (given ideal splitting) *H/N*. The actual value will hover around that.

To simplify, let's assume that *X* has 100 elements and only one feature *y* that can take 2 states. Both states are assumed equally. Thus, the entropy is:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/entr_ex.gif" alt="eq2"/>
</p>

Next, we want to seperate this set into 4 groups with 25 elements each. First, groups are assigned randomly and their individual entropy is:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/entr_ex2.gif" alt="eq3"/>
</p>

To best represent the initial set, these probabilities should best approach the initial ones. The way I chose to approach this is to maximize (with one caveat) the individual entropies. 

However, one has to consider the case when a state feature in the initial set is e.g. only assumed 2 times. Thus, in the group the maximun entropy should be approached by:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/entr_spec.gif" alt="eq4"/>
</p>

The optimization algorithm is pretty straightforward. We choose two groups at random, from these two groups then we again choose one element each at random, propose a switch, check if the entropy is increasing and if so accept the change. Otherwise we start over. This is not very efficient but given enough iterations finds an optimal grouping. 

One small (optional) feature is a random swap (chance: 1 in 1500) that will accept a change even when the entropy is decreasing. The thought behind this is to avoid getting stuck in a local maximum. However, I have not encountered a situation where the inclusion of this yielded a better result but hey - who knows? 


## How to use

[I changed a bit so it is not working right now]

Usage is fairly simple. Install the package via the command line,
```
python setup.py install
```

import the class

```python
from GroupingClass import EntropyGrouping 
```

and create an instance:

```python
grp = EntropyGrouping(df, name_columnm, feature_columns, N, random_swap, shuffle)
result = grp.find_best_groups(n)
```
**Parameters**
* df  : pandas.DataFrame  
    - DataFrame with name column and features that shall be used for grouping
    - Can include more columns too
* name_column  : str 
    - Name of the column that should be used for grouping
* feature_column  : list 
    - List of column names from Dataframe to use for the calculation of entropy
    - e.g. ['gender', 'nationality']
* N  : int
    - Number of groups that df should be split into
* random_swap  : boolean, optional
    - Leads to random swaps along the optimization
    - Default: False
* shuffle  : boolean, optional
    - Leads to random shuffling of the dataframe befor the optimzation
    - If the Dataframe has some kind of order this will generally lead to faster convergence
    - Default: True
* n  : int, optional
    - Number of iterations for optimization
    - Default: 'auto' = 2*(length dataframe)^2/N (needs re-assessment)
    
## Notes

- The length of the list and number of groups do not have to divisible e.g. 62 can be split into 4 groups containing 15, 15, 16 and 16 elements. 

- Convergence for splitting into *N* groups roughly scales like *~2/N* (not verified yet). For the following benchmarks I'm using a list containing 62 items with 3 features.

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/bmk2.png" alt="bmk"/>
</p>

- So far I have not found an intuitive explanation why the entropy is increasing with *N*. However, the number of features *seems* to be a determining factor:

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/bmk3.png" alt="bmk"/>
</p>

Considering the artifacts due to the small size of the list, I propose (note that I inverted the sign for the entropy):

<p align="center">
  <img src="https://github.com/faboo8/max_entropy_grouper/blob/master/media/entr_prop.gif" alt="bmk"/>
</p>




## Tasks

- [ ] Implement convergence criteria
- [x] Make package installable
- [ ] Add terminal usage e.g. for excel files
- [ ] Make usable for non-discrete features by binning them
