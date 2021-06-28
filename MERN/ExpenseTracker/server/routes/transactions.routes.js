const TransactionsController = require('../controllers/transactions.controller');
module.exports = function(app){
    
    app.get('/api/expensetracker', TransactionsController.getallTransactions);
    app.post('/api/expensetracker', TransactionsController.createTransaction);
    app.get('/api/expensetracker/:_id', TransactionsController.getOneTransaction);
    app.put('/api/expensetracker/:_id', TransactionsController.updateTransaction);
    app.delete('/api/expensetracker/:_id', TransactionsController.deleteTransaction);

}

