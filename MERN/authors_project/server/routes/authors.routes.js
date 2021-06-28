const AuthorController = require('../controllers/authors.controller');
module.exports = function(app){
    
    app.get('/api/authors', AuthorController.getallauthors);
    app.post('/api/authors', AuthorController.createAuthor);
    app.get('/api/authors/:_id', AuthorController.getOneauthor);
    app.put('/api/authors/:_id', AuthorController.updateAuthor);
    app.delete('/api/authors/:_id', AuthorController.deleteAuthor);

}

