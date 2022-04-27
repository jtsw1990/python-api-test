# python-api-test
Repository to deploy sample insurance pricing api

- [Endpoint](https://insurance-pricing-api.herokuapp.com/)
- [Pricing Webapp github](https://github.com/jtsw1990/webapp-pricingengine)


High-level architecture
- Batch-trained (for now) Python GLM model
- Flask API wrapper
- Heroku as a free hosting service (Refer to endpoint) 
- Will be called by [Pricing webapp](https://github.com/jtsw1990/webapp-pricingengine) using Nodejs/Fetch/Axios


# Tools and tech stack
## Model
- `statsmodel` library to implement a generalised linear model
- Gamma distribution assumption, log link function

## API
- `Flask` to wrap around the model
- Schema defined in app.py (Can be abstracted out)
- `GET` returns schema
- `POST` returns following given schema:
```
{ 
    "claims_cost" : $K, 
    "coefficients" : {
      "coef1" : K1,
      "coef2" : K2
    }  
}
```


## Deployment
- Heroku used as a platform to host the API
- `Heroku cli` used as git integration frontend is down
- Steps to update model:
    - `git add`
    - `git commit -m <message>`
    - `git push heroku main`
