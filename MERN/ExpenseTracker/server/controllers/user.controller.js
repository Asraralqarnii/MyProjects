const User = require("../models/User.model")
const jwt = require("jsonwebtoken")
const bcrypt = require('bcrypt')

module.exports = {
  register: (req, res) => {
    User.create(req.body)
      .then((user) => {
        const userToken = jwt.sign({ id: user._id }, process.env.MY_SECRET)

        res.cookie("mycookie", userToken, { httpOnly: true }).json({
          message: "This response has a cookie",
          user,
        })
      })
      .catch((err) => res.status(400).json(err))
  },
  login: async (req, res) => {
    const user = await User.findOne({ email: req.body.email })

    if (user === null) {
      console.log(user)
      return res.sendStatus(400)
    }

    const correctPassword = await bcrypt.compare(
      req.body.password,
      user.password
    )

    if (!correctPassword) {
      return res.sendStatus(400)
    }

    const userToken = jwt.sign(
      {
        id: user._id,
      },
      process.env.MY_SECRET
    )

    res
      .cookie("mycookie", userToken, process.env.MY_SECRET, {
        httpOnly: true,
      })
      .json({ msg: "success!", user })
  },
  getAll: (req, res) => {
    User.find({})
      .then((users) => {
        console.log(users)
        res.json({ users })
      })
      .catch((err) => res.status(400).json(err))
  },
  logout: (req, res) => {
    res.clearCookie("mycookie")
    res.sendStatus(200)
  },
}
