const {User} = require('../models')

module.exports = {
    async login (req, res) {
        try {
            const user = await User.create(req.body)
            res.send(user.toJSON())
        } catch (err) {
            res.status(400).send({
                error: 'User already exists.'
            })
        }        
    }
}