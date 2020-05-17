"use strict";

module.exports.hello = function(event, context, callback) {
  const response = {
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Origin": "*", // Required for CORS support to work
      "Access-Control-Allow-Credentials": true, // Required for cookies, authorization headers with HTTPS
    },
    body: JSON.stringify({ message: "Hello World!" }),
  };

  callback(null, response);
};
