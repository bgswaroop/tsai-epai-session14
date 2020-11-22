# EPAi session14 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session14 objectives
This assignment, helps to code the concepts that are learnt in the session 14 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

- List Comprehensions
- Iterating Collections
- Iterators
- Iterators and Iterables
- Consuming Iterators Manually
- Cyclic Iterations
- Lazy Iterables
- In-Built Iterables
- Sorting Iterables
- The iter() function
- Iterating Callables
- Delegating Iterators
- Reversed Iteration
- Using Iterators as function arguments

---

Look at the test_polygons_modules.ipynb jupyter notebook to run some sample test cases and examples.
 
---
## Polygon
class methods


**__init__(self, n, R)**

        Instantiate a Polygon
         : param n :  number of vertices
         : param R :  circum radius

**count_edges(self)**
        
        Property


**circumradius(self)**
        
        Property


**count_vertices(self)**
        
        Property


**interior_angle(self)**
        
        Property


**side_length(self)**
        
        Property


**apothem(self)**
        
        Property


**area(self)**
        
        Property


**perimeter(self)**
        
        Property

**__repr__(self)**

        Representation of a polygon
         : return :  str

**__eq__(self, other)**

        Check for equality of two polygons
         : param other :  Other Polygon
         : return :  bool

**__gt__(self, other)**

        Verify if the current polygon is greater than the other polygon
         : param other :  another polygon
         : return :  bool

---
## Polygons
class methods


**__init__(self, m, R)**

        Initialize the polynomial sequence
         : param m :  maximum number of vertices
         : param R :  float circum radius

**max_efficiency_polygon(self)**

        determine the polynomial with maximum efficiency
         : return :  Polynomial

**get_polygon(self, n, R)**


**__getitem__(self, item)**

        Implementing getitem to make this Class a sequence
         : param item :  index for the sequence
         : return :  the polynomial element

**__len__(self)**

        Determine the length of the sequence
         : return :  int

**__repr__(self)**

        Formatted representation of the poly sequence
         : return :  str

**__iter__(self)**


**__init__(self, polygon, radius, max_vertices)**


**__iter__(self)**


**__next__(self)**


