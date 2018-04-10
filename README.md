# SnapCap

[SnapCap](http://) is a web app for posting pictures for people to caption. It was created for Project 4 at General Assembly, WDI-17 and is hosted on Heroku at:

SnapCap live site: https://

### Jump to...

- [Technologies Used](https://github.com/WithoutATowel/SnapCap#technologies-used)
- [Routes](https://github.com/WithoutATowel/SnapCap#routes)
- [Models](https://github.com/WithoutATowel/SnapCap#models)
- [APIs Used](https://github.com/WithoutATowel/SnapCap#apis-used)
- [User Stories](https://github.com/WithoutATowel/SnapCap#user-stories)
- [About the project](https://github.com/WithoutATowel/SnapCap#about-the-project)
- [Wireframes](https://github.com/WithoutATowel/SnapCap#wireframes)
- [Next Steps](https://github.com/WithoutATowel/SnapCap#next-steps)

<!-- SnapCap Homepage
![SnapCap homepage](/readme-images/finished_homepage.png) -->

---
## Technologies Used
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)

- HTML5 / CSS3
- JavaScript
- Materialize?
- Python
- Django
- Vue.js


## Routes
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)

| CRUD   | ROUTE                  | FUNCTIONALITY
|--------|------------------------|-------------------------
| GET    | /	home/all            | home/all
| GET    | /snaps/:id             |	Details
| GET    | /snaps/friends         |	friends
| GET    | /snaps/:category       |	categories
| POST   | /snaps                 |	Post (modal)
| GET    | /snaps?={searchterms}  |	Search
| PUT    | /snaps/:id/vote        |	Snap Vote
| POST   | /signup                |	Sign Up (modal)
| POST   | /login                 |	Login (modal)
| GET    | /logout                |	Logout
| GET    | /profile/:id           |	Profile
| PUT    | /profile/:id           |	EditProfile (form)
| DELETE | /profile/:id           |	Delete Profile (form)
| PUT    | /caps/:id/:card        |	Cap Vote



## Models
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)

#### User
| id | name | username | password | email | picture_points | caption_points | profile_img | picture_votes | caption_points
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
| integer | string | string | string | email | integer | integer | string | integer | integer

#### Pictures
| id | user_id | votes | cloudinary_url | category
| --- | --- | --- | --- | ---
| integer | integer | integer | string | string

#### Usertext
| id | text | user_id | votes | picture_id
| --- | --- | --- | --- | ---
| integer | string | integer | integer | integer

#### Friendship
| id | user_id | friend_id | status
| --- | --- | --- | ---
| integer | integer | integer | string?

#### Cards
| id | text
| --- | ---
| integer | string

#### Users_Cards
| id | user_id | card_id
| --- |  --- | ---
| integer | integer | integer

#### Pictures_Cards
| id | picture_id | card_id | user_id | votes
| --- | --- | --- | --- | ---
| integer | integer | integer | integer | integer


## APIs Used
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)
- [Avatar API](https://www.avatarapi.com)

## User Stories
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)

1.
2.
3.

## About the project
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)

DESCRIPTION HERE

## Wireframes
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)

<!-- ![Landing page wireframe](readme-images/1.jpg) -->



## Next Steps
[to the top](https://github.com/WithoutATowel/SnapCap#snapcap)











<!-- # snapcap

> A Django - Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run all tests
npm test

# deploy
.deploy.sh
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader). -->
