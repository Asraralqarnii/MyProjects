const mongoose = require('mongoose');
const TransactionSchema = new mongoose.Schema({
    Name: { type: String,
    required: [true, "{PATH} is required"],
    minlength: [3, "{PATH} must be at least {MINLENGTH}"], 
},
  Category:{
    type: String,
    required: [true, "{PATH} is required"],
  },
  Type:{
    type: String,
    required: [true, "{PATH} is required"],
  },
  Amount:{
    type: Number,
    required: [true, "{PATH} is required"],
    minlength: [1, "{PATH} must be at least {MINLENGTH}"],
  },
  Date:{
    type: Date,
    required: [true, "{PATH} is required"],
  },
},{ timestamps: true });

module.exports.Transaction = mongoose.model('Transaction', TransactionSchema);

