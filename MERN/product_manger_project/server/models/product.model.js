const mongoose = require('mongoose');
const ProductManagerSchema = new mongoose.Schema({
    Title: { type: String },
    Price: { type: Number },
    Description: { type: String }

}, { timestamps: true });
module.exports.ProductManager = mongoose.model('ProductManager', ProductManagerSchema);

