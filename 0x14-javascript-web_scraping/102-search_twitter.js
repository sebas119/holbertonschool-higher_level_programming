#!/usr/bin/node

const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const API_KEY = process.argv[2] || '9U79aFfXb2AGxkNGXNEtZzN9X';
const API_SECRET = process.argv[3] || '9hCPFl23d1GzuLnZiCHGoT2PWKJql38AXleRUUQaOVP8jDwhnf';
const API_TOKENS = `${API_KEY}:${API_SECRET}`;
const API_TOKENS_ENCODED = base64.encode(utf8.encode(API_TOKENS));

const opAuth = {
  url: 'https://api.twitter.com/oauth2/token',
  headers: {
    Authorization: `Basic ${API_TOKENS_ENCODED}`,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  form: {
    grant_type: 'client_credentials'
  }
};

const authRequest = async (options) => {
  return new Promise((resolve, reject) => {
    request.post(opAuth, (error, response, body) => {
      if (!error) {
        resolve(JSON.parse(body).access_token);
      }
    });
  });
};

const searchRequest = async (bearerToken) => {
  const opSearch = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: {
      Authorization: `Bearer ${bearerToken}`
    },
    qs: {
      q: process.argv[4] || '#cisfun',
      count: '5'
    }
  };
  return new Promise((resolve, reject) => {
    request.get(opSearch, (error, respose, body) => {
      if (!error) {
        resolve(JSON.parse(body).statuses);
      }
    });
  });
};

const main = async () => {
  const accessToken = await authRequest(opAuth);
  const statuses = await searchRequest(accessToken);
  for (const tweet of statuses) {
    console.log(`[${tweet.id}] ${tweet.text} by ${tweet.user.name}`);
  }
};
main();
