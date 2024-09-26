[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dVvYLkYY)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12424414)
## Dad Jokes API Server

For this project you're going to create an API server that returns Dad Jokes as JSON.

### Routes
You're API application needs to serve the following routes.

All routes should return an `application/json` content type and appropriate HTTP status code. 

#### Home
`/`
Must return JSON `{'success': True, 'message': 'This is the home page'}` with a `application/json` content type and a 200 status header.

#### Random Joke
`/random`
Should pull a random joke out of `dadjokes.json` and send it back to the browser. 

An example request may return the following JSON string.

```json
{
    "id": "b6dc0870",
    "name": "Color Blind",
    "joke": "Found out I was colour blind the other day... That one came right out the purple."
}
```

Subsequent runs should return different jokes, although the tester does account for the fact that random isn't always random. 


#### Specific Joke
`/joke`

This route allows you to request a specific joke from the data file by passing an `id` parameter. For example, if you want to get joke #123 the request would be `/joke?id=123`. 

`/joke?id=c9aaad4d` should return the following JSON string.

```json
{
    "id": "c9aaad4d",
    "name": "The Royal Flush Of The Jungle",
    "joke": "Why shouldn't you play cards in the jungle? Too many cheetahs."
}
```

You will need to check that the id parameter is there. If it is not, your server should return a 404 status header.

If the requested joke id is not in the data you should also send a 404 status header. 

### More info about status codes
[HTTP Status Cats](https://http.cat/)

[HTTP Status Dogs](https://httpstatusdogs.com/)

[List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) 

### Credit
`dadjokes.json` came from [GitHub](https://github.com/mshwery/dad-jokes-api)