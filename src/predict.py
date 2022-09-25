import requests

prediction = requests.post(
    #"http://127.0.0.1:5000/predict", #for local inference
    "https://customer-segmentation-8202.herokuapp.com/predict", # for heroku 
    headers={"content-type": "application/json"},
    data='{"Income": 80000, "Recency": 58, "NumWebVisitsMonth": 2, "Complain": 0, "age": 25,"total_purchases": 25,"enrollment_years": 10,"family_size": 1}',
).text

print(prediction)