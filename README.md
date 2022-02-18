<h1>Zolsha Online Ordering</h1>

<img src=""><br>
<h4><a href="" target="_blank">GitHub Link</a></h4>
<h4><a href="" target="_blank">Deployed Project</a></h4><br>
<p></p> 
<h2>Table of Contents</h2>
<ol>
<li><a href="#ux">UX</a></li>
<ul>
<li><a href="#wireframes">Wireframes</a></li>
<li><a href="#target-audience">Target Audience</a></li>
<li><a href="#user-stories">User Stories</a></li>
<li><a href="#design">Design</a></li>
<ul>
<li><a href="defensive-design">Defensive Design</a></li>
<li><a href="typography">Typography</a></li>
</ul>
</ul>
<li><a href="#database">Database</a></li>
<li><a href="#features">Features</a></li>
<ul>
<li><a href="#existing-features">Existing Features</a></li>
<li><a href="#new-features">Features left to implement</a></li>
</ul>
<li><a href="#technologies">Technologies Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#credits">Credits</a></li>
</ol>

<h1 id="ux"><u>UX</u></h1>
This websites primary purpose is to allow Zolsha Restaurant & Takeaway's customers to order their favourite dishes from the comfort of their own homes and to have the food either delivered or to allow them to collect the food once it is ready. The functionality is as such that the customers can provide all the relevant details to allow for the food to be delivered and make a secure payment for the order. A website search function will provide any users the ability to search for menu items by a keyword to save them time if they know what they would like to purchase. The ordering system will be available for any visitors to the site however delivery will only be available for customers within a certain distance from the restaurant. Additional functionality will be made available for user's that register on the site such as a profile that stores all previous orders and delivery information to save time for regular customers when ordering.
The website will also have a secondary purpose which is to allow customers to make table reservations for dining in at the restaurant. The user can check availability and if a table is available a booking can be made. Again, a registered user will have the additional functionality to view all of their table reservations in their profile.
The third and final purpose of this website will be to allow the restaurant ovwners and employees to keep up to date with orders and reservations for that day by providing them with a dashboard showing these in a easy to read format. It will also allow them to keep their menu up to date by offering them the opportunity to add new dishes to the menu.
<br>

<h2 id="wireframes">Wireframes</h2>
Please see the wireframes for this project:<br>
<a href="media/readme/desktop-wireframe.png" target="_blank">Desktop</a><br>
<a href="media/readme/mobile-wireframe.png" target="_blank">Mobile</a><br>

<h2 id="target-audience">Target Audience</h2>
<ul>
<li>The target audience for this website has a relatively narrow scope. As this is primarily a tool for ordering a food delivery, the target audience will live within a small geographical area surrrounding the restaurant. As delivery is limited to a number of postcodes and customer will not be willing to travel too far to visit the restaurant, I have estimated that the target audience will be based within 7 miles of the restaurant.</li>
<li>The demographic for the consumer audience will be Indian food lovers, aged over 16. </li>
<li>There will also be a secondary audience which is the restaurant owner/employees to allow them to keep up to date with orders and bookings the restaurant has recieved. </li>
</ul><br>

<h2 id="user-stories">User Stories</h2>
As a user of the website, the following actions and results would need to be achieved:
<ul>
<li>Unregistered User</li>
<strong>As an unregistered user, I would like to be able to:</strong>
<ol>

