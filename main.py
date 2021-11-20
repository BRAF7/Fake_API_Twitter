#FastAPI
from fastapi import FastAPI, status, Body
#Python
import json
from typing import List, Optional
#Models
from models import User, Tweet, UserRegister


#we defined our app
app = FastAPI()

#Path Operations
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def sign_up(user: UserRegister = Body(...)) -> None: 
    """
    Signup
    This path operation register a user in the app
    Parameters: 
        - Request body parameter
            - user: UserRegister
    
    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: str
    """
    with open('users.json', 'r+', encoding='utf-8') as f:
        #castin archive to json
        results = json.loads(f.read())
        #casting user to dict
        user_dict = user.dict()
        #This parameters aren´t str so we cast them to str
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        #we're moving to the first position
        f.seek(0)
        # then we write
        f.write(json.dumps(results))
        return user



#Get all users
@app.get(
    path          ='/users',
    response_model= List[User],
    status_code   = status.HTTP_200_OK,
    summary       ='Show all users',
    tags          =['Users']
)
def list_users() -> List[User]:
    """
    Get all users

    Returns a json with:
        User´s with the following keys:
        -user id
        -email
        -first name
        -last name
        -birthday (Optional)
    """
    with open('users.json', 'r', encoding='utf-8') as f:
        result = json.loads(f.read())
        return result



#Get one user
@app.get(
    path          ='/user/{id_user}',
    response_model= User,
    status_code   = status.HTTP_200_OK,
    summary       ='Show a user',
    tags          =['Users']
)
def get_user() -> User:
    pass 



#Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user(): 
    pass



#Update a user
@app.put(
    path          ='/user/{id_user}/update',
    response_model= User,
    status_code   = status.HTTP_200_OK,
    summary       ='Update a user',
    tags          =['Users']
)
def update_user() -> User:
    pass 



### Show  all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home() -> dict:
    """
    ## Home app

    This path operation show all tweets in the app

    ## Parameters:
  
    ## Returns a json list with all tweets in the app, with the following keys:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json",'r',encoding='utf-8') as f:
        results = json.loads(f.read())
    return results



### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)): 
    """
    Post a Tweet
    This path operation post a tweet in the app
    Parameters: 
        - Request body parameter
            - tweet: Tweet
    
    Returns a json with the basic tweet information: 
        tweet_id: UUID  
        content: str    
        created_at: datetime
        updated_at: Optional[datetime]
        by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        #Here we're accesing to the informacion inside by 
        #so we can cast de id and the birth
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet


### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet(): 
    pass



### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet(): 
    pass



### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet(): 
    pass