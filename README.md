To run API with Docker run following commands:
docker build -t radio:latest
docker run -p 80:80 radio:latest

To run API without docker use following commands:
pip install -r requirements.txt
python app.py


Environment variable with the name 'host_ip' defines host ip.
Default value: localhost

api endpoints info can be reached via swagger at:
http://localhost/apidocs/