// Set proxy for HTTP (use https.proxy* for HTTPS)
System.setProperty("http.proxyHost", "proxy.example.com");
System.setProperty("http.proxyPort", "443");
// Bypass proxy for internal servers (optional)
System.setProperty("http.nonProxyHosts", "*.internal.example.com|localhost");