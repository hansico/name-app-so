# aca-dev-name-api 2021

## Instructions
### Requirements
See requirements.txt, basically just ```pip install Flask```.
### Running
```python serv.py``` 
### Access api
#### /api/names   
> Returns json object matching the given parameters. Invalid requests return a
> string with information to fix the issue.
> - *optional* parameters: 
>    - **keys** \- Returns values with the given key(s). To use
         multiple keys separate them with |. E.g. ```name|amount```. Allowed
         values: ```name```, ```amount```. Default: ```name```
>    - **sort** \- Returned query is sorted by this value. Allowed
      values: ```amount```, ```name```. Default: ```None```
>    - **reverse** \- If sort is given the order of the returned
      query is determined by this value. Allowed values: ```False```, ```True```. Default: ```False```

#### /api/names/count
> Returns the requested name count as a string. 
> - ***required*** parameters:
>   - **name** \- Returns the number of people with given name. Using
>     ```*``` returns the sum of all people. Default: ```*```