const { Transaction } = require('../models/transactions.model');


module.exports.createTransaction = (request, response) => {
    Transaction.create(request.body)
        .then(transaction => response.json(transaction))
        .catch(err => response.status(400).json(err));
}

module.exports.getallTransactions = (request, response) => {
    Transaction.find({})
    .then(transaction => response.json(transaction))
        .catch(err => response.json(err));
}
module.exports.deleteTransaction = (request, response) => {
    Transaction.deleteOne({ _id: request.params._id })
        .then(deleteConfirmation => response.json(deleteConfirmation))
        .catch(err => response.json(err))
}
module.exports.getOneTransaction = (req, res) => {
    Transaction.findOne({ _id: req.params._id })
        .then((oneSinglepmovie) => {res.json(oneSinglepmovie)
        })
        .catch((err) => {res.json(err)
        })
}

module.exports.updateTransaction = (request, response) => {
    Transaction.findOneAndUpdate({_id: request.params._id}, request.body, {new:true , runValidators: true,})
        .then(updatedtransaction=> response.json(updatedtransaction))
        .catch(err => response.status(400).json(err));
}