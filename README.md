# dev-academy-exercise 2021

## Instructions
#### /api/names   
> - *optional* parameters: 
>    - **keys** \- Returns values with the given key(s). To use
         multiple keys separate them with |. E.g. ```name|amount```. Allowed
         values: ```name```, ```amount```. Default: ```name```
>    - **sort** \- Returned query is sorted by this value. Allowed
      values: ```amount```, ```name```. Default: ```None```
>    - **reverse** \- If sort is given the order of the returned
      query is determined by this value. Allowed values: ```False```, ```True```. Default: ```False```

#### /api/names/count
> - ***required*** parameters:
>   - **name** \- Returns the number of people with given name. Using
>     ```*``` returns the sum of all people. Default: ```*```