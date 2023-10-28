# Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is traditionally considered a scripting language used primarily on the backend. Python runs on the Python interpreter. Javascript was designed to run in most web browsers, running on the front end to  provide interactivty to websites. : Python is considered a strongly typed language,requiring explicit conversion of types and strict type checking.Javascript is a loosely typed language meaning it doesn't strictly enforce variable types and allows for more flexibility in type conversions.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  In Python, you can use the **_get** method to access a key, as well as check for the existince of a key using the **_in** operator. In both instances, a default value could be returned if the key is not in the dictionary, avoiding a KeyError and crashing th eprogram.

- What is a unit test?
A unit test is involves testing code in isolated small pieces . Typically unit testing focuses one specific function or method.

- What is an integration test?
Integration testing invovles grouping multiple units to perform tests. The purpose of integration testing is to ensure that multiple components can work together.

- What is the role of web application framework, like Flask?
A web framework like Flask faciliates web development with Python. Hence Python could be used for both front end and back end development.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  Passing a parameter in a route URL is best for unique identifiers or essential criteria, making the URL more readable and descriptive.
  Query parameters would work well when utilizing functionality involving search parameters, optional or additional parameters,or other non essential data to avoid cluttering the route structure.

- How do you collect data from a URL placeholder parameter using Flask?
When defining an endpoint ,this parameter is passed as a parameter to the  view function definition for the respective endpoint.This URL placeholder parameter is then available for use within the function.

- How do you collect data from the query string using Flask?
In Flask, you can collect data from the query string using request.args.

- How do you collect data from the body of the request using Flask?
Datafrom the body of the request can be accessed using request.form for form data or request.get_json() for JSON data.

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data stored in a user's web browser by a website they visit. It contains information about the user's interactions with the site, such as login credentials, preferences, or items in a shopping cart.They help websites recognize and remember users, to improve the user experience.

- What is the session object in Flask?
this object allows for the storage of  user-specific information across multiple HTTP requests. It maintains state and user-specific data without the need to repeatedly pass information between the client and server.

- What does Flask's `jsonify()` do?
`jsonify()`serializes data to JavaScript Object Notation (JSON) format and wraps it in a Response object. This facilitates the transmission and parsing of data between a server and a client,and is commonly used when making api calls.
