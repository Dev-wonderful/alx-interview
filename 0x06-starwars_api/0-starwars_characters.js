#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

function people (charactersArr, index) {
  if (index < charactersArr.length) {
    request(charactersArr[index], function (error, response, body) {
      if (error) {
        console.error(error);
      } else {
        const name = JSON.parse(body).name;
        console.log(name);
        people(charactersArr, index + 1);
      }
    });
  }
}

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    people(characters, 0);
  }
});