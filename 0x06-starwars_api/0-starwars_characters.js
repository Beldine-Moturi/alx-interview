#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const baseUrl = 'https://swapi-api.hbtn.io/api/';

request.get(`${baseUrl}films/${id}`, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const result = body.characters;
  // console.log(result);

  listActors(result);
});

function listActors (result, i = 0) {
  if (i === result.length) return;

  request(result[i], { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }

    console.log(body.name);
    listActors(result, i + 1);
  });
}
