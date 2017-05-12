material-react
==============

Bootstrap for Material-UI + React + Redux...

Usage
-----

Here's how to use this boostrapper -- assuming you're in this project's directory:

1. Install `nodejs v6.10.0` ...using apt-get, brew, etc.
2. Install JS libs: `npm install`
3. Run test-server: `npm start`

..In a second shell, launch the backend:

1. `cd backend`
2. `./serve`

Test
----

1. Test main page: `http://localhost:3000`
2. Test backend: `http://localhost:5000/api/index`
3. Test backend via proxy: `http://localhost:3000/api/index`


Construction
------------

Here are some notes on how I made it:

1. Install `nodejs v6.10.0`
2. Install FB's react starter: `npm install -g create-react-app`
3. In my `~/dev` : `create-react-app material-react/`
4. Move over README, replace with this file.
5. Adding `backend` folder to host a simple Python REST service.
6. Added `proxy` entry to `package.json`.
7. ...
