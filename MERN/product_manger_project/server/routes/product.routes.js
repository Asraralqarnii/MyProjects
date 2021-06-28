const ProductManagerController = require('../controllers/product.controller');
module.exports = function(app){
    app.get('/api/productmanger', ProductManagerController.getAllProductManger);
    app.post('/api/productmanger', ProductManagerController.createProductManager);
    app.get('/api/productmanger/:_id', ProductManagerController.getOneSingleProduct); 
    app.put('/api/productmanger/:_id', ProductManagerController.updateProduct);
    app.delete('/api/productmanger/:_id', ProductManagerController.deleteProduct);






}

