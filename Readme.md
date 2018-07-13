<h1>Algiers Apartment Price Prediction </h1>
This is a set of regression algorithms from Scikit-Learn applied to a dataset that I created by scraping Ouedkniss.

This dataset has a total of 3553 samples with a size of 13, features are real positive values and targets are real between 1000 and 3000.        

<h3>Algorithms and results for dataset</h3>

<table>
  <tr>
    <th>Algorithm</th>
    <th>Model performance</th> 
  </tr>

  <tr> <td>Linear Regression + Polynomial Features</td>   <td>0.02067345956704003</td> </tr>
  <tr> <td>Gradient Boosting Regressor </td>   <td>0.12610201107980723</td> </tr>
  <tr> <td>K-Neighbors Regressor</td>   <td>-0.1956575117534145</td> </tr>
  <tr> <td>Decision Tree Regressor + Ada Boost Regressor</td>  <td>0.025200951666729643</td> </tr>
  <tr> <td>Decision Tree Regressor + Bagging Regressor </td>   <td>0.1218648622524763</td> </tr>
  <tr> <td>Random Forest Regressor</td>   <td>0.1303632423343436</td> </tr>
  <tr> <td>Huber Regressor </td>   <td>-0.2150968619259983</td> </tr>
  <tr> <td>Theil Sen Regressor </td>   <td>-0.03935666883265565</td> </tr>
  <tr> <td>Linear Regression + Shuffle</td>   <td>0.052494793812623786</td> </tr>
</table>

<h2>Correlation of selected features for dataset</h2>

<table>
  <tr>
    <th></th>
    <th>Commune</th> 
    <th>Etage</th>
    <th>Superficie</th> 
    <th>Piece</th>
    <th>Prix</th> 
  </tr>
  <tr> 
  	<td>Commune</td>
    <td>1.0</td> 
    <td>-0.15976914085263527</td> 
    <td>0.20950954048367096</td> 
    <td>0.05282241062499728</td> 
    <td>0.0770504304324702</td> 
   </tr>
  <tr> 
  	<td>Etage</td>   
  	<td>-0.15976914085263527</td> 
    <td>1.0</td> 
    <td>0.02088774679844994</td> 
    <td>0.03225100204879875</td> 
    <td>0.0028625214924493715</td> 
  </tr>
  <tr> 
  	<td>Superficie</td>     
  	<td>0.20950954048367096</td> 
    <td>0.02088774679844994</td> 
    <td>1.0</td> 
    <td>0.7423177491115521</td> 
    <td>-0.01459807463078822</td> 
  </tr>
  <tr> 
  	<td>Piece</td>   			
  	<td>0.05282241062499728</td> 
    <td>0.03225100204879875</td> 
    <td>0.7423177491115521</td> 
    <td>1.0</td> 
    <td>-0.02782093484314777</td> 
  </tr>
  <tr> 
  	<td>Prix</td>   
  	<td>0.0770504304324702</td> 
    <td>0.0028625214924493715</td> 
    <td>-0.01459807463078822</td> 
    <td>-0.02782093484314777</td> 
    <td>1.0</td> 
  </tr>
</table>

<h2>Data Profiling for dataset</h2>

<table>
  <tr>
    <th></th>
    <th>Minimum</th> 
    <th>Maximum</th>
    <th>Mode</th> 
    <th>Mean</th> 
    <th>Median</th>
    <th>Standard deviation</th> 
    <th>Quantile [0.25, 0.5, 0.75]</th> 
  </tr>
  <tr> 
  	<td>Commune</td>
    <td>1</td> 
    <td>28</td> 
    <td>4</td>  
    <td>13.17117117117117</td> 
    <td>13.0</td> 
    <td>8.574879777660525</td> 
    <td>[4.0, 13.0, 22.0]</td> 
   </tr>
  <tr>
  	<td>Etage</td> 
    <td>1</td> 
    <td>15</td> 
    <td>1</td>  
    <td>3.1331644144144146</td> 
    <td>3.0</td> 
    <td>2.174971764738508</td> 
    <td>[1.0, 3.0, 4.0]</td> 
  </tr>
  <tr> 
  	<td>Superficie</td>     
    <td>1</td> 
    <td>250</td> 
    <td>75</td>  
    <td>95.88006756756756</td> 
    <td>90.0</td> 
    <td>33.34758832480636</td> 
    <td>[75.0, 90.0, 115.0]</td> 
  </tr>
  <tr>
  	<td>Piece</td>   
    <td>1</td> 
    <td>9</td> 
    <td>3</td>  
    <td>3.516328828828829</td> 
    <td>3.0</td> 
    <td>0.8903647264348437</td> 
    <td>[3.0, 3.0, 4.0]</td> 
  </tr>
  <tr>
  	<td>Prix</td>   
    <td>1000.0</td> 
    <td>3000.0</td> 
    <td>2000.0</td>  
    <td>1905.3470157657657</td> 
    <td>1800.0</td> 
    <td>553.3634995790693</td> 
    <td>[1450.0, 1800.0, 2350.0]</td> 
  </tr>
</table>

<h2>Plot features for dataset</h2>

<h4>Commune</h4>

![commune](https://user-images.githubusercontent.com/19336306/42030378-87190468-7aca-11e8-8c64-60f721b4ce4d.png)

<h4>Etage</h4>

![etage](https://user-images.githubusercontent.com/19336306/42030380-87579d9a-7aca-11e8-86a0-97f9606e0bac.png)

<h4>Piece</h4>

![piece](https://user-images.githubusercontent.com/19336306/42030381-8794c422-7aca-11e8-9c08-7250624f36b8.png)

<h4>Superficie</h4>

![superficie](https://user-images.githubusercontent.com/19336306/42030382-87c79118-7aca-11e8-8141-4a55219ecfaf.png)

<h2>Requirements</h2>
Python 2.7 and up

<h2>Installation</h2>
The followoing are the prerequiste Python modules that needs to be installed to execute main.py:

	sudo pip install pandas
	sudo pip install -U scikit-learn
	sudo pip install numpy
	sudo pip install matplotlib

<h2>Downloads</h2>
Clone the repository using the below mentioned command and execute the Python program.
	
	git clone https://github.com/Sehaba95/Algiers-Apartment-Price-Prediction.git
	cd Algiers-Apartment-Price-Prediction/Regressors
	python AdaBoostRegressor.py

<h2>Authors</h2>

	Sehaba Amine


<h2>Contributors</h2>

[Okba BEKHELIFI](https://github.com/okbalefthanded)
