# Data-Kaveri

# Flask App with MySQL
It is a simple web application which provide a user-friendly interface in which user can enter there information the it will process the information and store it into the database.

*The application consists of two main component:*

Flask App: A python based web app build using the Flask framework.
MYSQL Database: A relational database for storing application data.

### Setup and Deployment using Docker Compose

To set up and deploy the application using Docker Compose, follow these steps:

1. Clone the repository: `git clone https://github.com/syntax2/Data-Kaveri.git`
2. Build and run the Docker containers: `docker-compose up -d`
3. Access the application: Open your browser and visit `http://localhost:8000/home`

### Setup and Deployment in Kubernetes (K8s)

To set up and deploy the whole application in Kubernetes, follow these steps:

1. `minikube start`
2. Apply the Kubernetes manifests: `kubectl apply -f mysql-deployment.yaml and kubectl apply -f flask-deployment.yml`
3. Monitor the deployment status: `kubectl get pods`
5. Access the application: Run `minikube service flask-app` to open the application in your default browser. Then add `/home` to see the interface .

And for seeing the application running on the http://localhost:8000/home use 

`kubectl port-forward service/flask-app 8000:8000`

## Approach and Configuration Details

### Configuring the Web Application to Talk to the Database in K8s

When the Flask application container needs to communicate with the MySQL database, it uses the Kubernetes Service named *mysql-service* to resolve the database's network address.
The mysql-service acts as an abstraction that provides a stable virtual IP and DNS name for the MySQL database.
*The Flask application container connects to the mysql-service using the DNS name (mysql-service) and the specified port (e.g., 3306) to establish the connection with the MySQL database.*

( on the app level they use a library called mysql-connector-python and the MYSQL credentials provided in the app code)

### Exposing the Web Application in K8s to the Outside World


the web application is exposed to the outside world in Minikube using a NodePort service type, The type: NodePort configuration makes the service accessible on a high-numbered port on each node in the cluster.

The NodePort service type maps a port on the Kubernetes nodes to a port on the service, allowing external access to the service


### Auto Scaling Configuration

the HPA monitors the CPU utilization of the Flask application pods. If the CPU utilization exceeds the target threshold (40%), the HPA will automatically scale up the number of replicas up to the maximum specified (3 replicas). If the CPU utilization drops below the target threshold, the HPA will scale down the number of replicas to the minimum specified (1 replica).


**Remember** to enable the Metrics Server in your minikube to collect the necessary CPU metrics for the HPA to function correctly.

**Testing the HPA**

I am  using apache bench (ab) as a load generator to test that auto-scaling is working.
`ab -n 1000 -c 10 http://192.168.49.2:31794/home`
or you can use the http://localhost:8000/home url after running the port-forwarding command.

*for making custom command:*
*-n 1000*: This specifies the number of requests to be sent to the URL.
*-c 10:* it determines the number of multiple requests to send at a time. 
