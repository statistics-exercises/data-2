# Calculating the mean of a data set

When you drew your scatter graph in the previous exercise you probably saw that there is not much of a pattern.  A second step we might, therefore, take to analyse the data to compute some summary statistics.  In this exercise, therefore, we are going to use Python to calculate the mean of the data set.
  
As you know we calculate the mean of a data set by:

1. adding all the data points in the set together 
2. and by then dividing by the total number of data points.

We can express this procedure using the following equation:

![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{N}\sum_{i=1}^{N}X_i)

where the symbol ![](https://render.githubusercontent.com/render/math?math=X_i) is used to indicate the ith of the points in our data set.

In the code on the right I have loaded the data set into the list called `x` for you again by writing the command:

````
x = np.loadtxt("data.dat")
````

To compute the mean you will need to write a for loop in order to add together all the elements in this list.  You will then need to divide this sum by the length of `x`, which you can calculate using:

````
N = len(x)
````

To pass the test you will need to have a variable called `mean`. This variable must be set equal to the mean for the data set. You should print the value of `mean` for your own benefit.
