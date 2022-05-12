# kreuzer-skarke-invariant-ML
The file v26.gz is taken from http://quark.itp.tuwien.ac.at/~kreuzer/V. It contains around 78,000 reflexive polytopes, each corresponding to a different Calabi-Yau 3-fold.
Entries look like this:

```
4 26  M:51 26 N:11 10 H:6,46 [-80]
   1   0   0   0   0  -1   0   0   0   0  -2   2  -1   1   0  -1   0  -2   2   1  -1  -2   0   2   0   1
   0   1   0   0  -1   0   2   0   0  -2   0   0   1  -1  -2   0  -1   0   0   0  -2  -1   1   1   2   2
   0   0   1   0   1   1  -1   1  -1   1   1  -1   1   0   1  -1   1   0  -1   0   1   1  -2  -2  -2  -2
   0   0   0   1   1   1  -1  -1   1   1   1  -1   0   1   0   1  -1   1  -2  -2   1   1   0  -2  -1  -2
```

The numbers in the first line mean (taken from http://www2.macaulay2.com/Macaulay2/doc/Macaulay2-1.18/share/doc/Macaulay2/ReflexivePolytopesDB/html/___Kreuzer-__Skarke_spdescription_spheaders.html):         
            
'4 10': the first 2 numbers are the number of rows and columns of the matrix $A$            
            
'M:25 10': number of lattice points and the number of vertices of the 4-dimensional lattice polytope $P$ which is the convex hull of the columns of the matrix $A$            
            
'N: 10 9' is the number of lattice points and the number of vertices of the polar dual polytope $P^o$ of $P$            
            
'H: 5,20 [-30]' are the Hodge numbers $h^{1,1}(X)$, $h^{1,2}(X)$, and the topological Euler characteristic of $X$, where $X$ is the Calabi-Yau variety described next            
The last four lines stand for 26 vectors in 4-dimensional Euclidean space.
Note that permuting columns and permuting rows of this matrix describes a polytope that encodes an isomorphic Calabi-Yau 3-fold.
