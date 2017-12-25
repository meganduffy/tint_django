# Type It Now Transcription

## Overview

### What is this website for?

This project was designed for a start-up transcription business, Type It Now Transcription. They specialize in professional, competitive, turn around time focused transcription for corporate, legal, medical and educational purposes. The wide variety of options and unique pricing scheme posed a wonderful challenge for setting up commerce. You can view the website created at [**typeitnow.herokuapp.com**](https://typeitnow.herokuapp.com/).

### What does it do?

This website boasts several wonderful features. There is an informative shopfront complete with FAQs, contact forms and instant price calculators to entice and persuade new customers.
There is also a membership area where, upon registering, customers can create transcription orders by uploading files and selecting the transcription options and categories that accommodate their needs. Once an order has been placed, they can avail of a "Transcript Tracker" which logs what phase of the transcription process their file is in, how long until it will be ready and what the receiving email is. Once the transcript has been sent out via email, the customer can then leave reviews on the individual order.
If the customer has files they would like transcribed but are not yet ready to place an order, they can add the order to their "Saved For Later" queue.
Both of these tools can be viewed from the Profile page where customers can also update their contact information and view their recent Forum posts.
The Forum is in place in order to link and network the companies customers.


### How does it work?

This project uses the Python Django Framework for building a server which connects multiple web applications through a robust structure. It also connects up with a mySQL database to store customer information as well as transcript files and forum posts. Using 3rd Party Javascript and Python Packages (__see **Tech Used**__), I created a esoteric commerce site that catered to the unique technical needs of a transcription company while maintaining their start up aesthetic .

## Features

### Existing Features

1. Visually effective and informative presentation layer
2. Contact/Custom Price Quote forms
3. Instant Quote Live Calculation Form
4. Membership area with customizable profiles
5. Commerce area with file upload, transcription detail and PayPal payment sections
6. Order tracking area with live ETA, as well as order summary, plus optional reviews once ETA has been passed
7. "Saved For Later" order section
8. Forum with user created threads and posts
9. User created polls
10. Mobile friendly layout
11. Testing

## Tech Used

### Some Tech Used Includes

- [Django](https://www.djangoproject.com/)
    - A Python based high-level framework, **Django** was used to serve data from to server to my web based interface.
- [MySQL](https://www.mysql.com/)
    - A database management system, **MySQL** is the most popular database tool in the world. It is a lightweight relational database used to store and connect data.
- [Django Paypal](https://django-paypal.readthedocs.io/en/stable/)
 - A python package **Django Paypal** was used to link and utilize Paypal's Standard Payments.
- [Django TinyMCE](https://pypi.python.org/pypi/django-tinymce)
 - **Django TinyMCE** is a package which contains a widget which renders a form field, used to facilitate form threads and posts, as well as reviews on the site.
- [Mutagen](https://mutagen.readthedocs.io/en/latest/)
 - A audio metadata package, **Mutagen** is used to process the audio files that are uploaded to the site for orders.
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap** is the most popular framework for developing responsive layouts.

## Web Design

- [**jQuery**](https://jquery.com/)
 - I created some interactive elements using **jQuery**, such as click-to-reveal information panels:
</br></br>
**_Interactive Information Panels_**</br>
![Interactive Information Panels](https://s3.amazonaws.com/uploads.hipchat.com/16076/5060597/XUSJeM70HZyZugA/Type_It_Now_Transcription_Services.png)


- [**JavaScript**](https://www.javascript.com/)
- I used **JavaScript** in order to pull live information from the browser and create an instant quote calculator:

**_Instant Quote Calculator_**
![Instant Quote Calculator](https://s3.amazonaws.com/uploads.hipchat.com/16076/5060597/8u3ySAUBZGwgt2f/Type_It_Now_Transcription_Services.png)

## Responsive Web Design

I used a variety of methods to ensure the responsiveness of my dashboard. These included:
- **Mobile First Design**
    - **Mobile First Design** is a fundamental part of designing for a multi screen world. I build this dashboard with mobile space, functionality and utility as first priority.

- [**Bootstrap**](http://getbootstrap.com/)
    - I used the **Bootstrap** Framework to create tried and trusted sleek, responsive elements. For example, Bootstrap makes it simple to implement a stylish collapsible navbar and responsive columns:
        </br></br>**_Uncollapsed navabr and columns in single row_**</br>
        ![Uncollapsed Navbar](https://s3.amazonaws.com/uploads.hipchat.com/16076/5060597/QzA60bzwtf7fQnd/Type_It_Now_Transcription_Services.png "Uncollapsed Navbar")
        </br></br>**_Collapsed navbar and columns seperated into multiple rows_**</br>
        ![Collapsed Navbar](https://s3.amazonaws.com/uploads.hipchat.com/16076/5060597/U8fj2YkqS6ECy4G/Type_It_Now_Transcription_Services.png "Collapsed Navbar")

- **Flexbox**
    - I used **Flexbox** display for simple yet powerful design layouts that ensure responsiveness. **Flexbox** can come in very handy when you need to devise seemingly straight-forward designs (which easily become tricky using more traditional methods) with just a few lines of code:
        </br></br>**_Three divs vertically displayed in a single row_**</br>
        ![Vertical Flex Display](https://s3.amazonaws.com/uploads.hipchat.com/16076/5060597/JNLYcNtssWwUmYd/Type_It_Now_Transcription_Services.png "Vertical Flex Display")

### Responsive Web Design Testing

I used a variety of methods to test the responsiveness of my dashboard. These included:

- [Firefox Responsive Design Mode](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode)
    - This was an essential tool to testing the responsiveness of my dashboard, **Firefox Responsive Design Mode** makes it fast and effortless to switch between screen sizes and devices.
        </br></br>**_Firefox Responsive Design Mode simulating an Apple iPhone SE_**</br>
        ![Firefox RDM](https://s3.amazonaws.com/uploads.hipchat.com/16076/5060597/G420cl98BTTacAz/Type_It_Now_Transcription_Services.png "FirefoxRDM")

- **Testing In Different Environments**
    - There is no simulator that could replace simply testing my dashboard in as many environments as possible. Using as many different browsers and devices as I could get my hands on was key to weening out design flaws. **Testing in Different Environments** was a integral part of guaranteeing my dashboard functions correctly for every User.

### Integration Tests
- Within the project I have included a few Test Suits in order to test the permissions of pages, though it has not been extensive.

### Personal Note
- I have enjoyed working on this project immensely and am very proud of the progress I made on it. It is by no means a completed site in my eyes.
- I have had a great honor of finding employment in the development industry during the completion of this project. Unfortunately, this has translated negatively to the work I am presenting to you today. Despite my employment dreams having been fulfilled, I realize that my time commitment and skill dedication has drifted from the project at hand.
