# dj-say

### What is dj-say?

dj-say is an easy to implement and fully customizable contact form designed to work with Django web applications.

### Why did I make this?

Look at any basic contact form on almost any website. They all more or less look like this:

![Contact Form](http://www.evklein.com/static/images/screenshots/dj-say/dj_say_1.png)

Needless to say, they're all pretty much the exact same format, give or take a few small components and changes. dj-say fixes this, by allowing a user to implement a simple, customizable contact form in a very short amount of time, and have it just <i>work</i>.

## Getting dj-say Set Up in Less Than 5 Minutes

### Initial download and installation

1. Download dj-say as a ZIP file and unzip into a directory.
2. Create a new Django application inside of your project using <code>python manage.py startapp contact</code>.
3. Move all the components inside of dj-say's `contact` folder into your contact application. Overwrite any duplicates such as `views.py` and `urls.py.`
4. Move all contents of the `templates` folder into your application's main template directory.
5. In your main `urls.py` make sure to include the new URLs by adding `url(r'^contact/', include('contact.urls')),`

### Setting up SMTP and Mail Access

For dj-say to work, you're going to need some kind of [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) access. By giving your `settings.py` access to some kind of SMTP-driven email address, your application will then send emails to that account automatically!

There are plenty of good SMTP services, both free and paid. I recommend using [Google SMTP](https://support.google.com/a/answer/176600?hl=en) for small projects, though for larger projects where you need additional support and infrastructure there are excellent paid services, like [SendGrid](https://sendgrid.com/).

To set this up, include this code in your `settings.py`:

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 000 # Make sure to change this depending on your host's designated SMTP port
EMAIL_HOST = '' # Your SMTP host
EMAIL_HOST_USER = '' # Your SMTP email address
EMAIL_HOST_PASSWORD = '' # Your SMTP email address password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

### CSS ###
To include CSS in your contact form, add the typical `link` element to the HTML template `contact_form.html`.

`<link rel="stylesheet" href="{% static 'your_css.css' %}" />`

As for writing the actual CSS itself, all of the text boxes are HTML `input` elements, while the labels are (obviously) `label` elements.

Some sample code: 
```
label {
  display: block;
  margin-top: 5px;
  margin-bottom: 5px;
  font-family: Helvetica;
  color: #63635F;
}

input {
  width: 400px; /* Set box width. */
  color: #63635F; /* Set text color for input box. */
}
```

The submit button itself can be customized with:

```
button #submit {
  width: 400px;
}
```

### Adding your own form components

The form shipped with dj-say consists of 4 lines: name, e-mail address, subject, and content, followed by a submission button.

As an example case, we'll say the new component is an additional text field for specifying what your favorite type of horse is.

Start with the `form.py` file, and add this line:

`contact_favorite_horse = forms.CharField(required=True)`

Then move to `views.py`. Find where the rest of your components are specified into `POST` variables and add this line:
`contact_favorite_horse = request.POST.get('contact_favorite_horse', '')`

Then, move down the file until you find where the variable called `context` is declared. `context` is an array of key-value pairs. Add your horse info to the context.

'favorite_horse': contact_favorite_horse,

The last step is to make sure that you include this new information in your `message_template.html` file, which is what Django sends to your SMTP service.

In `message_template.html` add: ` Favorite Horse: {{ favorite_horse }}`

Ta-da! Your new element should be implemented. 

# License

dj-say is registred under the MIT License. This project is free to use, modify, and redistribute by anybody. 

# Get in Touch

Trying to reach me? Shoot me a message on [my site!](http://www.evklein.com/contact/)