<li>Browse the menu items and filter by categories.</li>
<li>Add items to my shopping bag.</li>
<li>Search for a specific dish or ingredient without having to browse through all menu items.</li>
<li>See a summary of the items in my shopping bag and an order total each time I add a new item without having to visit the shopping bag each time.</li>
<li>Calculate the delivery fee by providing my postcode. </li>
<li>Review my shopping bag details before completing the checkout process and make any amendments should they be required. </li>
<li>Provide delivery & contact details before providing payment for my order.</li>
<li>View a confirmation of the items I have ordered & the order number.</li>
<li>Have the option to register for an account by providing an email and creating a password & username.</li>
<li>Check availability for a table in the restaurant on a given date and make a dining reservation. </li>
</ol>
<li>Registered User</li>
<strong>As a registered user, I would like to be able to do all of the above actions (for an unregsitered user) and:</strong>
<ol>
<li>Save my delivery details to my profile which will then be automatically entered at the checkout.</li>
<li>View my previous order details including the items ordered in my profile </li>
<li>Reorder previous orders directly from the order history without having to search through the menu to find each item.</li>
<li>View any table reservations I have made including the reservation details, such as the date & time, in my profile</li>
<li>Have the ability to cancel any table reservations I have made directly from my profile without having to contact the restaurant directly. </li>
</ol>
<li>Admin/Super User</li>
<strong>As the admin/super user, I would like to be able to:</strong>
<ol>
<li>Add new dishes/items to the menu. </li>
<li>View all of the current days orders including the postcode and price.</li>
<li>View all of the current days table reservations in details with the time and number of people shown.</li>
</ol>
</ul><br>

<h2 id="design"><u>Design</u></h2>
I have kept the design of the webpages simple and easy to navigate.
<ul><li>All of the headings are the same size, colour & font and the colour scheme is the same throughout.</li>
<li>Also all of the buttons have the same colour schemes and sizes.</li>
<li></li>
<li></li>
</ul>

<h2 id="defensive-design">Defensive Design</h2>
<p></p>
<ul>
<li></li>
<li></li>
<li></li>
<li> </li>
<li></li>
</ul>

<h2 id="typography">Typography</h2>
<p>2 Google Fonts were used in this project:</p>
<ol>
<li></li>
<li> </li>
</ol><br>

<h1 id="database"><u>Database</u></h1>
For this website, there will be a schema of interconnecting models. The tables below show the items in each of the models and the Foreign keys connecting them to each other.<br>

<h3><u>Users</u></h3>
<p>This model was installed with the help of Django AllAuth to allow users to register and then sign in to their accounts. </p>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|username| Username decided by user| Varchar/Integer |
|password| Password chosen by user that has been hashed| Varchar/Integer |
|first name| Users first name | Varchar |
|last name| Users last name | Varchar |
|email address | Users email address | Email |
|date joined | The date the user registered | Date/Time |

<br>
<h3><u>Menu App</u></h3><br>
<h4><u>Category</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|name| category name| Text |
|friendly name| An easier to understand name that can be displayed to users| Text |

<br>
<h4><u>Subcategory</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|name| subcategory name| Text |
|friendly_name| An easier to understand name that can be displayed to users| Text |
|category| Foreign Key to link each subcategory to the relevant category | Foreign Key |

<br>
<h4><u>Menu</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|sku| Unique combination of letters and numbers to each menu item | Varchar |
|name| The name of the menu item | Text |
|description| A description of the menu item  | Text |
|price| Price of each item to 2 decimal places  | Numbers - float 2 |
|has_options| Whether the item has different options able to be selected | Boolean |
|category| Foreign Key to link each menu item to the relevant category | Foreign Key |
|subcategory| Foreign Key to link each menu item to the relevant subcategory | Foreign Key |

<br>
<h3><u>Bag App</u></h3><br>
<h4><u>Delivery Charges</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|area| The postcode prefix for each area| Varchar (max 4) |
|charge| The cost of delivery to the area | Number - float 2 |


<br>
<h3><u>Checkout App</u></h3><br>
<h4><u>Order</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|order_number| Unique order number for each order | Varchar (max 32) |
|user_profile| Foreign Key to link order to user profile | Foreign Key |
|full_name | Customers full name | Text |
|email | Customers email | Email |
|phone_number | Customers phone number  | Number |
|postcode | Customers delivery postcode  | Varchar (7) |
|town_or_city | Customers delivery town  | Text |
|street_address1 | Customers delivery address line 1  | Varchar |
|street_address2 | Customers delivery address line 2  | Varchar |
|order_date | Order date for this order  | Date/Time |
|order_time | Order time for this order  | Date/Time |
|delivery_details | Any additional information provided by customer for delivery driver  | Text |
|delivery_cost | Price of delivery  | Decimal - float 2 |
|order_total | Price of all ordered items  | Decimal - float 2 |
|grand_total | Price of all ordered items plus delivery charge  | Decimal - float 2 |
|original_bag | Summary of the shoppping bag  | Text |
|stripe_pid | Stripe Payment ID  | Varchar |
<br>

