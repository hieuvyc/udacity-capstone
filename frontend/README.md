
# Using get JWT from Auth0 

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

> _note_: If you are using Node.js version 17 or above, you might encounter issues due to OpenSSL changes. Use the following environment variable to avoid these issues:

```bash
export NODE_OPTIONS=--openssl-legacy-provider
```

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

```bash
sudo npm install -g @ionic/cli
```

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _note_: If you encounter issues with `node-sass`, ensure `sass` is installed instead:

```bash
npm uninstall node-sass
npm install node-sass@4.14.1
```
> _tip_: **npm i** is shorthand for **npm install**

> _note_: If you encounter an error related to python2 while installing dependencies, you might need to install Python  Use the following command if necessary:
```bash
brew install python@2
```

## Running Your Frontend in Dev Mode

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
export NODE_OPTIONS=--openssl-legacy-provider
ionic serve
```

> _tip_: Do not use **ionic serve** in production. Instead, build Ionic into a build artifact for your desired platforms.
> [Checkout the Ionic docs to learn more](https://ionicframework.com/docs/cli/commands/build)

## Get the token
- Go to: http://localhost:8100/
- Login with username and password to get the token
