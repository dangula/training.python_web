week 5 Homework
Part 1 - Blog app running on Flask
1. Finished reworking blog app.
2. Flask app is installed on VM at  - http://block647038-n5j.blueboxgrid.com

Part 2- Re-implement Blog app with bottle:
 I had to try really hard to get the blog app working in a different small framework.
 I short I came to a conclusion that flask is the best/most helpful small framework out there.
I feel like flask has the right ratio of abstraction to freedom making it easy to use.
other small frameworks didn't provide enough abstraction making it hard to accomplish trival tasks.
 Some cool features provided by flask were missing in bottle(and webpy) for example, 
 bottle didn't have support for sessions or flash or loading properties into config.
 
 As a result here is along list of thinngs you have to do
 1. Create a bottle.db file in tmp dir
 2. run dbSetup.py(because bottle had no way to load propertis in config, hence no init_db())
 3. crate a new virtualenv and install bottle
 4. install jnija2(bottle uses it s own wierd templating system where you store files as .tpl)
 4. install bottle_sqlite plugin
 5. install beaker middleware for session management.(no native session management in bottle)
 6 . Now run bottler.py
 7 . go http://localhost:8080 to access your blog