<h4><u>Order Line Item</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|order | Foreign Key to link the order line items to a specific order | Foreign Key |
|item | Foreign Key to link this line item to the related item in the Menu model | Foreign Key |
|item_option | If the item has options, the option selected will be stored | Text |
|quantity | The quantity of the item that was in the shopping bag | Integer |
|lineitem_total | The item price multiplied by the quantity | Decimal - float 2 |

<br>
<h4><u>Offer</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|offer_code | Offer code that customers can be given to gain a discount | Varchar |
|discount | Percentage discount provided by the offer code | Number |

<br>
<h3><u>Reservations App</u></h3><br>
<h4><u>Reservation</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|_id | Id (automatically generated to be unique & sequential)| ID |
|res_number | Randomly generated reservation number unique to each booking | Varchar |
|date | Reservation date | Date/Time |
|time | Reservation time | Date/Time |
|covers | Number of Guests | Number |
|full_name | Name of lead guest | Text |
|email | Email address for lead guest | Email |
|phone_number | Phone number for lead guest | Number |
|user_profile | Links reservation to User's profile if registered | Foreign Key |
<br>

<h3><u>Profiles App</u></h3><br>
<h4><u>User Profile</u></h4>

| Key                | Value          |  Data Type       |
|--------------------|----------------|------------------|
|user | User that was created by Django AllAuth | Foreign Key |
|defualt_name| Preferred name for user | Text |
|default_phone_number| Preferred phone number | Number |
|default_street_address1| Delivery address line 1 | Varchar |
|default_street_address2| Delivery address line 2 | Varchar |
|default_town_or_city | Delivery town or city | Text |
|default_postcode | Delivery postcode | Varchar |

<br>
<h3>Database Design</h3>
See below a diagram for the flow of data through the different database models in this project.<br>
<img src="media/readme/database-schema.jpeg">


<h2 id="existing-features"><u>Existing Features</u></h2>
<ol>
<li>NAVIGATION</li>
<li>VIEW MENU ITEMS</li>
<li>SEARCH MENU ITEMS</li>
<li>FILTER MENU ITEMS BY CATEGORY/SUBCATEGORY</li>
<li>ADD ITEMS TO SHOPPING BASKET</li>
<li>CALCULATE DELIVERY CHARGE</li>
<li>EDIT & REMOVE ITEMS IN SHOPPING BASKET</li>
<li>ADD PROMOTIONAL CODES TO GAIN DISCOUNT</li>
<li>SECURE CHECKOUT</li>
<li>REGISTRATION</li>
<li>LOGIN</li>
<li>LOGOUT</li>
<li>USER PROFILE</li>
<li>CHECK DINING AVAILABILITY</li>
<li>COMPLETE DINING RESERVATION</li>
<li>CANCEL DINING RESERVATION</li>
<li>RESTAURANT DASHBOARD</li>
</ol>
<br>
<h2 id="new-features"><u>Features Left to Implement</u></h2>

<ol>
<li>Automatically delete and remove past date dining reservations from the database and therefore from the user profile as well.</li>
<li>Create an 'address book' of the restaurants customers who have previously ordered or booked a table and only give access to the admin user.</li>
<li>Add additional functionality to the Restaurant Dashboard to allow the restaurant owner to contact customers by email directly from the dashboard.</li>
<li>Add an additional view to the user profile to allow the user to amend their dining reservation directly from their profile.</li>
</ol>


