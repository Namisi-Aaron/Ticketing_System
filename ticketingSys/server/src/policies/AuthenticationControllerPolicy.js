const Joi = require('joi')

module.exports = {
    register (req, res, next) {
        const schema = Joi.object ({
            password: Joi.string().regex(
                new RegExp('^[a-zA-Z0-9]{8, 32}$')
            )
        })
        const {error, value} = schema.validate(req.body)

        if (error) {
            switch (error.details[0].context.key) {
                case 'password':
                    res.status(400).send({
                        error: 'Password must be more than 8 characters long'
                        })
                        break
                    default:
                        res.status(400).send({
                            error: 'invalid registration details'
                            })
                        }
                    }
        else {
            next()
        }
    }
}
