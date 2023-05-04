'use strict';
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

const emailSchema = new mongoose.Schema({
  inputEmail: String,
  outputEmail: String,
  userId: {type:ObjectId, ref:'user' }
});

module.exports = mongoose.model('Email', emailSchema);