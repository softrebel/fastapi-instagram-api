# fastapi-instagram-api
A simple project to use instagram apis such as login, get followers, following and etc.


## Requirements:
- python 3.8
- install dependencies using `pip install -r requirements.txt`
- Copy `.env.sample` and rename it to `.env.local`. Then fill the variables
- Create MongoDb database with name `SinaDb`
- run command `python -m main` in the root folder.



## Future Work
- Encapsulate requests in Ig model
- Change print to logging
- Add middlewares to support logging and error handling
- Implement Repositry Pattern to interact with database
- Implement IOC Container
- Implement Database driver pattern
- Implement Redis Cache

