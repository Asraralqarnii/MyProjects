const { ProductManager } = require('../models/product.model');
module.exports.getAllProductManger = (request, response) => {
    ProductManager.find({})
    .then(product => response.json(product))
        .catch(err => response.json(err));
}

module.exports.getOneSingleProduct = (req, res) => {
    ProductManager.findOne({ _id: req.params._id })
        .then((oneSingleProduct) => {res.json(oneSingleProduct)
        })
        .catch((err) => {res.json(err)
        })
}
    // The method below is new
module.exports.createProductManager = (request, response) => {
    const { Title, Price,Description } = request.body;
    ProductManager.create({
        Title,
        Price,
        Description
    })
        .then(product => response.json(product))
        .catch(err => response.json(err));
}

module.exports.updateProduct = (request, response) => {
    ProductManager.findOneAndUpdate({_id: request.params._id}, request.body, {new:true})
        .then(updatedProduct => response.json(updatedProduct))
        .catch(err => response.json(err))
}
module.exports.deleteProduct = (request, response) => {
    ProductManager.deleteOne({ _id: request.params._id })
        .then(deleteConfirmation => response.json(deleteConfirmation))
        .catch(err => response.json(err))
}




