### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  * Python has varibles types that are interpreted at runtime. It is also server-side developemnt and used for data science, machine learning, and scripting. Python also has it's own intrepeter for code exectuion. Python is traditionally used for threading concurrency and uses indentation to define code blocks. 
  
  * Javascript is loosely typed due to automatic type coercion. Javascript is commonly used for front-end development, cross-platform mobile appps and server-side development with Node.JS. JS is executed by the browser on the front-end or by Node.JS via runtime on the back-end. It also uses an event-driven, non-block model, and uses curly braces for code block.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    * The `get` method can be used:
        my_dict = {"a": 1, "b": 2}
        value = my_dict.get("c", None)

    * Using a Conditional Statement can also be used:
        my_dict = {"a": 1, "b": 2}
          key = "c"
          if key in my_dict:
              value = my_dict[key]
          else:
              value = None

- What is a unit test?
  It is software testing the units or components being tested in isolation. The goal is to ensure that each unit perdorms as designed.

- What is an integration test?
  This is to ensure that the units or components of an application are tested in combination and work as intented.

- What is the role of web application framework, like Flask?
  Flask is a web application framework for Python. Its role includes simplifying the process of building web applications by providing tools, libraries, and patterns for tasks such as routing, handling HTTP requests and responses, and managing sessions.

- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?
  Using a route paprameter is great for when the data is essential to the resource being identified in the URL. Otherwise query parameters when the data is optional like the later URL.

- How do you collect data from a URL placeholder parameter using Flask?
    Using the previous example of food and example of a URL placeholder parameter:
    @app.route('/foods/<food_type>')
    def get_food(food_type):

- How do you collect data from the query string using Flask?
    @app.route('/food')
    def get_food():
      food_type = request.args.get('type')

- How do you collect data from the body of the request using Flask?
    @app.route('/foods', methods=['POST'])
    def create_():
      data = request.json

- What is a cookie and what kinds of things are they commonly used for?
    Cookies are small pieces of data that is stored on the client's computer to manage their sessions, personalization, and tracking the user's behavior.

- What is the session object in Flask?
    In Flask, the session object is a dictionary-like object that allows you to store data across requests. It uses cookies to store a session identifier on the client side and keeps the data on the server side.

- What does Flask's `jsonify()` do?
    It is a function in Flask that converts a Python dictionary into a JSON response. It sets the appropriate Content-Type header for JSON and returns a JSON-formatted response. It is commonly used in API development.