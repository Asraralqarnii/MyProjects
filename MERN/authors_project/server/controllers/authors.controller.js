const { Author } = require('../models/authors.model');



module.exports.createAuthor = (request, response) => {
    const {Name} = request.body;
    Author.create({
        Name
    })
        .then(author => response.json(author))
        .catch(err => response.status(400).json(err));
}

module.exports.getallauthors = (request, response) => {
    Author.find({})
    .then(author => response.json(author))
        .catch(err => response.json(err));
}
module.exports.updateAuthor = (request, response) => {
    Author.findOneAndUpdate({_id: request.params._id}, request.body, {new:true , runValidators: true,})
        .then(updatedauthor=> response.json(updatedauthor))
        .catch(err => response.status(400).json(err));
}
module.exports.deleteAuthor = (request, response) => {
    Author.deleteOne({ _id: request.params._id })
        .then(deleteConfirmation => response.json(deleteConfirmation))
        .catch(err => response.json(err))
}
module.exports.getOneauthor = (req, res) => {
    Author.findOne({ _id: req.params._id })
        .then((oneSingleProduct) => {res.json(oneSingleProduct)
        })
        .catch((err) => {res.json(err)
        })
}