<h1 id="technologies"><u>Technologies Used</u></h1>

<h3>Languages Used</h3>
<ul>
<li>HTML5</li>
<li>CSS3 </li>
<li>JavaScript</li>
<li>Python3</li>
</ul>
<h3>Libraries Used</h3>
<ul>
<li>JQuery</li>
<li><a href=" target="_blank">Bootstrap</a> - Used to provide page structure, Navbar design and form components. Also used to provide generic styling. </li>
<li><a href="https://fontawesome.com/" target="_blank">Font Awesome</a>  - Icons for forms and styling.</li>
<li><a href="https://fonts.google.com/" target="_blank">Google Fonts</a> - Used to create a look in keeping with the website aim and to create uniform styling throughout.</li>
</ul>
<h3>Python Frameworks & Libraries</h3>
<ul>
<li>Django</li>
<ul>
<li>AllAuth</li>
</ul>
<li></li>
<li></li>
<li></li>
</ul>
<h3>Database & Deployment</h3>
<ul>
<li></li>
<li>Git</li>
<li>GitHub</li>
<li>Heroku</li>
</ul>

</ul>

<h1 id="testing"><u>Testing</u></h1>
<h4>Validators</h4>
<ul>
<li>W3C HTML Validator</li>
All pages of HTML content have been checked by the HTML validator and have passed.
<li>W3C CSS Validator</li>
<img src="">
<li>PEP8 Compliant</li>
<img src="">
</ul>

<h4>Manual Testing</h4>
I have carried out a lot of manual testing on different aspects of this project. Please see detailed manual testing logs <a href="testing.md"> here </a>.
Please see below a brief overview of the testing carried out. Any issues found and fixes put in place are documented in the testing log.

| Page                  | Bug Detected   | Bug fixed Y/N |
|---------------------- |----------------| --------------|
| Home Page (user)    | No issues found| 
| Home Page (user logged in)  | No issues found| 
| Register Page (user)  | No issues found| 
| Log In Page (user)  | No issues found| 
| Log In Page (admin user)  | No issues found |
| Menu (user)  | ISSUE FOUND | Y
| Shopping Bag (user) | ISSUE FOUND    | Y
| Checkout Page (user) | ISSUE FOUND     | Y
| Checkout Page (user logged in) | ISSUE FOUND     | Y
| Order Success (user) | No issues found     | 
| Check Dining Availability (user) | No issues found     | 
| Make Dining Reservation (user) |ISSUE FOUND   | Y (but further improvements could be made)
| Make Dining Reservation (user logged in) | ISSUE FOUND  | Y (but further improvements could be made)
| User Profile | No issues found     | 
| Reorder previous orders (user logged in) | No issues found     | 
| Cancel Dining Reservation | No issues found    |
| Restaurant Dashboard (admin user) | No issues found    |
| Add New Recipe (admin user) | No issues found    | 

<h1 id="deployment"><u>Deployment</u></h1>
This project has been deployed via Heroku and can be accessed <a href="" target="_blank">here</a> .<br>

If you would like to deploy this project for yourself please see below the steps I followed to deploy and you can do the same:
<ol>
<li>
Create your new repository (I used GitHub) and then download or clone the following link: <a href = "">
</li>

This site is currently deployed on Heroku using the master branch on GitHub. You can deploy this project remotely using the following steps:
<h3>Deploying with Heroku</h3>
<ol>
<li>Firstly you need to create a requirements.txt file. This is used by Heroku to install all the required dependancies that are needed to run the application. To create the requirements.txt file you will need to enter the following into the terminal:

pip3 freeze --local > requirements.txt
You can view the requirements.txt file for this project here to ensure all of the requirements are present in your own file.</li>
<li>Secondly, Heroku requires a Procfile which tells it what type of application is being deployed and how it should run it. To add the Procfile you will need to enter the below into the terminal:

echo web: python run.py > Procfile

(Please make note that the 'P' in Procfile should be capitalized)


