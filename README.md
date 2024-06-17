# Farm Easy - Crop Recommendation System

The agriculture industry is important for the global economy as it provides food, jobs, and income for many people. However, it faces challenges that affect productivity and profitability. One major challenge is the lack of knowledge in choosing and managing crops, which leads to lower yields and less profit.

To address this challenge, a crop recommendation system that uses machine learning has been developed. This system uses machine learning algorithms to analyze data on crop requirements and growth conditions. Based on this information, personalized recommendations can be given to farmers based on their specific conditions, such as soil type, climate, and topography.

The system collects and analyzes data from various sources, including satellite images, weather patterns, soil samples, and crop growth models. Machine learning algorithms are then used to predict the best crops to grow in a particular location. The system also provides recommendations on when to plant, which seed variety to use, and how to irrigate in order to maximize yield.

Several machine learning algorithms can be used for this system, such as decision trees, neural networks, support vector machines, and random forests. These algorithms are trained using historical data on crop yields, soil and weather conditions, and other relevant parameters to make accurate predictions.

One of the main benefits of this system is that it helps farmers make informed decisions on crop selection and management. By receiving personalized recommendations based on their specific conditions, farmers can optimize yields and maximize profitability. The system also promotes sustainable farming practices by reducing waste and improving soil health.

This application helps farmers increase agricultural productivity, prevent soil degradation, reduce chemical use, and maximize water resource efficiency.

In conclusion, the use of machine learning for crop recommendation is a powerful solution that can revolutionize the agriculture industry. By leveraging machine learning algorithms and advanced technologies, personalized recommendations can be provided to farmers, leading to higher yields, improved profitability, and sustainable farming practices.

# [Installation]()
```bash
pip install -r requirements.txt
```

# [Usage]()
```bash
python app.py
```

# [Technologies Used]()
* Python 3.9

# [Dataset]()
This dataset was created by combining rainfall, climate, and fertilizer data available for India.

### [Attributes information:]()

* **N** - Nitrogen content ratio in soil
* **P** - Phosphorous content ratio in soil
* **K** - Potassium content ratio in soil
* **Temperature** - temperature in degree Celsius
* **Humidity** - relative humidity in %
* **ph** - soil pH value
* **Rainfall** - rainfall in mm

### [Experiment Results:]()
* **Data Analysis**
   * All columns contain outliers except for N.
 * **Performance Evaluation**
   * The dataset was split into 80% training set and 20% validation set.
 * **Training and Validation**
   * GaussianNB achieved the highest accuracy score among other classification models.
   * GaussianNB (99% accuracy score)
 * **Performance Results**
   * Training Score: 99.5%
   * Validation Score: 99.3%

# References
* [Crop Recommendation System using Machine Learning for Digital Farming](https://www.prolim.com/crop-recommendation-system-using-machine-learning-for-digital-farming/)
* [Crop Recommendation System using Machine Learning Techniques](https://www.irjet.net/archives/V4/i12/IRJET-V4I12179.pdf)
* [Crop Recommendation using Machine Learning](https://ieeexplore.ieee.org/document/8768790)
* [Crop Plantation Recommendation using Feature Extraction and Machine Learning Techniques](http://sersc.org/journals/index.php/IJAST/article/view/30399)
* [FarmEasy: Crop Recommendation Portal for Farmers](https://towardsdatascience.com/farmeasy-crop-recommendation-portal-for-farmers-48a8809b421c)
* [Crop Recommendation Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)
* [Crop Recommendation based on Soil and Climate Parameters](http://agri.ckcest.cn/ass/8185d605-6c4d-4d8a-b280-c867c2304d42.pdf)

