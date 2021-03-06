# FoodRecommendation

In this project, we tested the performance of R-Trees and KD-Trees on storing and retrieving location-based data. By performing a multi-stage rigorous performance analysis, we observe that KD-Trees are faster than R-Trees in the building as well as the searching process. We then utilize the algorithms to build a food recommendation system. Our system runs a web-based application on the front end. Users can input their custom location, or they can allow the location services to extract their current location for them. They can then adjust other parameters such as cuisine type and the radius of the search for refining their search experience. We implemented the underlying algorithms in a local server, and the web application communicated the input and output with the server. We implemented the server as an Express application and the underlying algorithms on C++ and Python. 


# KDTree Document

https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree

https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html

# Web Application

Our web-based application is hosted on the Heroku app and accessible via
http://ec504project.herokuapp.com/. Due to the lack of an SSL certificate, the web application
doesn’t open with HTTPs, hence we need to manually enter HTTP for now, as a limitation. The
browser opens https by default, hence we need to enter the http:// URL to run the demo
properly.

# Report

The full report of the the project including benchmarks and analysis is available in the repo