You can view the Procfile for my project here: Procfile</li>

<li>You will then need to sign up for a free Heroku account or, if you already have one, you will need to sign in. The link to create your account is: https://signup.heroku.com/ </li>

<li>Once signed in to your Heroku account, you will need to create a new app ensuring you select the region closest to your location.</li>

<li>You then need to choose your deployment method in the Deploy section. If you have created your repository using GitHub, you can connect to the specific repository by searching for the repo-name. If you cannot connect via GitHub, you can connect using Heroku Git (follow the instructions provided on Heroku).</li>

<li>Once connected, you can 'Enable Automatice Deploys' so if you make any further changes and commits, it will automatically update and deploy a new version of the application.</li>

<li>In Heroku click on the 'Settings' tab. In the Config Vars section, click on 'Reveal Config Vars' which is used to configure the environmental variables. You will need to set up your env.py file in order to complete this section. Setting up your env.py file can be done as follows:
<ul>
<li>Create a new file outside the folder structure called env.py.</li>
<li>You will need to type 'import os' at the top of this file.</li>
<li>Then the environment variables need adding as below:<br>
os.environ.setdefault("IP", "0.0.0.0")<br>
os.environ.setdefault("PORT", "5000")<br>
os.environ.setdefault("SECRET_KEY", "insert your secret key here")<br>
os.environ.setdefault("MONGO_URI", "insert your connection string here")<br>
os.environ.setdefault("MONGO_DBNAME", "insert you database name here")<br>
The SECRET_KET can be anything you choose.<br>
The MONGO_URI connection string can be found by doing the following in MongoDB:
<ul>
<li>Click on the 'Overview' tab</li>
<li>Click on the 'Connect' option</li>
<li>Select the 'Connect your application' option</li>
<li>Select 'Python' as the driver</li>
<li>You will then be provided with a connection string</li>
<li>Paste the connection string into MONGO_URI variable</li>
<li>Ensure you update the sections in capital letters with your own information e.g your password, your cluster name and your collection name: mongodb+srv://myRoot:MONGODB-PASSWORD@CLUSTER-NAME-96wib.mongodb.net/DATABASE-NAME?retryWrites=true&w=majority".</li></ul></li>
</ul>
</li>
<li>Once your env.py file is created, go back to the Config Vars in Heroku and add the IP, PORT, SECRET_KEY, MONGO_URI & MONGO_DBNAME with the correct values as per your env.py file.</li>
<li>Finally, go back to the 'Deploy' tab on Heroku and in the Manual Deploy section chose the 'main' branch and click 'Deploy Branch'. Once the application has been built, you will receive a message stating 'Your app was successfully deployed' with a link to view the app.</li>
</ol>
</li>

<h1 id="#credits">Credits</h1>

<h3>Design</h3>
<ul>
<li>The following elements and components have been taken from Bootstrap including the Jquery (when required) to operate them successfully:</li>
<ul>
<li>Navbar & Side Navbar</li>
<li>Card Component for all menu items, availability section & order history.</li>
<li>Toast component for messages section.</li>
<li>Date & time selectors for dining availability.</li>
</ul>
<li>Bootstrap classes have also been used for styling the components.</li>
<li>Google Fonts utilized for all font styles within the project.</li></ul>

<h3>Code</h3>
<ul>
<li><a href= target="_blank">Django Documentation</a> </li>
<li><a href="" target="_blank"></li>
<li>Tutor Support assisted with </li>
<li>Code Institute Tutorials were used for reference when creating functions.</li>
<li>Boutique Ado Mini Project.  </li>
<li><a href="" target="_blank"></a> </li>


</ul>

<h3>Media</h3>
<ul>
<li>Font Awesome used for all icons and symbols.
</li>
<li>All photograph images were provided by Zolsha Restaurant.</li>
<li>Image to show responsive design from <a href="http://ami.responsivedesign.is/#" target="_blank">http://ami.responsivedesign.is/#</a></li></ul>