const mongoose = require('mongoose');
const AuthorSchema = new mongoose.Schema({
    Name: { type: String,
    required: [true, "{PATH} is required"],
    minlength: [3, "{PATH} must be at least {MINLENGTH}"], },
}, { timestamps: true });

module.exports.Author = mongoose.model('Author', AuthorSchema);

