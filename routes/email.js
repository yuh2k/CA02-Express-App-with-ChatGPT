require('dotenv').config();
const express = require('express');
const router = express.Router();
const Email = require('../models/Email');
const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
const openai = new OpenAIApi(configuration);
isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }
  

const getIndex = async (req, res) => {
    const emails = await Email.find();
    res.render('email', { emails });
};

const createReply = async (req, res) => {
    const inputEmail = req.body.email;
    const answer =  await openai.createCompletion({
        model: "text-davinci-003",
        prompt: "Generate the reply to the email",
        max_tokens:2048,
        n:1,
        temperature:0.8,
    });
  
    const outputEmail = answer.data.choices[0].text;
    const email = new Email({ inputEmail, outputEmail });
    await email.save();
    res.redirect('/emailReply');
};

const getEmailReply = async (req, res) => {
    const emails = await Email.find();
    res.render('emailReply', { emails });
};

const deleteEmail = async (req, res) => {
    const emailId = req.params.id;
    await Email.findByIdAndDelete(emailId);
    res.redirect('/email');
};

router.get('/email', isLoggedIn, getIndex);
router.post('/reply', isLoggedIn, createReply);
router.get('/emailReply', isLoggedIn, getEmailReply);
router.delete('/emailReply/:id', isLoggedIn, deleteEmail);

module.exports = router;