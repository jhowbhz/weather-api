### Weather for Lat Long IP (Previsão do tempo por latitude e longitude)
Is a simple API develop in PYTHON and Flask, to integration in OpenWeatherMap for free user :)
# API Doc

## get temperature and climate for city and state 
<u>Climate for city and state</u>

``GET : /api/weather?city=Belo%20Horizonte,minas%20gerais``
<hr>

## Get status session
<u>Status Session</u>

``GET : https://whatsapp.contrateumdev.com.br/status?sessionName=MySession99/``
<hr>

## Finish close session
<u>Close Session</u>

``GET : https://whatsapp.contrateumdev.com.br/close?sessionName=MySession99/``
<hr>

## Get QR CODE
<u>Get QRCODE</u>

``GET : https://whatsapp.contrateumdev.com.br/qrcode?sessionName=MySession99&image=true``
> - image
<hr>

## Get QR CODE
<u>Get QRCODE base64</u>

``GET : https://whatsapp.contrateumdev.com.br/qrcode?sessionName=MySession99``
> - json (base64) ** recommended
<hr>

## Request send message
<u>Send Message</u>

``GET : https://whatsapp.contrateumdev.com.br/sendText``
> Request Body
> - sessionName - name of session started
> - number - number with code of country
> - text - text of send to number
<hr>

## Request send files
<u>Send Files</u>

``GET : https://whatsapp.contrateumdev.com.br/sendFile``
> Request Body
> - sessionName - name of session started
> - number - number with code of country
> - base64Data:"44696d61",//hexadecimal
> - fileName: "test.txt",
> - caption - text (optional)
<hr>

### Example JS send message (POST method)

```javascript
$.post({
  method: 'POST',
  url: `https://whatsapp.contrateumdev.com.br/sendText`,
  contentType:"application/json; charset=utf-8",
  dataType:"json",
  data: JSON.stringify({
      sessionName: `session99`,
      number: `5531995360492`,
      text: `Olá`
  }),
  success: function(resultado, status, xhr) {
      console.log(resultado)
  }
}) 
```

### Example JS send File (POST method)

```javascript
$.post({
  method: 'POST',
  url: `https://whatsapp.contrateumdev.com.br/sendFile`,
  contentType:"application/json; charset=utf-8",
  dataType:"json",
  data: JSON.stringify({
     sessionName: "session99", 
      number: '556334140378',
      base64Data:"44696d61", //hexadecimal
      fileName:"test.txt",
      caption: "Document" //optional
  }),
  success: function(resultado, status, xhr) {
      console.log(resultado)
  }
}) 

```