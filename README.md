# API Doc
### Weather for Lat Long IP (Previsão do tempo por latitude e longitude)
Is a simple API develop in PYTHON and Flask, to integration in OpenWeatherMap for free user :)
## Climate for city and state
<u>get temperature and climate for city and state </u>

``GET : /api/weather/city/?city=Belo%20Horizonte,minas%20gerais``
<hr>

## Climate for latitude longitude
<u>get temperature and climate for latitude longitude </u>

``GET : /api/weather?lat=-19.8218131&lon=-44.0094874``
<hr>

### Example city JS

```javascript
$.post({
  method: 'GET',
  url: `https://weather.contrateumdev.com.br/api/weather/city/?city=Belo%20Horizonte,minas%20gerais`,
  contentType:"application/json; charset=utf-8",
  dataType:"json",
  success: function(resultado, status, xhr) {
      console.log(resultado)
  }
}) 
```

### Example lat & lon JS

```javascript
$.post({
  method: 'GET',
  url: `https://weather.contrateumdev.com.br/api/weather/api/weather?lat=-19.8218131&lon=-44.0094874`,
  contentType:"application/json; charset=utf-8",
  dataType:"json",
  success: function(resultado, status, xhr) {
      console.log(resultado)
  }
}) 

```