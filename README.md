# Second-Hand-Car-Price-prediction


Overview

Given datasets collected from used cars advertisements. Task is to build and evaluate machine learning algorithms that will predict the price of used cars.

The datasets are divided into training and testing sets. models are trained on the training dataset, and used the testing dataset for testing and evaluation purposes only.

Compare the test dataset's price USD with your predictions using Mean Absolute Error as the main evaluation metric.


Data

manufacturer_name: the name of the car manufacturer
transmission: type of car transmission
color: the car's body color
odometer_value: how many kilometers are recorded on the car
year_produced: the year the car has been produced
engine_fuel: car engine's fuel type
engine_type: car engine's type
engine_capacity: the capacity of the engine in liters
body_type: car body's type
has_warranty: does the car have warranty?
ownership: new/owned/emergency. emergency means the car has been damaged previously severly.
type_of_drive: front/rear/all type of drive
is_exchangeable: if True, the owner of the car is willing to exchange the car with other cars
number_of_photos: the number of photos the car's advertisement contains
number_of_maintenance: the number of times the car has been repaired or serviced
duration_listed: the number of days the car's advertisement is listed
price_usd: the price of the car in the advertisement. The label to predict
