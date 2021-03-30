# CRAFTSTORE
## Full Stack Framework with Django

![Mockup]()



The project is a Database-driven Ecommerce shop for indiginous Ghanaian Hand made crafts.
The project allows a user to view a collection of hand-made crafts under various categories, whiles reviewing their prices 
and moving desired items to the basket where payment can be made.

<hr>
Find a live version <a href="http://ami.responsivedesign.is/?url=https:///gh-recipes.herokuapp.com/">here</a>


## UX Design

My design was inspired by the youtube channel called <a href="https://www.youtube.com/c/veryacademy/videos">Very Academy</a>, 
which basically teaches programming to their subscribers. The design is intended to display a few handcrafted artifacts on the homepage
to attract a users attention and at the same time inviting their curiosity to explore the site further by way of viewing 
other crafts instore.
Upon the completion of all functionalities, Users of the website should be able to set up accounts, read about the various crafts they see, 
select the individual products as well as move them into the basket where they could be paid for. Users should also be able to remove 
products from the basket if they are no longer interested in the craft.

##Scope
A MVP (minimum viable product) includes:

- landing page displaying a few crafts
- A library button acting as a dropdown menu for various categoris of crafts
- A basket button 
- A section giving an overview of crafts available on the site

### User stories

**ID** | **As a/an** | **I want to be able to...** | **So that I can**
--- | --- | --- | ---
1 | Site User | Register to the site | Log in to my account 
2 | Site User | Log In and Log Out | View my profile
3 | Site User | Receive email confirmation | Confirm successful registration
4 | Site User | Have a user profile | View my purchases, and be able to check my order history
5 | Potential customer | View some crafts | Select to purchase
6 | Potential customer | View details of the craft | See price and description
7 | Potential customer | Pay for the craft i like | Buy
8 | Customer | View craft in my bag | Check the cost to review
9 | Customer | Enter payment information and see that process is secure | Checkout without issues
11 | Administrator | Add new catergory of crafts | To make them visible to customer
12 | Administrator | Edit or update various categories | To change a pric and/or description 
13 | Administrator | Delete a category of craft | To remove from a site

## Features

### home

the home feature is intended to be a showcase of recipes visitors to the site will be able to to 
click on and read about. It also offers users links to other functionalities of the site

### Library

The library icon when clicked on exposes the Category of crafts available on the site

### Basket

The basket button on the right side of the navigation bar is meant to hold a list of items 
that have been reviewed by the site user awaiting payment.

### Wireframes

- Home Page

    <details><summary>Desktop (click to view)</summary>

    ![](<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2F9eOMIaCWLS6u7WBXtREDNX%2Fcraftstore%3Fnode-id%3D1%253A27" allowfullscreen></iframe>)
    </details>
    <details><summary>Alternatively (click to view)</summary>
    
    ![](static/images/Wireframe.png)
    </details>
## Technologies Used

- Python 3.8.8
- Django 3.1.7
- BootStrap 3
- Coverage 5.5
- JavaScript
- CSS
- HTML
- figma for wireframing

## Database Schema

Database contains 3 table:
- user
- categories
- products

I use Django default databases SQLite in gitpod environment and PostgreSQL database with Heroku as production enviroment.

<details><summary>Database schema (click to view)</summary>

![](static/images/database.png)

</details>

<details><summary>User table: (click to view)</summary>

| UserName | Email Address | First Name| Last Name |
:-------------:|:----------------:---------:-------:

</details>

<details><summary>User table for packages app: (click to view)</summary>

- #### Category:

<details><summary> Categories table: (click to view)</summary>

| Name | Slug | 
:------:|:--------:
Fibrics| fibrics
Woodworks | woodwork
beads | beads

</details>

### Security

All sensitive access keys are stored as `Config Vars` on Heroku cloud application platform.
Django allauth was used to meet security requirements.

## Deployment
This project was built using Python 3.8.6 and Flask 1.1.2.
1. The project was deployed to Heroku with config vars:
1. created requirements.txt that Heroku knows which packages are required for the application to run and install them.
1. created Procfile that Heroku knows what kind of application this is.
1. project eventually deployed at 
<a href="https://gh-recipes.herokuapp.com/">here</a>">

#### Challenges 
The developer was constrained by time in studying and executing all the desired functionalities for the project within an 
expected time frame. He however hopes to bring the project to completion in due course.

### project inspiration: 

1. inspiration for this project were largely drawn from tutorials on the Youtube channel of Very Academy.
1. Git ignore file was adopted from www.toptal.com/developers/gitignore/api
1. Appreciation goes to the code institute student support team for being very supportive throughout my period
   study with the code institute
1. Im grateful to my mentor Seun Owonikoko for her time.
