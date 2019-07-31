# Falcon Rest Boilerplate

That boilerplate can help you start a new REST appliaction based on Falcon 
Framewrok.

## What Is Inside?
- Falcon - Web framework for building speedy web APIs
- redis-astra - Redis ORM provider
- Marshmallow - Library to simplified object serialization

## System Requirements
- Python 3.7
- pipenv

## How Does It Work?
### Applications
Some solutions was inspired by Django, but this one has very simple implementation by design. The main idea gatchered from Django is: your project will have some dedicated logical blocks of code, called applications.

`app.py` it the only entrypoint. When you start it, it will try to load all packages from `applications` (see `settings.yaml`) and then it will call `on_ready` function on each application if that function existed there.

`on_ready` function receives reference to `AppManager` instance — this is applications common storage with one significant method: `export`. Applications can interact with each other through exported names.

For example, let's look at `src/rest/__init__.py`. On the `on_ready` function creates Falcon application and then that application exported under "rest" name. Then let's look at `src/api/__init__.py`. There is `add_route` method. This method will be called on Falcon application. Because `app.rest` is our application now.

Also there are system applications made by this way. System application do not mentioned in `applications` settings section. That applications will be run before the others during startup. One of them is `Commands` application. That application is avaliable for the others applications as `app.commands`. Thanks to this application, you can register your own commands to run throught the `app.py`. A good example contains in the `rest` application: `app.commands.register('rest', handler)`. It means you can run `app.py rest` and the `handler` will be called.


### ORM And Serializers
Redis-astra is simpler than ORM in Django. You should just define model's fields. You also may define static method for object creation (see `models/member.py`). There is no save or commit methods: working with objects directly affects database. More info you can find on redis-astra page.
Marshmallow's serializers are used for objects representation (see `serializers/member.py`). It allows to use great features like custom fields in the answer.

## Demo Application
`api/` directory contains an example of working as a REST service. Let's use httpie to communicate with our demo app:

```
# Create an member:
> http PUT http://localhost:8000/member/1 name='New member' email=test@domain.com age=24

# Get member:
> http GET http://localhost:8000/member/1

# Get only several member's fields:
> http GET http://localhost:8000/member/1?fields=id,name

# Update member:
> http POST http://localhost:8000/member/1 name='Our member' age=25
```





