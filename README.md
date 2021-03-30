# CRAFTSTORE

The project is a database-driven Ecommerce shop for indiginous Ghanaian Hand made crafts. The ecommerce shop was written in python
with the aide of the Django framework. The project utilises SQL/SQL3 as database.

The project allows a user to view a collection of hand-made crafts under various categories, whiles reviewing their prices 
and moving desired items to the basket for payment.

## Demo 
<hr>
Find a live version <a href=""http://ami.responsivedesign.is/?url=https:///gh-recipes.herokuapp.com/"">here</a>

![]()


## UX Design

My design was inspired by [the site builder report website](https://www.sitebuilderreport.com/inspiration/food-websites), 
which is basically a collection of website design. The design is intended to display a few handcrafted artifacts on the homepage
to attract a users attention and at the same time inviting their curiosity to explore the site further by way of viewing 
other crafts instore.
Upon the completion of all functionalities, Users of the website should be able to set up accounts, read about the various crafts they see, 
select the individual products as well as move them into the basket where they could be paid for. Users should also be able to remove 
products from the basket if they are no longer interested in the craft.

The home page displays the navigation bar with the brand of GH-RECIPES on the left of the page
and four navigational icons on the right of the page. Immediately below that is a display imge of 
a ghanaian dish which a welcome inscription to the user. This is followed by a display of recipes in 
the body and finally a footer displaying the developer involved in the project

The recipe page displays a list of recipes for which upon full completion of the project users 
will be fully able to create, Read, Update and Delete recipes as they wish.

The Login navigational icon allows regualar users to get back into their profile 
to fully access their previous activities on the page as well as create new ones.

The sign up icon permits new users to establish a profile on the page.

To return to the home-page a user simply clicks the Logo which is a common convention in programming,
I also added a home button alongside the logo to make this clearer. The back to the top button at 
the bottom right of the home page allows users to navigate easily by way of a click to the navigation bar.

## Features

### home

the home feature is intended to be a showcase of recipes visitors to the site will be able to to 
click on and read about. It also offers users links to other functionalities of the site

### Recipe

It is intended that users read, add and make changes to recipes on display using this icon. it offers a 
link to the data store.

### Log in

previous users of the website can assess their previous activities by loging in. Thereupon they can 
proceed to contribute to the data in store.

#### Add Recipe

Upon a successful log in, users can proceed to acess the Add Recipe functionality of the page by clicking 
and keying in information they require.

### Signup

For new users of the site, the signup icon offers them the ability to sign up and offer their contribution 
to the recipe store available.

#### Edit Recipe

A user is able to make edits to recipes found on the website. MongoDB allocates
each entry into a collection with an object ID and this is what is used to 
locate the individual recipe the user wants to edit and pre-fill the form
for the user. After the user has made the necessary changes they submit the form
and MongoDB's update() method to update the recipe.

## Technologies Used

- Python 3.8.8
- Django 3.1.7
- BootStrap 3
- Coverage 5.5
- JavaScript
- CSS
- HTML
- 

## Testing

#### Testing Add Recipe Form

- Test that a new added recipe immediately appears on the website's homepage
- Go to form and try to submit empty fields and make sure WTForms 
InputRequired() is working
- Try to submit an empty ingredients list and make sure in-line validation is
working
- Try to submit a value in the Image URL field that is not a valid URL to make
sure the custom JavaScript validator is working
- Ensure that the random number JS function for upvotes is being created when 
adding new recipe.
- Making sure that the select fields are being populated with all of the 
correct choices
- Ensure that the removal of newly created rows for ingredients/preparation
steps is possible and make sure that all of the rows are unable to be deleted
with feedback for user if they try.

#### Testing Edit Recipe Form

- Make sure that the form is being populated with the correct data from the
MongoDB document when editing recipe.
- Ensure that adding/removing ingredient/preparation step rows is not causing
an issue with clashing names when submitted
- Ensure a recipe is able to be updated more than once without any bugs
occuring (such as fields going missing or name clashes causing issues)
- Test that the select fields are producing the correct options.

## Database Schema

The database is structured with 5 collections, recipes  The two
collections are related as recipes contains a 'cuisine name' key that
corresponds the cuisine documents.

The recipes document itself contains unstuctured data. With key/value pairs
that make up a description of the recipe. The ingredient name, quantity and
value all have the same number within the key, and they are grouped through the
use of sorting by number and sliced for data representation.

An example of a recipe document can be found in static/images/doc_example.png


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
1. Im grateful to my Seun Owonikonkon for her time.
