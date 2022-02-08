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
<a href="" target="_blank">Desktop</a><br>
<a href="" target="_blank">Mobile</a><br>

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

<li>Browse the menu items and add items to my shopping bag.</li>
<li>Search for a specific dish or ingredient without having to browse through all menu items.</li>
<li>See a summary of the items in my shopping bag and an order total each time I add a new item without having to visit the shopping bag each time.</li>
<li>Calculate the delivery fee by providing my postcode. </li>
<li>Review my shopping bag details before completing the checkout process and make any amendments should they be required. </li>
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
For this website, there will be models. The tables below show the items in each of the models and the Foreign keys connecting them to each other.<br>

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


<h2 id="existing-features"><u>Existing Features</u></h2>
<ol>
<li>NAVIGATION</li>
<li>VIEW MENU ITEMS</li>
<li>SEARCH MENU ITEMS</li>
<li>FILTER MENU ITEMS BY CATEGORY</li>
<li>SHOPPING BASKET</li>
<li>SECURE CHECKOUT</li>
<li>REGISTRATION</li>
<li>LOGIN</li>
<li>LOGOUT</li>
<li>USER PROFILE</li>
<li>CHECK DINING AVAILABILITY</li>
<li>COMPLETE DINING RESERVATION</li>
<li>RESTAURANT DASHBOARD</li>
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
<li>Flask Framework</li>

<li>werkzeug.security</li>
<li>bson</li>
<li>Counter</li>
<li>Random</li>
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
| Home Page (user)    | ISSUE FOUND| Y
| Home Page (user logged in)  | No issues found| 
| Register Page (user)  | No issues found| 
| Log In Page (user)  | No issues found| 
| Menu (user)  | ISSUE FOUND| Y
| Shopping Bag (user) | No issues found     | 
| Checkout Page (user) | No issues found     | 
| Checkout Page (user logged in) | No issues found     | 
| Order Success (user) | No issues found     | 
| Check Dining Availability (user) | No issues found     | 
| Make Dining Reservation (user) | No issues found     | 
| Make Dining Reservation (user logged in) | No issues found     | 
| User Profile | No issues found     | 
| Reorder previous orders (user logged in) | No issues found     | 
| Cancel Dining Reservation | No issues found    |
| Restaurant Dashboard (admin user) | No issues found    |
| Add New Recipe (admin user) | No issues found    | 



<h1 id="#credits">Credits</h1>

<h3>Design</h3>
<ul>
<li>The following elements and components have been taken from Bootstrap including the Jquery (when required) to operate them successfully:</li>
<ul>
<li>Navbar & Side Navbar</li>
<li>Card Component for all menu items, availability section & order history.</li>
<li>Toast component for messages section.</li>
<li></li>
</ul>

<li></li>
<li>Google Fonts utilized for all font styles within the project.</li></ul>

<h3>Code</h3>
<ul>
<li><a href= target="_blank">Django Documentation</a> </li>
<li><a href="" target="_blank"></li>
<li>Tutor Support assisted with </li>
<li>Code Institute Turtorials were used for reference when creating functions.</li>
<li>Boutique Ado Mini Project.  </li>
<li><a href="" target="_blank"></a> </li>


</ul>

<h3>Media</h3>
<ul>
<li>Font Awesome used for all icons and symbols.
</li>
<li></li>
<li>Image to show responsive design from <a href="http://ami.responsivedesign.is/#" target="_blank">http://ami.responsivedesign.is/#</a></li></ul>