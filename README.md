# CarCar

Team:

* Shahem Al Hadid - Sales
* Ryan Curry - Service

## Design

We used domain driven design to build microservices. We have an inventory microservice, a sales microservice and a service microservice that allow us to manage our inventory, sales, customer and employee data. We used REST APIs for each microservice. We integrated the React framework to build a frontend UI to allow users to interact(create, read, delete) with our application and manage their inventory. We used docker containers to manage each service.

## Service microservice

Explain your models and integration with the inventory
microservice, here.

## Sales microservice

Created 3 models(Salesperson, Customer, and Sale) and 1 value object(automobile). The automobile value object links our sales to an automobile in our inventory microservice. Whenever an automobile is assigned to a sale, an automobile value object is created in our sales microservice database as a column in the table to link the automobile to the sale. Our salesperson, customer, and sale models allows us to save the respective data in our databases. The salesperson model allow us to input and our salespeoples' names while also creating and assignin a unique employee id to each employee. Our customer model allows us to create a database of all our customers' names, addresses, and phone numbers. The sale model has an automobile property that is there to link the automobile value object to an automobile in our inventory microservice. The salesperson and customer properties in our sales model grabs data from our salesperson and customer models and links them to a specific sale. We protected salesperson and customer properties on delete to avoid deleting the respective data when a sale is deleted and also to protect against deleting a salesperson or a customer that have already been assigned to a sale.
