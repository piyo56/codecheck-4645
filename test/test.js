"use strict";

const assert = require("chai").assert;
const codecheck = require("codecheck");

const COMMAND = process.env.APP_COMMAND;

describe("Test with valid parameters", () => {
  const app = codecheck.consoleApp(COMMAND);
  const cases = require("./01_valid-cases.json");
  cases.forEach(v => {
    let desc = v.it || `${v.input} =>=> ${v.output}`;
    it(desc, () => {
      return app.codecheck(v.input.split(" "))
        .then(result => {
          assert.equal(result.code, 0);
          assert.equal(result.stdout[0], v.output);
        });
    });
  });
});

describe("Test with invalid parameters", () => {
  const app = codecheck.consoleApp(COMMAND);
  const cases = require("./02_invalid-args.json");
  cases.forEach(v => {
    let desc = v.it || `${v.input} =>=> ${v.output}`;
    it(desc, () => {
      return app.codecheck(v.input.split(" "))
        .then(result => {
          assert.equal(result.code, 0);
          assert.equal(result.stdout[0], v.output);
        });
    });
  });
});

describe("Test with invalid range", () => {
  const app = codecheck.consoleApp(COMMAND);
  const cases = require("./03_invalid-range.json");
  cases.forEach(v => {
    let desc = v.it || `${v.input} =>=> ${v.output}`;
    it(desc, () => {
      return app.codecheck(v.input.split(" "))
        .then(result => {
          assert.equal(result.code, 0);
          assert.equal(result.stdout[0], v.output);
        });
    });
  });
});
