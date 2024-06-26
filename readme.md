
# Moive Rating

This is a movie api provider app. where uses can logi, register,add movie,see all movie detals and provie rating.


## API Home Page

![App Screenshot](https://i.ibb.co/Wfm4yx2/Capture.png)

## Environment Variables

To run this project, you will need to create a virtual environment and add the following environment variables to your .env file

```
SECRET_KEY=
DEBUG=True

#database

NAME=
USER=
PASSWORD=
HOST=
PORT=

```


## Features

- Sign In & Sign Up Methods
- Create Account per users
- Add Movies
- Add Rating
- Search movies

## Used Technologies
#### ⏪ Backend
- Python 
- Django
- Django Rest Framework
- Djoser
- Simple JWT
- MySQL

#### ⏩ Frontend 
- Javascript 
- React
- React Router Dom
- Tailwind CSS
- Shadcn



## 🔗 Links
- [Frontend Live Link](https://movie-rating-djreact.netlify.app/)
- [API Live Link](https://movierating.pythonanywhere.com/)
- [Frontend Code Link](https://github.com/foysalmia/Movie-Rating)
- [Backend Code Link](https://github.com/foysalmia/Movie-Rating-Backend)





## API yaml file 
```
openapi: 3.0.3
info:
  title: Movie Rating
  version: 1.0.0
  description: This is a movie rating api.
paths:
  /api/movies/:
    get:
      operationId: api_movies_list
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/GetMovie'
          description: ''
    post:
      operationId: api_movies_create
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Movie'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Movie'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Movie'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Movie'
          description: ''
  /api/movies/{id}/:
    get:
      operationId: api_movies_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this movie.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMovie'
          description: ''
    put:
      operationId: api_movies_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this movie.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Movie'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Movie'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Movie'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Movie'
          description: ''
    patch:
      operationId: api_movies_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this movie.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedMovie'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedMovie'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedMovie'
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Movie'
          description: ''
    delete:
      operationId: api_movies_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this movie.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /api/ratings/:
    get:
      operationId: api_ratings_list
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Rating'
          description: ''
    post:
      operationId: api_ratings_create
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Rating'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Rating'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Rating'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Rating'
          description: ''
  /api/ratings/{id}/:
    get:
      operationId: api_ratings_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this rating.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Rating'
          description: ''
    put:
      operationId: api_ratings_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this rating.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Rating'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Rating'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Rating'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Rating'
          description: ''
    patch:
      operationId: api_ratings_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this rating.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedRating'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedRating'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedRating'
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Rating'
          description: ''
    delete:
      operationId: api_ratings_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this rating.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /auth/jwt/create/:
    post:
      operationId: auth_jwt_create_create
      description: |-
        Takes a set of user credentials and returns an access and refresh JSON web
        token pair to prove the authentication of those credentials.
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TokenObtainPair'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/TokenObtainPair'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/TokenObtainPair'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenObtainPair'
          description: ''
  /auth/jwt/refresh/:
    post:
      operationId: auth_jwt_refresh_create
      description: |-
        Takes a refresh type JSON web token and returns an access type JSON web
        token if the refresh token is valid.
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TokenRefresh'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/TokenRefresh'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/TokenRefresh'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenRefresh'
          description: ''
  /auth/jwt/verify/:
    post:
      operationId: auth_jwt_verify_create
      description: |-
        Takes a token and indicates if it is valid.  This view provides no
        information about a token's fitness for a particular use.
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TokenVerify'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/TokenVerify'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/TokenVerify'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenVerify'
          description: ''
  /auth/users/:
    get:
      operationId: auth_users_list
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
          description: ''
    post:
      operationId: auth_users_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserCreate'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/UserCreate'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UserCreate'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserCreate'
          description: ''
  /auth/users/{id}/:
    get:
      operationId: auth_users_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this user.
        required: true
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    put:
      operationId: auth_users_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this user.
        required: true
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/User'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/User'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    patch:
      operationId: auth_users_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this user.
        required: true
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedUser'
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    delete:
      operationId: auth_users_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this user.
        required: true
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '204':
          description: No response body
  /auth/users/activation/:
    post:
      operationId: auth_users_activation_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Activation'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Activation'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Activation'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Activation'
          description: ''
  /auth/users/me/:
    get:
      operationId: auth_users_me_retrieve
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    put:
      operationId: auth_users_me_update
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/User'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/User'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    patch:
      operationId: auth_users_me_partial_update
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedUser'
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    delete:
      operationId: auth_users_me_destroy
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '204':
          description: No response body
  /auth/users/resend_activation/:
    post:
      operationId: auth_users_resend_activation_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailReset'
          description: ''
  /auth/users/reset_email/:
    post:
      operationId: auth_users_reset_email_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailReset'
          description: ''
  /auth/users/reset_email_confirm/:
    post:
      operationId: auth_users_reset_email_confirm_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UsernameResetConfirm'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/UsernameResetConfirm'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UsernameResetConfirm'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsernameResetConfirm'
          description: ''
  /auth/users/reset_password/:
    post:
      operationId: auth_users_reset_password_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailReset'
          description: ''
  /auth/users/reset_password_confirm/:
    post:
      operationId: auth_users_reset_password_confirm_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PasswordResetConfirm'
          description: ''
  /auth/users/set_email/:
    post:
      operationId: auth_users_set_email_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetUsername'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SetUsername'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SetUsername'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SetUsername'
          description: ''
  /auth/users/set_password/:
    post:
      operationId: auth_users_set_password_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetPassword'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SetPassword'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SetPassword'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SetPassword'
          description: ''
components:
  schemas:
    Activation:
      type: object
      properties:
        uid:
          type: string
        token:
          type: string
      required:
      - token
      - uid
    GetMovie:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        genre:
          type: string
          maxLength: 255
        rating:
          type: string
          maxLength: 50
        release_date:
          type: string
          format: date
        avg_rating:
          type: string
          readOnly: true
        total_rating:
          type: string
          readOnly: true
      required:
      - avg_rating
      - genre
      - id
      - name
      - rating
      - release_date
      - total_rating
    Movie:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        genre:
          type: string
          maxLength: 255
        rating:
          type: string
          maxLength: 50
        release_date:
          type: string
          format: date
      required:
      - genre
      - id
      - name
      - rating
      - release_date
    PasswordResetConfirm:
      type: object
      properties:
        uid:
          type: string
        token:
          type: string
        new_password:
          type: string
      required:
      - new_password
      - token
      - uid
    PatchedMovie:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        genre:
          type: string
          maxLength: 255
        rating:
          type: string
          maxLength: 50
        release_date:
          type: string
          format: date
    PatchedRating:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        user_id:
          type: integer
        movie_id:
          type: integer
        rating:
          type: number
          format: double
          maximum: 5
          minimum: 1
    PatchedUser:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        phone:
          type: string
          maxLength: 15
        email:
          type: string
          format: email
          readOnly: true
    Rating:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        user_id:
          type: integer
        movie_id:
          type: integer
        rating:
          type: number
          format: double
          maximum: 5
          minimum: 1
      required:
      - id
      - movie_id
      - rating
      - user_id
    SendEmailReset:
      type: object
      properties:
        email:
          type: string
          format: email
      required:
      - email
    SetPassword:
      type: object
      properties:
        new_password:
          type: string
        current_password:
          type: string
      required:
      - current_password
      - new_password
    SetUsername:
      type: object
      properties:
        current_password:
          type: string
        new_email:
          type: string
          format: email
          title: Email
          maxLength: 254
      required:
      - current_password
      - new_email
    TokenObtainPair:
      type: object
      properties:
        email:
          type: string
          writeOnly: true
        password:
          type: string
          writeOnly: true
        access:
          type: string
          readOnly: true
        refresh:
          type: string
          readOnly: true
      required:
      - access
      - email
      - password
      - refresh
    TokenRefresh:
      type: object
      properties:
        access:
          type: string
          readOnly: true
        refresh:
          type: string
          writeOnly: true
      required:
      - access
      - refresh
    TokenVerify:
      type: object
      properties:
        token:
          type: string
          writeOnly: true
      required:
      - token
    User:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        phone:
          type: string
          maxLength: 15
        email:
          type: string
          format: email
          readOnly: true
      required:
      - email
      - id
      - name
      - phone
    UserCreate:
      type: object
      properties:
        name:
          type: string
          maxLength: 255
        phone:
          type: string
          maxLength: 15
        email:
          type: string
          format: email
          maxLength: 254
        password:
          type: string
          writeOnly: true
      required:
      - email
      - name
      - password
      - phone
    UsernameResetConfirm:
      type: object
      properties:
        new_email:
          type: string
          format: email
          title: Email
          maxLength: 254
      required:
      - new_email
  securitySchemes:
    jwtAuth:
      type: apiKey
      in: header
      name: Authorization
      description: Token-based authentication with required prefix "JWT"


```

## 🚀 About Me
I'm a React & Django based full stack developer.


![Myself](https://i.ibb.co/6Pwpfz0/myimge.jpg)

