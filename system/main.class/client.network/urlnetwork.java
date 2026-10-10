// Apache HttpClient example
CloseableHttpClient client = HttpClients.createDefault();
HttpGet request = new HttpGet("https://xmlserver.phonrathana.stoer.com/data.xml");
request.setConfig(RequestConfig.custom()
    .setConnectTimeout(5000)
    .setSocketTimeout(10000)
    .build());
try (CloseableHttpResponse response = client.execute(request)) {
    // Process XML
}